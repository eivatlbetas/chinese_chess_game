from piece import Piece

class Board:
    def __init__(self):
        self.pieces = []  # 存储所有棋子的列表
        self.initialize_board()
        self.game_over = False
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

    def _is_game_over(self):
        return not any(piece.name == '帥' for piece in self.pieces) or not any(piece.name == '將' for piece in self.pieces)

    def _select_piece(self, position):
        piece = self.get_piece_at(position)
        if piece is not None:
            if piece.color == self.current_player:
                self.selected_piece = piece
                print(f'选中 {piece.color} {piece.name} {piece.position} 棋子，请移动。')
            else:
                print(f'这不是你的棋子，请选择 {self.current_player} 色棋子。')
        else:
            print(f'{position} 没有棋子，请重新选择。')

    def _move_piece_to(self, to_position):
        print(f'尝试将 {self.selected_piece.name} 移动到 {to_position}。')
        if self.is_move_legal(self.selected_piece, to_position):
            target_piece = self.get_piece_at(to_position)
            if target_piece and target_piece.color != self.selected_piece.color:
                self.pieces.remove(target_piece)
                print(f'{target_piece.color} 方的 {target_piece.name} 被吃掉。')
            self.selected_piece.move(to_position)
            self.selected_piece = None  # 移动成功后取消选择    

            if (self._is_game_over()):  # 检查游戏是否结束
                self.game_over = True  # 设置游戏结束标志
                print(f'游戏结束，{self.current_player} 方获胜！')
                return
            else:  # 游戏未结束，切换玩家
                self.current_player = '黑' if self.current_player == '红' else '红'
                print(f'移动成功，当前轮到 {self.current_player} 方。')
        else:
            print('移动失败，请重新移动。')

    def click_position(self, position):
        if self.selected_piece is None:  # 没有选中棋子，尝试选择
            self._select_piece(position)
        else:  # 已经选中棋子，尝试移动
            self._move_piece_to(position)
