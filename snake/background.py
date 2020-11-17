import pygame
from random import randint, randrange

class BG:
    """
    BGクラス
    """
    def __init__(self, surface):
        self.surf = surface

        self.max_obj = 500

        self.width = surface.get_width()

        self.height = surface.get_height()

        self.x = [randrange(-self.width, 2 * self.width) for i in range(self.max_obj)]

        self.y = [randrange(-self.height, 2 * self.height) for i in range(self.max_obj)]

        self.side = [randint(2, 5) for i in range(self.max_obj)]

        self.speed = [randint(1, 4) for i in range(self.max_obj)]

        self.color = [(randrange(255), randrange(255), randrange(255)) for i in range(self.max_obj)]


    def draw(self, direction):
        """
        背景を描画
        """
        if direction == "l":
            self.x = [x + r for x, r in zip(self.x, self.speed)]

        elif direction == "r":
            self.x = [x - r for x, r in zip(self.x, self.speed)]

        elif direction == "u":
            self.y = [y + r for y, r in zip(self.y, self.speed)]

        elif direction == "d":
            self.y = [y - r for y, r in zip(self.y, self.speed)]

        [pygame.draw.rect(self.surf, self.color[1], (self.x[i], self.y[i], self.side[i], self.side[i])) if i % 5 else pygame.draw.rect((self.surf), (randrange(255), randrange(255), randrange(255)),(self.x[i], self.y[i], self.side[i], self.side[i])) for i in range(self.max_obj)]                    

