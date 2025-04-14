import pygame
from board import Board
from view import ChessView

# 初始化 Pygame
pygame.init()

# 设置边距
margin_x = 60
margin_y = 60

# 设置游戏窗口
screen_width = 60 * 8 + 2 * margin_x
screen_height = 60 * 9 + 2 * margin_y
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
            grid_x = x // 60
            grid_y = y // 60
            # 处理点击事件
            selected_piece = board.get_piece_at((grid_x, grid_y))
            if selected_piece:
                possible_moves = selected_piece.get_possible_moves(board)
                # 这里可以添加显示可能移动位置的代码
            pass

    view.display_board(screen, margin_x, margin_y)

    # 更新显示
    pygame.display.flip() 

# 退出 Pygame
pygame.quit()