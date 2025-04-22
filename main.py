import pygame
import time
from board import Board
from view import BoardView
from view import PlayerView

# 定义棋盘视图参数
board_view_x_0 = 0
board_view_y_0 = 0
board_view_grid_size = 60
board_view_piece_size = 25
board_view_width = 10 * board_view_grid_size
board_view_height = 11 * board_view_grid_size
# 定义玩家视图参数
player_view_x_0 = 0
player_view_y_0 = board_view_height
player_view_width = board_view_width  # 玩家视图宽度
player_view_height = 120  # 玩家视图高度
# 定义屏幕大小
screen_width = board_view_width
screen_height = board_view_height + player_view_height
screen_color = (255, 255, 255)  # 白色背景
# 初始化 Pygame
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('中国象棋')

# 初始化棋盘
if __name__ == '__main__':
    board = Board()
    board_view = BoardView(board, board_view_x_0, board_view_y_0, board_view_grid_size, board_view_piece_size)
    player_view = PlayerView(board, player_view_x_0, player_view_y_0, player_view_width, player_view_height)
    running = True
    last_time_update = time.time() # 初始化计时器

while running:
    current_time = time.time()
    # 更新时间显示（每秒更新一次）
    if current_time - last_time_update >= 1.0:
        if board.player_turn == board.red_player:  # 只更新当前玩家的时间
            board.red_player.update_time()
        else:
            board.black_player.update_time()
        last_time_update = current_time
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q: # ESC键或Q键退出
                running = False
            if event.key == pygame.K_BACKSPACE: # Backspace键悔棋
                board.click_key_Backspace()
            elif event.key == pygame.K_r: # R键重新开始
                board = Board()
                board_view = BoardView(board)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_RIGHT: # 右键点击
                board.click_right()
            elif event.button == pygame.BUTTON_LEFT: # 左键点击
                center = board_view.find_nearby_center(event.pos)
                if center == board_view.INVALID_POS:
                    print('点击位置无效，请在网格附近点击。')
                    continue
                board.click_position(center)

    # 填充白色背景
    screen.fill(screen_color)
    # 显示棋盘和棋子
    board_view.display_board(screen)
    
    if board.game_over is not True:
        # 显示玩家时间
        player_view.display_player_time(screen, board)
    else:
        # 显示游戏结果
        player_view.display_player_winner(screen, board)
    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

