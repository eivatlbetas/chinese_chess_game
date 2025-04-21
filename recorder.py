class Recorder:
    def __init__(self):
        '''初始化记录器'''
        self.moves = []
        self.captured_pieces = []

    def record_move(self, piece_name, piece_color, from_pos, to_pos, captured_piece=None):
        '''记录一步棋
        Args:
            piece_name: 棋子名称
            piece_color: 棋子颜色
            from_pos: 起始位置
            to_pos: 目标位置
            captured_piece: 被吃掉的棋子(可选)
        '''
        move_number = len(self.moves) + 1
            
        move_record = {
            'move_number': move_number,
            'piece': piece_name,
            'color': piece_color,
            'from': from_pos,
            'to': to_pos,
            'captured_piece': captured_piece
        }
        self.moves.append(move_record)
        if captured_piece:
            self.captured_pieces.append(captured_piece)

    def get_last_move(self):
        '''获取最后一步记录
        Returns:
            最后一步记录, 被吃掉的棋子(可选)
        '''
        if not self.moves:
            return None, None
        last_move = self.moves[-1]
        return last_move, last_move.get('captured_piece')

    def pop_last_move(self):
        '''悔棋 - 移除最后一步记录
        Returns:
            最后一步记录, 被吃掉的棋子(可选)
        '''
        if not self.moves:
            return None, None

        move = self.moves.pop()
        if move.get('captured_piece'):
            return move, self.captured_pieces.pop()
        return move, None