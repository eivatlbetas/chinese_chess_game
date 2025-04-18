class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def __str__(self):
        return f'{self.color}{self.name}{self.position}'

    def move(self, new_position):
        self.position = new_position

    def get_possible_moves(self, board):
        # 根据棋子类型实现不同的移动逻辑
        if self.name in ['俥', '車']:
            moves = self._get_chariot_moves(board)
        elif self.name in ['傌', '馬']:
            moves = self._get_horse_moves(board)
        elif self.name in ['相', '象']:
            moves = self._get_elephant_moves(board)
        elif self.name in ['仕', '士']:
            moves = self._get_advisor_moves(board)
        elif self.name in ['帥', '將']:
            moves = self._get_general_moves(board)
        elif self.name in ['砲', '炮']:
            moves = self._get_cannon_moves(board)
        elif self.name in ['兵', '卒']:
            moves = self._get_soldier_moves(board)
        else:
            moves = []
        return moves

    def _get_chariot_moves(self, board):
        # 实现俥/車的移动逻辑
        moves = []
        x, y = self.position
        # 横向移动
        for dx in [-1, 1]:
            new_x = x + dx
            while 0 <= new_x < 9:
                target_piece = board.get_piece_at((new_x, y))
                if target_piece is None:
                    moves.append((new_x, y))
                elif target_piece.color != self.color:
                    moves.append((new_x, y))
                    break
                else:
                    break
                new_x += dx
        # 纵向移动
        for dy in [-1, 1]:
            new_y = y + dy
            while 0 <= new_y < 10:
                target_piece = board.get_piece_at((x, new_y))
                if target_piece is None:
                    moves.append((x, new_y))
                elif target_piece.color != self.color:
                    moves.append((x, new_y))
                    break
                else:
                    break
                new_y += dy
        return moves

    def _get_horse_moves(self, board):
        # 实现傌/馬的移动逻辑
        moves = []
        x, y = self.position
        offsets = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 9 and 0 <= new_y < 10:
                # 蹩马腿检查
                if abs(dx) == 2:
                    blocked_x = x + dx // 2
                    if board.get_piece_at((blocked_x, y)) is None:
                        target_piece = board.get_piece_at((new_x, new_y))
                        if target_piece is None or target_piece.color != self.color:
                            moves.append((new_x, new_y))
                else:
                    blocked_y = y + dy // 2
                    if board.get_piece_at((x, blocked_y)) is None:
                        target_piece = board.get_piece_at((new_x, new_y))
                        if target_piece is None or target_piece.color != self.color:
                            moves.append((new_x, new_y))
        return moves

    def _get_elephant_moves(self, board):
        # 实现相/象的移动逻辑
        moves = []
        x, y = self.position
        offsets = [(2, 2), (-2, 2), (2, -2), (-2, -2)]
        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if self.color == '红' and new_y >= 5:
                continue
            if self.color == '黑' and new_y < 5:
                continue
            if 0 <= new_x < 9 and 0 <= new_y < 10:
                # 塞象眼检查
                blocked_x = x + dx // 2
                blocked_y = y + dy // 2
                if board.get_piece_at((blocked_x, blocked_y)) is None:
                    target_piece = board.get_piece_at((new_x, new_y))
                    if target_piece is None or target_piece.color != self.color:
                        moves.append((new_x, new_y))
        return moves

    def _get_advisor_moves(self, board):
        # 实现仕/士的移动逻辑
        moves = []
        x, y = self.position
        offsets = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        palace_x_range = (3, 5)
        if self.color == '红':
            palace_y_range = (0, 2)
        else:
            palace_y_range = (7, 9)
        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if palace_x_range[0] <= new_x <= palace_x_range[1] and palace_y_range[0] <= new_y <= palace_y_range[1]:
                target_piece = board.get_piece_at((new_x, new_y))
                if target_piece is None or target_piece.color != self.color:
                    moves.append((new_x, new_y))
        return moves

    def _get_general_moves(self, board):
        # 实现帥/將的移动逻辑
        moves = []
        x, y = self.position
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        palace_x_range = (3, 5)
        if self.color == '红':
            palace_y_range = (0, 2)
        else:
            palace_y_range = (7, 9)
        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if palace_x_range[0] <= new_x <= palace_x_range[1] and palace_y_range[0] <= new_y <= palace_y_range[1]:
                target_piece = board.get_piece_at((new_x, new_y))
                if target_piece is None or target_piece.color != self.color:
                    moves.append((new_x, new_y))
        return moves

    def _get_cannon_moves(self, board):
        # 实现砲/炮的移动逻辑
        moves = []
        x, y = self.position
        # 横向移动
        for dx in [-1, 1]:
            new_x = x + dx
            found_screen = False
            while 0 <= new_x < 9:
                target_piece = board.get_piece_at((new_x, y))
                if not found_screen:
                    if target_piece is None:
                        moves.append((new_x, y))
                    else:
                        found_screen = True
                else:
                    if target_piece is not None:
                        if target_piece.color != self.color:
                            moves.append((new_x, y))
                        break
                new_x += dx
        # 纵向移动
        for dy in [-1, 1]:
            new_y = y + dy
            found_screen = False
            while 0 <= new_y < 10:
                target_piece = board.get_piece_at((x, new_y))
                if not found_screen:
                    if target_piece is None:
                        moves.append((x, new_y))
                    else:
                        found_screen = True
                else:
                    if target_piece is not None:
                        if target_piece.color != self.color:
                            moves.append((x, new_y))
                        break
                new_y += dy
        return moves

    def _get_soldier_moves(self, board):
        # 实现兵/卒的移动逻辑
        moves = []
        x, y = self.position
        has_crossed_river = (self.color == '红' and y >= 5) or (self.color == '黑' and y < 5)
        # 定义移动偏移量
        if self.color == '红':
            if has_crossed_river:
                offsets = [(0, 1), (1, 0), (-1, 0)]
            else:
                offsets = [(0, 1)]
        else:
            if has_crossed_river:
                offsets = [(0, -1), (1, 0), (-1, 0)]
            else:
                offsets = [(0, -1)]
        for dx, dy in offsets:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 9 and 0 <= new_y < 10:
                target_piece = board.get_piece_at((new_x, new_y))
                if target_piece is None or target_piece.color != self.color:
                    moves.append((new_x, new_y))
        return moves

    def is_only_piece_between_generals(self, board):
        # 查找双方的将/帅
        red_general = None
        black_general = None
        
        for piece in board.pieces:
            if piece.name == '帥' and piece.color == '红':
                red_general = piece
            elif piece.name == '將' and piece.color == '黑':
                black_general = piece
        
        # 如果没有找到双方的将/帅，返回False
        if not red_general or not black_general:
            return False
            
        # 检查是否在同一列
        red_x, red_y = red_general.position
        black_x, black_y = black_general.position
        
        if red_x != black_x:
            return False
            
        # 检查当前棋子是否在两将之间
        x, y = self.position
        if not (x == red_x and min(red_y, black_y) < y < max(red_y, black_y)):
            return False

        # 检查两将之间是否有其他棋子
        for piece in board.pieces:
            x, y = piece.position
            if x == red_x and min(red_y, black_y) < y < max(red_y, black_y):
                if piece != self:  # 发现其他棋子
                    return False
                    
        return True