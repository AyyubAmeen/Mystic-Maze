import pygame
from constants import *

class spritesheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def getSprite(self, x, y, spriteWidth, spriteHeight, width, height, colour):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, spriteWidth, spriteHeight))
        pygame.transform.scale(sprite, (width, height))
        sprite.set_colorkey(colour)
        return sprite

class terrain:
    def __init__(self, game, room, x, y):
        self.game = game
        self.room = room

        self.x = x * self.room.tileWidth
        self.y = y * self.room.tileHeight
        self.width = self.room.tileWidth
        self.height = self.room.tileHeight
        self.spriteWidth = spriteSize
        self.spriteHeight = spriteSize
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.spritesheet = spritesheet(self.game.terrainSheet)

class block(terrain):
    def __init__(self, game, room, x, y):
        super().__init__(game, room, x, y)

    def draw(self):
        self.sprite = self.spritesheet.getSprite(128, 480, self.spriteWidth, self.spriteHeight, self.width, self.height, colour["black"])
        self.game.window.blit(self.surf, (self.rect.x, self.rect.y))

class floor(terrain):
    def __init__(self, game, room, x, y):
        super().__init__(game, room, x, y)

    def draw(self):
        self.sprite = self.spritesheet.getSprite(416, 96, self.spriteWidth, self.spriteHeight, self.width, self.height, colour["black"])
        self.game.window.blit(self.surf, (self.rect.x, self.rect.y))