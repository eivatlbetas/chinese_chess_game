import pygame
import time
from board import Board
from view import BoardView
from view import PlayerView

# 定义网格大小和边距
x_0 = 60
y_0 = 60
grid_size = 60
player_view_width = 200

# 初始化 Pygame
pygame.init()

# 设置游戏窗口
screen_width = grid_size * 8 + 2 * x_0 + player_view_width
screen_height = grid_size * 9 + 2 * y_0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('中国象棋')

# 初始化棋盘
if __name__ == '__main__':
    board = Board()
    board_view = BoardView(board)
    player_view = PlayerView(screen_width - player_view_width, 0, player_view_width, screen_height, board)
    running = True
    last_time_update = time.time() # 初始化计时器
    clock = pygame.time.Clock()  # 创建时钟对象控制帧率

while running:
    current_time = time.time()
    # 更新时间显示（每秒更新一次）
    if current_time - last_time_update >= 1.0:
        if board.player_turn == board.red_player:  # 只更新当前玩家的时间
            board.red_player.update_time()
        else:
            board.black_player.update_time()
        last_time_update = current_time
    
    clock.tick(120)  # 限制帧率为120FPS
    
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
            if event.button == 3: # 右键点击
                board.click_right()
            elif event.button == 1: # 左键点击
                center = board_view.find_nearby_center(event.pos)
                if center == board_view.INVALID_POS:
                    print('点击位置无效，请在网格附近点击。')
                    continue
                board.click_position(center)

    # 显示棋盘和棋子
    board_view.display_board(screen)
    # 显示玩家时间
    player_view.display_player_time(screen, board)
    # 显示游戏结束信息
    if board.game_over is True:
        board_view.display_game_over(screen)
    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

