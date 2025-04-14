from piece import Piece

class Board:
    def __init__(self):
        self.pieces = []  # 存储所有棋子的列表
        self.initialize_board()

    def initialize_board(self):
        # 初始化红方各类棋子，包括俥、傌、相、仕、帥、砲、兵
        self.pieces.append(Piece('俥', 'red', (0, 0)))
        self.pieces.append(Piece('傌', 'red', (1, 0)))
        self.pieces.append(Piece('相', 'red', (2, 0)))
        self.pieces.append(Piece('仕', 'red', (3, 0)))
        self.pieces.append(Piece('帥', 'red', (4, 0)))
        self.pieces.append(Piece('仕', 'red', (5, 0)))
        self.pieces.append(Piece('相', 'red', (6, 0)))
        self.pieces.append(Piece('傌', 'red', (7, 0)))
        self.pieces.append(Piece('俥', 'red', (8, 0)))
        self.pieces.append(Piece('砲', 'red', (1, 2)))
        self.pieces.append(Piece('砲', 'red', (7, 2)))
        for i in range(0, 9, 2):
            self.pieces.append(Piece('兵', 'red', (i, 3)))

        # 初始化黑方各类棋子，包括車、馬、象、士、將、炮、卒
        self.pieces.append(Piece('車', 'black', (0, 9)))
        self.pieces.append(Piece('馬', 'black', (1, 9)))
        self.pieces.append(Piece('象', 'black', (2, 9)))
        self.pieces.append(Piece('士', 'black', (3, 9)))
        self.pieces.append(Piece('將', 'black', (4, 9)))
        self.pieces.append(Piece('士', 'black', (5, 9)))
        self.pieces.append(Piece('象', 'black', (6, 9)))
        self.pieces.append(Piece('馬', 'black', (7, 9)))
        self.pieces.append(Piece('車', 'black', (8, 9)))
        self.pieces.append(Piece('炮', 'black', (1, 7)))
        self.pieces.append(Piece('炮', 'black', (7, 7)))
        for i in range(0, 9, 2):
            self.pieces.append(Piece('卒', 'black', (i, 6)))

    def get_piece_at(self, position):
        # 获取指定位置的棋子
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def is_move_legal(self, piece, to_position):
        possible_moves = piece.get_possible_moves(self)
        return to_position in possible_moves

    def check_game_over(self):
        red_general = False
        black_general = False
        for piece in self.pieces:
            if piece.name == '帥':
                red_general = True
            elif piece.name == '將':
                black_general = True
        if not red_general:
            print('黑方胜利！')
            return 'black'
        elif not black_general:
            print('红方胜利！')
            return 'red'
        return None

    def move_piece(self, from_position, to_position, current_player):
        piece = self.get_piece_at(from_position)
        if piece:
            if piece.color != current_player:
                print(f'当前轮到 {current_player} 方，不能移动 {piece.color} 方的棋子。')
                return
            if self.is_move_legal(piece, to_position):
                target_piece = self.get_piece_at(to_position)
                if target_piece and target_piece.color != piece.color:
                    self.pieces.remove(target_piece)
                    print(f'{piece.color} 方的 {target_piece.name} 被吃掉。')
                piece.move(to_position, self)
