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
    running = True
    game_over = False
    current_player = 'red'  # 初始化当前玩家为红方
    selected_piece = None  # 初始化选中的棋子
    selected_piece_pos = None  # 初始化选中的棋子位置

# 模糊网格转换
INVALID_POS = (-1, -1)
def convert_mouse_to_fuzzy_grid(x, y, fuzzy_range = grid_size / 4):
    for piece in board.pieces:
        piece_x = x_0 + piece.position[0] * grid_size
        piece_y = y_0 + piece.position[1] * grid_size
        distance = ((x - piece_x) ** 2 + (y - piece_y) ** 2) ** 0.5
        # print("convert_mouse_to_fuzzy_grid",x, y, piece_x, piece_y, distance)
        if distance <= fuzzy_range:
            return piece.position
    return INVALID_POS

while running and not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3: # 右键点击，取消选择
                selected_piece = None
                selected_piece_pos = None
                print('取消选择。')
                continue

            x, y = event.pos
            grid_x, grid_y = convert_mouse_to_fuzzy_grid(x, y)
            if (grid_x, grid_y) == INVALID_POS:
                print('点击位置无效，请在网格附近点击。')
                continue

            if selected_piece_pos is not None:  # 已有选中棋子，尝试移动
                print(f'尝试将 {selected_piece.name} 移动到 ({grid_x}, {grid_y})。')
                if board.move_piece(selected_piece_pos, (grid_x, grid_y), current_player):
                    selected_piece = None  # 移动成功后取消选择
                    selected_piece_pos = None
                    current_player = 'black' if current_player == 'red' else 'red'
                    print(f'移动成功，当前轮到 {current_player} 方。')
                else:
                    print('移动失败，请重新选择。')
            else:  # 没有选中棋子，尝试选择
                piece = board.get_piece_at((grid_x, grid_y))
                if piece is not None and piece.color == current_player:
                    print(f'选中 {piece.color} {piece.name} {piece.position} 棋子。')
                    selected_piece = piece
                    selected_piece_pos = (grid_x, grid_y)

    view.display_board(screen, x_0, y_0, grid_size)

    # 更新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()

