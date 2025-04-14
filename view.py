import pygame

class ChessView:
    def __init__(self, board):
        self.board = board

    def display_board(self, screen, margin_x, margin_y):
        # 填充背景色
        screen.fill((255, 255, 255))

        # 绘制棋盘网格
        for i in range(10):
            # 绘制横线
            pygame.draw.line(screen, (0, 0, 0), (margin_x, margin_y + i * 60), (margin_x + 60 * 8, margin_y + i * 60))
        for i in range(9):
            # 绘制竖线
            pygame.draw.line(screen, (0, 0, 0), (margin_x + i * 60, margin_y), (margin_x + i * 60, margin_y + 540))

        # 绘制楚河汉界
        font = pygame.font.SysFont('simhei', 32)
        text1 = font.render('楚', True, (128, 128, 128))
        text2 = font.render('河', True, (128, 128, 128))
        text3 = font.render('汉', True, (128, 128, 128))
        text4 = font.render('界', True, (128, 128, 128))
        screen.blit(text1, (margin_x + 60, margin_y + 250))
        screen.blit(text2, (margin_x + 120, margin_y + 250))
        screen.blit(text3, (margin_x + 320, margin_y + 250))
        screen.blit(text4, (margin_x + 380, margin_y + 250))

        # 绘制棋子
        for piece in self.board.pieces:
            x, y = piece.position
            center_x = margin_x + x * 60
            center_y = margin_y + y * 60
            radius = 25
            # 绘制棋子的轮廓
            pygame.draw.circle(screen, (0, 0, 0) if piece.color == 'red' else (255, 0, 0), (center_x, center_y), radius, 2)
            # 绘制棋子的内部
            pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), radius // 3)
            # 绘制棋子的名称
            font = pygame.font.SysFont('simhei', 36)
            text = font.render(piece.name, True, (0, 0, 0) if piece.color == 'red' else (255, 0, 0))
            text_rect = text.get_rect(center=(center_x, center_y))
            screen.blit(text, text_rect)

    def display_possible_moves(self, moves):
        # 显示棋子可能的移动位置
        pass

    def display_message(self, message):
        # 显示提示信息
        print(message)