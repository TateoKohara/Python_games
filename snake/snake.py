import pygame 
import sys
from pygame.locals import *
import tkinter as tk
import os
from snake import *
from food import *
from background import *
from effects import *

class Game:
    """
    Gameクラス

    Game全体を管理するクラス
    """
    SIZE = WIDTH, HEIGHT = (800, 800)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    fps = 20
    score = 0

    def __init__(self):
        """
        初期化関数
        """
        os.environ["SDL_VIDEO_WINDOW_POS"] = f'{(tk.TK().winfo_screenwidth() - self.WIDTH) // 2}'
        f'{(tk.TK().winfo_screenheight() - self.HEIGHT) // 2}'

        pygame.mixer.pre_init(44100, -16, 2, 2046)
        pygame.mixer.init()

        pygame.init()

        pygame.mixer.music.load("System/Sounds/music.mid")

        pygame.mixer.music.play(9)

        pygame.display.set_caption("Snake")


        self.sound_game_over = pygame.mixer.Sound("System/Sounds/game_over.wav")

        self.sound_eat_food = pygame.mixer.Sound("System/Sounds/eat_food.wav")

        self.surf = pygame.display.set_mode(self.SIZE)

        self.clock = pygame.time.Clock()


        self.bg = BG(self.surf)

        self.effect = Effect(self.surf)

        self.effect_trigger = False

        self.snake = Snake(self.surf)

        self.food = Food(self.surf)


        self.font_score = pygame.font.Font(None, 22)

        self.font_end = pygame.font.Font(None, 48)

        self.font_button = pygame.font.Font(None, 30)


        self.play()

    def play(self):
        """
        キー操作
        foodを食べた時の処理
        ゲームオーバー判定
        """

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[K_LEFT] or keys[K_a]:
                if self.snake.direction != "r":
                  self.snake.direction = "l"

            elif keys[K_RIGHT] or keys[K_d]:
                if self.snake.direction != "l":
                  self.snake.direction = "r"

            elif keys[K_UP] or keys[K_w]:
                if self.snake.direction != "d":
                  self.snake.direction = "u"

            elif keys[K_DOWN] or keys[K_s]:
                if self.snake.direction != "u":
                  self.snake.direction = "d"

            if self.food_is_eaten(self.snake.x, self.snake.y, self.snake.SIDE):
                self.sound_eat_food.play()
                self.snake.add_length()
                self.effect_trigger = True
                self.food.new_foodxy(self.snake.SIDE)
                self.score += 1
                self.fps += 1

            if(self.snake.x < 0 or self.snake.y < 0 or self.snake.x + self.snake.SIDE > self.WIDTH or self.y + snake.SIDE > self.HEIGHT) or len(self.snake.xy) != len(set(self.snake.XY)):
                self.game_over()

            self.draw()    

    def draw(self):
        """
        描画関数
        """
        self.surf.fill(self.BLACK)

        self.surf.blit(self.font_score.render(f'SCORE:{self.score}', 1 , (255, 165, 0)), (self.WIDTH -90, 5))

        self.bg.draw(self.snake.direction)

        self.add_food()

        self.snake.move_snake(self.snake.direction)

        

                  

