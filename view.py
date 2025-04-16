import pygame

class ChessView:
    def __init__(self, board, x_0 = 60, y_0 = 60, grid_size = 60, piece_size = 25):
        self.board = board # 设置棋盘对象
        self.x_0 = x_0 # 设置边距
        self.y_0 = y_0 # 设置边距
        self.grid_size = grid_size # 设置网格大小
        self.piece_size = piece_size # 设置棋子大小

    # 定义颜色常量
    RED_COLOR = (255, 0, 0)
    BLACK_COLOR = (0, 0, 0)
    BLUE_COLOR = (0, 0, 255)
    WHITE_COLOR = (255, 255, 255)
    GRAY_COLOR = (128, 128, 128)

    def display_board(self, screen):
        # 填充背景色
        screen.fill(self.WHITE_COLOR)

        # 绘制棋盘
        self._draw_board(screen)

        # 绘制棋子
        self._draw_pieces(screen)

        # 显示可能的移动位置
        self._draw_possible_moves(screen)

    def _draw_board(self, screen):
        # 绘制棋盘网格
        for i in range(10):  # 第0-9行
            self._draw_line(screen, (0, i), (8, i))
        for i in [0, 8]:  # 第0列、第8列
            self._draw_line(screen, (i, 0), (i, 9))
        for i in range(1, 8):  # 第1-8列
            self._draw_line(screen, (i, 0), (i, 4))
            self._draw_line(screen, (i, 5), (i, 9))
        
        # 绘制米字格
        self._draw_line(screen, (3, 0), (5, 2)) 
        self._draw_line(screen, (5, 0), (3, 2))  
        self._draw_line(screen, (3, 7), (5, 9))
        self._draw_line(screen, (5, 7), (3, 9)) 

        # 绘制炮的定位
        for y in [2, 7]:
            for x in [1, 7]:
                self._draw_jing_shape(screen, self.x_0 + (8 - x) * self.grid_size, self.y_0 + (9 - y) * self.grid_size, 2, 8)

        # 绘制兵的定位
        for y in [3, 6]:
            for x in range(0, 9, 2):
                self._draw_jing_shape(screen, self.x_0 + (8 - x) * self.grid_size, self.y_0 + (9 - y) * self.grid_size, 2, 8)

        # 绘制楚河汉界
        self._draw_river_boundary(screen, self.GRAY_COLOR, 'simhei', 48)

    def _draw_line(self, screen, from_position, to_position):
        # 绘制线段
        pygame.draw.line(screen, self.BLACK_COLOR, 
                        (self.x_0 + from_position[0] * self.grid_size, self.y_0 + from_position[1] * self.grid_size), 
                        (self.x_0 + to_position[0] * self.grid_size, self.y_0 + to_position[1] * self.grid_size))

    def _draw_jing_shape(self, screen, center_x, center_y, near = 2, far = 8):
        # 绘制井字形
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - near, center_y - near), (center_x - near, center_y - far ))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - near, center_y - near), (center_x - far , center_y - near))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x + near, center_y - near), (center_x + near, center_y - far ))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x + near, center_y - near), (center_x + far , center_y - near))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x + near, center_y + near), (center_x + near, center_y + far ))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x + near, center_y + near), (center_x + far , center_y + near))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - near, center_y + near), (center_x - near, center_y + far ))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - near, center_y + near), (center_x - far , center_y + near))

    def _draw_river_boundary(self, screen, color=(128, 128, 128), font_name='simhei', font_size=48):
        # 绘制楚河汉界
        font = pygame.font.SysFont(font_name, font_size)
        center_x = 9 * self.grid_size // 2
        center_y = 10 * self.grid_size // 2
        
        screen.blit(font.render('楚', True, color), (center_x - 3 * self.grid_size, center_y))
        screen.blit(font.render('河', True, color), (center_x - 2 * self.grid_size, center_y))
        screen.blit(font.render('汉', True, color), (center_x + 2 * self.grid_size, center_y))
        screen.blit(font.render('界', True, color), (center_x + 3 * self.grid_size, center_y))

    def _draw_pieces(self, screen):
        # 绘制棋子
        for piece in self.board.pieces:
            color = self.RED_COLOR if piece.color =='red' else self.BLACK_COLOR
            center = self._pos_convert(piece.position)
            # 绘制棋子的轮廓
            pygame.draw.circle(screen, color, center, self.piece_size, 2)
            # 绘制棋子的内部
            pygame.draw.circle(screen, self.WHITE_COLOR, center, self.piece_size - 2)
            # 绘制棋子的名称
            font = pygame.font.SysFont('simhei', 36)
            text = font.render(piece.name, True, color)
            text_rect = text.get_rect(center=center)
            screen.blit(text, text_rect)

    def _draw_possible_moves(self, screen):
        # 显示棋子可能的移动位置
        if hasattr(self.board, 'selected_piece') and self.board.selected_piece:
            possible_moves = self.board.selected_piece.get_possible_moves(self.board)
            for move in possible_moves:
                pygame.draw.circle(screen, self.BLUE_COLOR, self._pos_convert(move), 8)

    def _pos_convert(self, position):
        # 棋盘坐标转换为屏幕坐标，棋盘右下角坐标为（0,0），左上角坐标为（8,9），屏幕左上角坐标为（x_0, y_0）
        return (self.x_0 + (8 - position[0]) * self.grid_size, self.y_0 + (9 - position[1]) * self.grid_size)

    # 定义无效位置常量
    INVALID_POS = (-1, -1)

    def find_nearby_center(self, mouse):
        # 遍历所有棋盘位置，计算与点击位置的距离，若小于棋子半径则返回对应坐标
        for x in range(9):
            for y in range(10):
                board_pos = (x, y)
                center = self._pos_convert(board_pos)
                distance = ((mouse[0] - center[0]) ** 2 + (mouse[1] - center[1]) ** 2) ** 0.5
                if distance <= self.piece_size:
                    return board_pos
        return self.INVALID_POS
