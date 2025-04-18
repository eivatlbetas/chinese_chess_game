from turtle import Turtle
import pygame
from board import Board
from view import BoardView

# 定义网格大小和边距
x_0 = 60
y_0 = 60
grid_size = 60


# 初始化 Pygame
pygame.init()

# 设置游戏窗口
screen_width = grid_size * 8 + 2 * x_0
screen_height = grid_size * 9 + 2 * y_0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('中国象棋')

# 初始化棋盘
if __name__ == '__main__':
    board = Board()
    view = BoardView(board)
    running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3: # 右键点击，取消选择
                board.selected_piece = None
                print('取消选择。')
                continue

            center = view.find_nearby_center(event.pos)
            if center == view.INVALID_POS:
                print('点击位置无效，请在网格附近点击。')
                continue
            
            board.click_position(center)

        view.display_board(screen)
        if board.game_over is True:
            view.display_game_over(screen)

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

