import pygame
from constants import *
from framework import *

class terrain:
    def __init__(self, game, x, y):
        self.game = game

        self.x = x * self.game.tileWidth
        self.y = y * self.game.tileHeight
        self.width = self.game.tileWidth
        self.height = self.game.tileHeight
        self.spriteWidth = spriteSize
        self.spriteHeight = spriteSize

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.spritesheet = spritesheet(self.game.terrainSheet)

    def draw(self):
        self.game.window.blit(pygame.transform.scale(self.sprite, (self.width, self.height)), (self.rect.x, self.rect.y))

class block(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(192, 608, self.spriteWidth, self.spriteHeight)

class floor(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight)


class leftRoom(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight)

class rightRoom(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight)

class upRoom(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight)

class downRoom(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight)