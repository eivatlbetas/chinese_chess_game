from recorder import Recorder
from piece import Piece
from player import Player

class Board:
    def __init__(self):
        '''初始化棋盘
        Attributes:
            recorder: 棋谱记录器
            pieces: 棋子列表
            game_over: 游戏是否结束
            red_player: 红方玩家
            black_player: 黑方玩家 
            player_turn: 当前回合玩家
            selected_piece: 选中的棋子
        '''
        self.recorder = Recorder() # 初始化棋谱记录器
        self.pieces = []  # 存储所有棋子的列表
        self.initialize_board()
        self.game_over = False
        self.red_player = Player('红')  # 初始化红方玩家
        self.black_player = Player('黑')  # 初始化黑方玩家
        self.player_turn = self.red_player  # 初始时红方先行
        self.selected_piece = None  # 存储选中的棋子

    # 右下角坐标为（0,0），左上角坐标为（8,9），下方为红方，上方为黑方
    def initialize_board(self):
        '''初始化棋盘棋子位置'''
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

    def switch_player(self, color=None):
        '''切换当前玩家
        Args:
            color: 指定切换到的玩家颜色(可选)
        '''
        if color == '红':
            self.player_turn = self.red_player
        elif color == '黑':
            self.player_turn = self.black_player
        else: # 切换到下一个玩家，即红方变黑方，黑方变红方
            self.player_turn = self.black_player if self.player_turn == self.red_player else self.red_player

    def get_piece_at(self, position):
        '''获取指定位置的棋子
        Args:
            position: 位置坐标(x,y)
        Returns:
            棋子对象或None
        '''
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def _is_move_legal(self, piece, to_position):
        '''检查移动是否合法
        Args:
            piece: 棋子对象
            to_position: 目标位置
        Returns:
            bool: 是否合法
        '''
        possible_moves = piece.get_possible_moves(self)
        return to_position in possible_moves

    def _is_check(self, player):
        '''检查是否被将军
        Args:
            player: 玩家对象
        Returns:
            bool: 是否被将军
        '''
        # 找到自己的帅
        general_name = '帥' if player.color == '红' else '將'
        general = next((p for p in self.pieces if p.name == general_name), None)
        if not general:
            return False

        # 检查是否有对方棋子可以攻击到自己的帅
        for piece in self.pieces:
            if piece.color != player.color and piece.position != general.position:
                if general.position in piece.get_possible_moves(self):
                    return True
        return False

    def _is_checkmate(self):
        '''检查是否被将死
        Returns:
            bool: 是否被将死
        '''
        return False  # TODO:暂时不实现

    def _is_stalemate(self):
        '''检查是否困毙
        Returns:
            bool: 是否无棋可走
        '''
        for piece in self.pieces:
            if piece.color == self.player_turn.color and piece.get_possible_moves(self):
                return False
        return True

    def _is_game_over(self):
        '''检查游戏是否结束
        Returns:
            bool: 游戏是否结束
        '''
        # FIXME: 检查当前玩家是否无棋可走
        return (not any(piece.name == '帥' for piece in self.pieces)
             or not any(piece.name == '將' for piece in self.pieces))

    def _select_piece(self, position):
        '''选择棋子
        Args:
            position: 棋子位置
        '''
        if self.selected_piece is None:
            piece = self.get_piece_at(position)
            if piece is not None:
                if piece.color == self.player_turn.color:
                    self.selected_piece = piece
                    if self.selected_piece.get_possible_moves(self):
                        print(f'选中{self.selected_piece} 棋子，请移动。')
                    else:
                        print(f'{self.selected_piece}无位置移动，请右键取消选择。') 
                else:
                    print(f'这不是你的棋子，请选择{self.player_turn.color}色棋子。')
            else:
                print(f'{position}没有棋子，请重新选择。')
        else:
            print(f'已有棋子{self.selected_piece}被选中，请先取消选择。')

    def _move_piece_to(self, to_position):
        '''移动棋子到指定位置
        Args:
            to_position: 目标位置
        '''
        if self.selected_piece is not None:
            if self._is_move_legal(self.selected_piece, to_position):
                print(f'移动成功，将{self.selected_piece}移动到{to_position}。')
                # 检查是否吃子
                target_piece = self.get_piece_at(to_position)
                self.recorder.record_move(self.selected_piece.name, self.selected_piece.color, self.selected_piece.position, to_position, target_piece)
                if target_piece and target_piece.color != self.selected_piece.color:
                    self.pieces.remove(target_piece)
                    print(f'{target_piece}被吃掉。')
                self.selected_piece.move(to_position)
                self.selected_piece = None  # 移动成功后取消选择

                if self._is_game_over():  # 检查游戏是否结束
                    self.game_over = True 
                    print(f'游戏结束，{self.player_turn}获胜！')
                    return
                else:  # 游戏未结束
                    if self._is_check(self.player_turn):
                        print(f'{self.player_turn}被将军！')
                    self.switch_player() # 切换玩家
                    if self._is_check(self.player_turn):
                        print(f'{self.player_turn}被将军！')
                    print(f'当前轮到{self.player_turn}。') 
            else:
                if self.selected_piece.get_possible_moves(self):
                    print(f'无法将{self.selected_piece}移动到{to_position}，请重新选择。')
                else:
                    print(f'{self.selected_piece}无位置移动，请右键取消选择。')
        else:
            print('没有选中棋子，请先选择棋子。')

    def _undo_move(self):
        '''撤销上一步棋'''
        last_move, captured_piece = self.recorder.undo_move()
        if last_move:  # 确保有棋步可以撤销
            self.selected_piece = self.get_piece_at(last_move['to'])  # 获取上一步棋步的棋
            if self.selected_piece:  # 确保棋子存在
                self.selected_piece.move(last_move['from'])  # 恢复棋子位置
                if captured_piece:  # 如果有被吃掉的棋子
                    self.pieces.append(captured_piece)  # 恢复被吃掉的棋子
                    print(f'恢复了被吃掉的棋子{captured_piece}。')
                self.switch_player(last_move['color'])  # 切换回上一步的玩家
                self.selected_piece = None  # 取消选择
                self.game_over = False  # 重置游戏结束状态
                print(f'撤销了一步棋，当前玩家为{self.player_turn}。')
            else:
                print('错误：找不到要撤销的棋子。')
        else:
            print('没有可撤销的棋步。')

    def click_position(self, position):
        '''处理点击位置事件
        Args:
            position: 点击位置坐标(x,y)
        '''
        if self.selected_piece is None:  # 没有选中棋子，尝试选择
            self._select_piece(position)
        else:  # 已经选中棋子，尝试移动
            self._move_piece_to(position)

    def click_right(self):
        '''处理右键点击事件'''
        if self.selected_piece is not None:
            print(f'取消选择{self.selected_piece}。')
            self.selected_piece = None

    def click_key_Backspace(self): # Backspace键悔棋
        '''处理退格键悔棋事件'''
        if self.game_over:  # 游戏结束时不能悔棋
            print('游戏已经结束，无法悔棋。')
            return
        self._undo_move()
