import pygame

class ChessView:
    def __init__(self, board):
        self.board = board

    # 定义颜色常量
    RED_COLOR = (255, 0, 0)
    BLACK_COLOR = (0, 0, 0)
    BLUE_COLOR = (0, 0, 255)
    WHITE_COLOR = (255, 255, 255)
    GRAY_COLOR = (128, 128, 128)

    def display_board(self, screen, x_0, y_0, grid_size):
        # 填充背景色
        screen.fill(self.WHITE_COLOR)

        # 绘制棋盘
        self._draw_board(screen, x_0, y_0, grid_size)

        # 绘制棋子
        self._draw_pieces(screen, x_0, y_0, grid_size)

    def _draw_board(self, screen, x_0, y_0, grid_size):
        # 绘制棋盘网格
        self._draw_tian_shape(screen, x_0, y_0, grid_size)

        # 绘制米字格
        self._draw_mi_shape(screen, x_0 + 4 * grid_size, y_0 + 1 * grid_size, grid_size)
        self._draw_mi_shape(screen, x_0 + 4 * grid_size, y_0 + 8 * grid_size, grid_size) 

        # 绘制炮的定位
        for y in [2, 7]:
            for x in [1, 7]:
                self._draw_jing_shape(screen, x_0 + x * grid_size, y_0 + y * grid_size, 2, 8)

        # 绘制兵的定位
        for y in [3, 6]:
            for x in range(0, 9, 2):
                self._draw_jing_shape(screen, x_0 + x * grid_size, y_0 + y * grid_size, 2, 8)

        # 绘制楚河汉界
        self._draw_river_boundary(screen, grid_size, self.GRAY_COLOR, 'simhei', 48)

    def _draw_tian_shape(self, screen, x_0, y_0, grid_size):
        # 绘制田字形
        # 绘制横线
        for i in range(10):
            pygame.draw.line(screen, self.BLACK_COLOR, (x_0, y_0 + i * grid_size), (x_0 + grid_size * 8, y_0 + i * grid_size))

        # 绘制竖线
        for i in range(9):
            pygame.draw.line(screen, self.BLACK_COLOR, (x_0 + i * grid_size, y_0 + 0 * grid_size), (x_0 + i * grid_size, y_0 + 4 * grid_size))
            pygame.draw.line(screen, self.BLACK_COLOR, (x_0 + i * grid_size, y_0 + 5 * grid_size), (x_0 + i * grid_size, y_0 + 9 * grid_size))
        pygame.draw.line(screen, self.BLACK_COLOR, (x_0 + 0 * grid_size, y_0 + 4 * grid_size), (x_0 + 0 * grid_size, y_0 + 5 * grid_size))
        pygame.draw.line(screen, self.BLACK_COLOR, (x_0 + 8 * grid_size, y_0 + 4 * grid_size), (x_0 + 8 * grid_size, y_0 + 5 * grid_size))

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

    def _draw_mi_shape(self, screen, center_x, center_y, grid_size):
        # 绘制米字形
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - grid_size, center_y - grid_size), (center_x + grid_size, center_y + grid_size))
        pygame.draw.line(screen, self.BLACK_COLOR, (center_x - grid_size, center_y + grid_size), (center_x + grid_size, center_y - grid_size))

    def _draw_river_boundary(self, screen, grid_size, color=(128, 128, 128), font_name='simhei', font_size=48):
        # 绘制楚河汉界
        font = pygame.font.SysFont(font_name, font_size)
        center_x = 9 * grid_size // 2
        center_y = 10 * grid_size // 2
        
        screen.blit(font.render('楚', True, color), (center_x - 3 * grid_size, center_y))
        screen.blit(font.render('河', True, color), (center_x - 2 * grid_size, center_y))
        screen.blit(font.render('汉', True, color), (center_x + 2 * grid_size, center_y))
        screen.blit(font.render('界', True, color), (center_x + 3 * grid_size, center_y))

    def _draw_pieces(self, screen, x_0, y_0, grid_size):
        for piece in self.board.pieces:
            x, y = piece.position
            center_x = x_0 + x * grid_size
            center_y = y_0 + y * grid_size
            radius = 25
            # 绘制棋子的轮廓
            pygame.draw.circle(screen, self.BLACK_COLOR if piece.color == 'red' else self.RED_COLOR, (center_x, center_y), radius, 2)
            # 绘制棋子的内部
            pygame.draw.circle(screen, self.WHITE_COLOR, (center_x, center_y), radius // 3)
            # 绘制棋子的名称
            font = pygame.font.SysFont('simhei', 36)
            text = font.render(piece.name, True, self.BLACK_COLOR if piece.color == 'red' else self.RED_COLOR)
            text_rect = text.get_rect(center=(center_x, center_y))
            screen.blit(text, text_rect)

    def display_possible_moves(self, moves):
        # 显示棋子可能的移动位置
        pass

    def display_message(self, message):
        # 显示提示信息
        print(message)
