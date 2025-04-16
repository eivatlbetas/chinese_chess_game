import pygame
from board import Board
from view import ChessView

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
    view = ChessView(board)
    running = True
    game_over = False

while running and not game_over:
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

            if board.selected_piece is not None:  # 已有选中棋子，尝试移动
                print(f'尝试将 {board.selected_piece.name} 移动到 ({center[0]}, {center[1]})。')
                if board.move_piece(board.selected_piece, center):
                    board.selected_piece = None  # 移动成功后取消选择
                    board.current_player = '黑' if board.current_player == '红' else '红'
                    print(f'移动成功，当前轮到 {board.current_player} 方。')
                else:
                    print('移动失败，请重新移动。')
            else:  # 没有选中棋子，尝试选择
                piece = board.get_piece_at(center)
                if piece is not None:
                    if piece.color == board.current_player:
                        board.selected_piece = piece
                        print(f'选中 {piece.color} {piece.name} {piece.position} 棋子，请移动。')
                    else:
                        print('这不是你的棋子，请选择你的棋子。')
                else:
                    print('没有选中棋子，请重新选择。')

            # 检查游戏是否结束
            if board.is_game_over() is not None:
                game_over = True
                print(f'游戏结束，{board.is_game_over()} 方获胜！')

    view.display_board(screen)

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

