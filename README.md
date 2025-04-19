# 中国象棋游戏

一个基于Python和Pygame实现的中国象棋游戏。

## 功能特性

- 简洁的图形界面
- 完整的中国象棋规则实现
- 支持红黑双方轮流走棋
- 实现所有棋子的标准走法规则
- 合法走法高亮提示
- 将军提示功能
- 游戏输赢判定

## 计划开发功能

- [ ] 悔棋功能
- [ ] 棋谱记录与回放功能
- [ ] 限定时间模式
- [ ] 保存/加载游戏进度功能
- [ ] 人机对战功能（支持难度选择）
- [ ] 网络对战模块（局域网/互联网）
- [ ] 残局挑战模式（内置经典残局）

## 运行环境

- Python 3.6+
- Pygame 2.0+

## 安装与运行

1. 克隆仓库：
```bash
git clone https://github.com/eivatlbetas/chinese_chess_game.git
```

2. 安装依赖：
```bash
pip install pygame
```

3. 运行游戏：
```bash
python main.py
```

## 操作说明

- 左键点击棋子选择
- 左键点击目标位置移动
- 右键取消当前选择
- 游戏会自动判断胜负和将军状态

## 项目结构

```
chinese_chess_game/
├── board.py       # 棋盘逻辑
├── piece.py       # 棋子逻辑 
├── main.py        # 主程序入口
├── view.py        # 图形界面
└── README.md      # 项目说明
```

## 开发者

[杨泽宇] - [eivatlbetas@163.com]

## 许可证

MIT License
```
这个README包含了项目的基本信息、运行方法、操作说明和项目结构，你可以根据实际情况修改内容。