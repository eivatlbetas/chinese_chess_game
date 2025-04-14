import pygame
from board import Board
from view import ChessView

# 初始化 Pygame
pygame.init()

# 定义网格大小常量
grid_size = 60

# 设置边距
x_0 = 60
y_0 = 60

# 设置游戏窗口
screen_width = grid_size * 8 + 2 * x_0
screen_height = grid_size * 9 + 2 * y_0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('中国象棋')

# 初始化棋盘
if __name__ == '__main__':
    board = Board()
    view = ChessView(board)
    # 初始化棋子

# 游戏主循环
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # 计算点击的棋盘格子坐标
            grid_x = x // grid_size
            grid_y = y // grid_size
            # 处理点击事件
            selected_piece = board.get_piece_at((grid_x, grid_y))
            if selected_piece:
                possible_moves = selected_piece.get_possible_moves(board)
                # 这里可以添加显示可能移动位置的代码
            pass

    view.display_board(screen, x_0, y_0, grid_size)

    # 更新显示
    pygame.display.flip() 

# 退出 Pygame
pygame.quit()