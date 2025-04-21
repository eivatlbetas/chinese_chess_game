class Player:
    def __init__(self, color):
        '''初始化玩家
        Args:
            color: 玩家颜色('红'或'黑')
        '''
        self.color = color
        self.time_left = self.DEF_TIME_TOTAL
        self.time_per_turn = self.DEF_TIME_PER_TURN
        self.last_update = None  # 最后更新时间戳
        self.is_active = False  # 是否当前回合

    DEF_TIME_TOTAL = 900  # 默认总时间（秒）
    DEF_TIME_PER_TURN = 60  # 默认回合时间（秒）

    def __str__(self):
        '''返回玩家字符串表示'''
        return f"{self.color}方"

    def start_turn(self):
        '''开始玩家回合'''
        self.is_active = True
        self.time_per_turn = min(self.DEF_TIME_PER_TURN, self.time_left)
        self.last_update = time.time()

    def end_turn(self):
        '''结束玩家回合''' 
        if self.is_active:
            self.update_time()  # 确保更新剩余时间
            self.is_active = False
            self.last_update = None
        
    def update_time(self):
        '''更新剩余时间
        Returns:
            bool: 时间是否用完
        '''
        if self.is_active and self.last_update:
            now = time.time()
            elapsed = now - self.last_update
            self.time_left = max(0, self.time_left - elapsed)  # 防止负时间
            self.last_update = now
            return self.time_left > 0
        return True

    def get_time_str(self):
        '''获取格式化时间显示
        Returns:
            str: 格式为"MM:SS"的时间字符串
        '''
        mins = int(self.time_left) // 60
        secs = int(self.time_left) % 60
        return f"{mins:02d}:{secs:02d}"
