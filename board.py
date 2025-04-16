from piece import Piece

class Board:
    def __init__(self):
        self.pieces = []  # 存储所有棋子的列表
        self.initialize_board()

        self.current_player = '红'  # 初始化当前玩家为红方
        self.selected_piece = None  # 存储选中的棋子

    # 右下角坐标为（0,0），左上角坐标为（8,9），下方为红方，上方为黑方
    def initialize_board(self):
        # 初始化红方各类棋子，包括俥、傌、相、仕、帥、砲、兵
        self.pieces.append(Piece('俥', '红', (0, 0)))
        self.pieces.append(Piece('傌', '红', (1, 0)))
        self.pieces.append(Piece('相', '红', (2, 0)))
        self.pieces.append(Piece('仕', '红', (3, 0)))
        self.pieces.append(Piece('帥', '红', (4, 0)))
        self.pieces.append(Piece('仕', '红', (5, 0)))
        self.pieces.append(Piece('相', '红', (6, 0)))
        self.pieces.append(Piece('傌', '红', (7, 0)))
        self.pieces.append(Piece('俥', '红', (8, 0)))
        self.pieces.append(Piece('砲', '红', (1, 2)))
        self.pieces.append(Piece('砲', '红', (7, 2)))
        for i in range(0, 9, 2):
            self.pieces.append(Piece('兵', '红', (i, 3)))

        # 初始化黑方各类棋子，包括車、馬、象、士、將、炮、卒
        self.pieces.append(Piece('車', '黑', (0, 9)))
        self.pieces.append(Piece('馬', '黑', (1, 9)))
        self.pieces.append(Piece('象', '黑', (2, 9)))
        self.pieces.append(Piece('士', '黑', (3, 9)))
        self.pieces.append(Piece('將', '黑', (4, 9)))
        self.pieces.append(Piece('士', '黑', (5, 9)))
        self.pieces.append(Piece('象', '黑', (6, 9)))
        self.pieces.append(Piece('馬', '黑', (7, 9)))
        self.pieces.append(Piece('車', '黑', (8, 9)))
        self.pieces.append(Piece('炮', '黑', (1, 7)))
        self.pieces.append(Piece('炮', '黑', (7, 7)))
        for i in range(0, 9, 2):
            self.pieces.append(Piece('卒', '黑', (i, 6)))

    def get_piece_at(self, position):
        # 获取指定位置的棋子
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_move_legal(self, piece, to_position):
        possible_moves = piece.get_possible_moves(self)
        return to_position in possible_moves

    def is_game_over(self):
        red_general = False
        black_general = False
        for piece in self.pieces:
            if piece.name == '帥':
                red_general = True
            elif piece.name == '將':
                black_general = True
        if not red_general:
            print('黑方胜利！')
            return '黑'
        elif not black_general:
            print('红方胜利！')
            return '红'
        return None

    def move_piece(self, piece, to_position):
        if self.is_move_legal(piece, to_position):
            target_piece = self.get_piece_at(to_position)
            if target_piece and target_piece.color != piece.color:
                self.pieces.remove(target_piece)
                print(f'{target_piece.color} 方的 {target_piece.name} 被吃掉。')
            piece.move(to_position)
            return True
        else:
            return False
            
