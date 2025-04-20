class Recorder:
    def __init__(self):
        self.moves = []
        self.captured_pieces = []

    def record_move(self, piece_name, piece_color, from_pos, to_pos, captured_piece=None):
        """
        记录一步棋
        :param piece_name: 棋子名称
        :param piece_color: 棋子颜色
        :param from_pos: 起始位置
        :param to_pos: 目标位置
        :param captured_piece: 被吃掉的棋子信息
        """
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

    def undo_move(self):
        """
        悔棋 - 移除最后一步记录
        :return: 被移除的移动记录和被吃掉的棋子信息，如果没有记录则返回None
        """
        if not self.moves:
            return None, None
            
        move = self.moves.pop()
        if move.get('captured_piece'):
            return move, self.captured_pieces.pop()
        return move, None