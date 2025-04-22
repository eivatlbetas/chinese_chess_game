import pygame

class BoardView:
    def __init__(self, board, x_0, y_0, grid_size, piece_size):
        '''初始化棋盘视图
        Args:
            board: 棋盘对象
            x_0: 水平边距
            y_0: 垂直边距 
            grid_size: 网格大小
            piece_size: 棋子大小
        '''
        self.board = board # 设置棋盘对象
        self.x_0 = x_0 # 设置水平边距
        self.y_0 = y_0 # 设置垂直边距
        self.grid_size = grid_size # 设置网格大小
        self.piece_size = piece_size # 设置棋子大小

    # 定义颜色常量
    RED_COLOR = (255, 0, 0)
    BLACK_COLOR = (0, 0, 0)
    GREEN_COLOR = (0, 255, 0)
    WHITE_COLOR = (255, 255, 255)

    # 木质棋盘底色
    BOARD_COLOR = (210, 180, 140)  # 浅棕色木质
    GRID_COLOR = (139, 69, 19)     # 深棕色线条
    # 红方棋子
    RED_PIECE_COLOR = (178, 34, 34)   # 深红色
    RED_TEXT_COLOR = (255, 255, 255)  # 白色文字
    # 黑方棋子  
    BLACK_PIECE_COLOR = (47, 79, 79)  # 深石板灰
    BLACK_TEXT_COLOR = (255, 215, 0)  # 金色文字

    # 提示信息
    LAST_MOVE_COLOR = WHITE_COLOR  # 最后一步移动的颜色
    SELECT_COLOR = GREEN_COLOR  # 选中棋子的颜色
    # 楚河汉界
    RIVER_TEXT_COLOR = GRID_COLOR

    def _pos_convert(self, position):
        '''棋盘坐标转换为屏幕坐标
        Args:
            position: 棋盘坐标(x,y)
        Returns:
            屏幕坐标(x,y)
        '''
        # 棋盘右下角坐标为（-1, -1），左上角坐标为（9, 10）
        # 棋子右下角坐标为（0, 0），左上角坐标为（8, 9）
        # 屏幕左上角坐标为（0, 0），右下角坐标为（10 * grid_size, 11 * grid_size）
        return (self.x_0 + (9 - position[0]) * self.grid_size, self.y_0 + (10 - position[1]) * self.grid_size)

    def display_board(self, screen):
        '''显示整个棋盘
        Args:
            screen: pygame显示器
        '''
        # 绘制棋盘
        self._draw_board(screen)

        # 绘制棋子
        self._draw_pieces(screen)

        # 绘制最后一步移动
        self._draw_last_move(screen)

        # 显示可能的移动位置
        self._draw_possible_moves(screen)

    def _draw_board(self, screen):
        '''绘制棋盘背景和网格
        Args:
            screen: pygame显示器
        '''
        # 绘制棋盘外框
        self._draw_board_rect(screen)

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
                center = self._pos_convert((x, y))
                self._draw_jing_shape(screen, center, 2, 8, '左右')

        # 绘制兵的定位
        for y in [3, 6]:
            for x in range(0, 9, 2):
                if x == 0:
                    flag = '右'
                elif x == 8:
                    flag = '左'
                else:
                    flag = '左右'
                center = self._pos_convert((x, y))
                self._draw_jing_shape(screen, center, 2, 8, flag)

        # 绘制楚河汉界
        self._draw_river_boundary(screen)

    def _draw_board_rect(self, screen):
        '''绘制棋盘外框
        Args:
            screen: pygame显示器
        '''
        # 绘制棋盘整体
        pygame.draw.rect(screen, self.BOARD_COLOR, (self.x_0, self.y_0, 10 * self.grid_size, 11 * self.grid_size))

        # 绘制棋盘外框
        pygame.draw.rect(screen, self.GRID_COLOR, (self.x_0 + self.grid_size - 6, self.y_0 + self.grid_size - 6, 
                                                  8 * self.grid_size + 13, 9 * self.grid_size + 13), 2)

    def _draw_line(self, screen, from_position, to_position):
        '''绘制线段
        Args:
            screen: pygame显示器
            from_position: 起点坐标
            to_position: 终点坐标
        '''
        pygame.draw.line(screen, self.GRID_COLOR, self._pos_convert(from_position), self._pos_convert(to_position))

    def _draw_jing_shape(self, screen, center, near = 2, far = 8, flag = '左右'):
        '''绘制井字形标记
        Args:
            screen: pygame显示器
            center: 中心点坐标
            near: 近端距离
            far: 远端距离
            flag: 标记方向('左'/'右'/'左右')
        '''
        color = self.GRID_COLOR

        if flag != '左':
            pygame.draw.line(screen, color, (center[0] - near, center[1] - near), (center[0] - near, center[1] - far ))
            pygame.draw.line(screen, color, (center[0] - near, center[1] - near), (center[0] - far , center[1] - near))
            pygame.draw.line(screen, color, (center[0] - near, center[1] + near), (center[0] - near, center[1] + far ))
            pygame.draw.line(screen, color, (center[0] - near, center[1] + near), (center[0] - far , center[1] + near))
        if flag != '右':
            pygame.draw.line(screen, color, (center[0] + near, center[1] - near), (center[0] + near, center[1] - far ))
            pygame.draw.line(screen, color, (center[0] + near, center[1] - near), (center[0] + far , center[1] - near))
            pygame.draw.line(screen, color, (center[0] + near, center[1] + near), (center[0] + near, center[1] + far ))
            pygame.draw.line(screen, color, (center[0] + near, center[1] + near), (center[0] + far , center[1] + near))

    def _draw_river_boundary(self, screen):
        '''绘制楚河汉界文字
        Args:
            screen: pygame显示器
        '''
        font_size = 40
        font = pygame.font.SysFont('simhei', font_size)
        center_x = self.x_0 + 5 * self.grid_size - font_size // 2
        center_y = self.y_0 + 5.5 * self.grid_size - font_size // 2
        color = self.RIVER_TEXT_COLOR
        
        screen.blit(font.render('楚', True, color), (center_x - 2.5 * self.grid_size, center_y))
        screen.blit(font.render('河', True, color), (center_x - 1.5 * self.grid_size, center_y))
        screen.blit(font.render('汉', True, color), (center_x + 1.5 * self.grid_size, center_y))
        screen.blit(font.render('界', True, color), (center_x + 2.5 * self.grid_size, center_y))

    def _draw_pieces(self, screen):
        '''绘制所有棋子
        Args:
            screen: pygame显示器
        '''
        for piece in self.board.pieces:
            center = self._pos_convert(piece.position)
            piece_color = self.RED_PIECE_COLOR if piece.color == '红' else self.BLACK_PIECE_COLOR
            text_color = self.RED_TEXT_COLOR if piece.color == '红' else self.BLACK_TEXT_COLOR

            # 绘制棋子的轮廓
            pygame.draw.circle(screen, piece_color, center, self.piece_size, 2)
            # 绘制棋子的内部
            pygame.draw.circle(screen, piece_color, center, self.piece_size - 2)

            # 绘制棋子的名称
            font = pygame.font.SysFont('simhei', 36)
            text = font.render(piece.name, True, text_color)
            text_rect = text.get_rect(center=center)
            screen.blit(text, text_rect)

    def _draw_possible_moves(self, screen):
        '''显示选中棋子的可移动位置
        Args:
            screen: pygame显示器
        '''
        if self.board.selected_piece is not None:
            # 绘制选中棋子的轮廓
            center = self._pos_convert(self.board.selected_piece.position)
            pygame.draw.circle(screen, self.SELECT_COLOR, center, self.piece_size + 3, 2)
            # 绘制选中棋子的可移动位置
            if hasattr(self.board, 'selected_piece') and self.board.selected_piece:
                possible_moves = self.board.selected_piece.get_possible_moves(self.board)
                for move in possible_moves:
                    pygame.draw.circle(screen, self.SELECT_COLOR, self._pos_convert(move), 6)

    def _draw_last_move(self, screen):
        '''绘制最后一步移动
        Args:
            screen: pygame显示器
        '''
        last_move, captured_piece = self.board.recorder.get_last_move()
        if last_move:
            # 绘制最后一步移动前位置
            pygame.draw.circle(screen, self.LAST_MOVE_COLOR, self._pos_convert(last_move['from']), 4, 4)
            pygame.draw.circle(screen, self.LAST_MOVE_COLOR, self._pos_convert(last_move['from']), 10, 2)
            # 绘制最后一步移动后位置
            pygame.draw.circle(screen, self.LAST_MOVE_COLOR, self._pos_convert(last_move['to']), self.piece_size + 3, 2)

    # 定义无效位置常量
    INVALID_POS = (-1, -1)

    def find_nearby_center(self, mouse):
        '''查找最近的棋盘位置
        Args:
            mouse: 鼠标坐标(x,y)
        Returns:
            最近的棋盘坐标或INVALID_POS
        '''
        # 遍历所有棋盘位置，计算与点击位置的距离，若小于棋子半径则返回对应坐标
        for x in range(9):
            for y in range(10):
                center = self._pos_convert((x, y))
                distance = ((mouse[0] - center[0]) ** 2 + (mouse[1] - center[1]) ** 2) ** 0.5
                if distance <= self.piece_size:
                    return (x, y)
        return self.INVALID_POS

class PlayerView:
    def __init__(self, board, x_0, y_0, width, height):
        '''初始化玩家视图
        Args:
            board: 棋盘对象
            x_0: 水平边距
            y_0: 垂直边距
            width: 宽度
            height: 高度
        '''
        self.x_0 = x_0 # 设置边距
        self.y_0 = y_0 # 设置边距
        self.width = width # 设置宽度
        self.height = height # 设置高度
        self.red_player = board.red_player # 设置红方玩家对象
        self.black_player = board.black_player # 设置黑方玩家对象

        # 定义颜色常量
        self.RED_COLOR = (255, 0, 0)
        self.BLACK_COLOR = (0, 0, 0)

    def display_player_time(self, screen, board):
        '''显示双方剩余时间
        Args:
            screen: pygame显示器
            board: 棋盘对象
        '''
        font = pygame.font.SysFont('SimHei', 20)
        red_player_name = font.render(f'{board.red_player.name}', True, self.RED_COLOR) # 红色字体，白色背景
        red_left_time = font.render(f'本局剩余: {board.red_player.get_time_left_str()}', True, self.RED_COLOR) # 红色字体，白色背景
        red_turn_time = font.render(f'本轮剩余: {board.red_player.get_time_per_turn_str()}', True, self.RED_COLOR) # 红色字体，白色背景
        black_player_name = font.render(f'{board.black_player.name}', True, self.BLACK_COLOR) # 黑色字体，白色背景
        black_left_time = font.render(f'本局剩余: {board.black_player.get_time_left_str()}', True, self.BLACK_COLOR) # 黑色字体，白色背景
        black_turn_time = font.render(f'本轮剩余: {board.black_player.get_time_per_turn_str()}', True, self.BLACK_COLOR) # 黑色字体，白色背景

        screen.blit(black_player_name, (self.x_0 + 30, self.y_0 + 20))
        screen.blit(black_left_time, (self.x_0 + 30, self.y_0 + 50)) 
        screen.blit(black_turn_time, (self.x_0 + 30, self.y_0 + 80))
        screen.blit(red_player_name, (self.x_0 + 30 + self.width // 2, self.y_0 + 20))
        screen.blit(red_left_time, (self.x_0 + 30 + self.width // 2, self.y_0 + 50)) 
        screen.blit(red_turn_time, (self.x_0 + 30 + self.width // 2, self.y_0 + 80))

    def display_game_over(self, screen, board):
        '''显示游戏结束信息
        Args:
            screen: pygame显示器
        '''
        font = pygame.font.SysFont('simhei', 72)
        if board.player_turn.color == '红':
            text = font.render('红方获胜！', True, self.RED_COLOR)
        elif board.player_turn.color == '黑':
            text = font.render('黑方获胜！', True, self.BLACK_COLOR)
        else:
            text = font.render('双方平局！', True, self.BLUE_COLOR)
        text_rect = text.get_rect(center=(self.x_0 + self.width // 2, self.y_0 + self.height // 2))
        screen.blit(text, text_rect)
