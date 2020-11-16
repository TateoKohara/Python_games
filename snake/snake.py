import pygame

class Snake:
    """
    Snakeクラス
    """
    COLOR = [0, 170, 0]
    SIDE = 15
    length = 2
    vel = 10

    def __init__(self, surface):
        """
        初期化関数
        """
        