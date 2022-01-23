import pygame
from constants import *

class spritesheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def getSprite(self, x, y, width, height, colour):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        pygame.transform.scale(sprite, (width, height))
        sprite.set_colorkey(colour)
        return sprite

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

class block(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def draw(self):
        self.sprite = self.spritesheet.getSprite(128, 480, self.spriteWidth, self.spriteHeight, colour["black"])
        self.game.window.blit(pygame.transform.scale(self.sprite, (self.width, self.height)), (self.rect.x, self.rect.y))

class floor(terrain):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def draw(self):
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight, colour["black"])
        self.game.window.blit(pygame.transform.scale(self.sprite, (self.width, self.height)), (self.rect.x, self.rect.y))