import pygame
from constants import *

class spritesheet:
    def __init__(self, sheet, x, y, width, height, colour):
        self.sheet = sheet
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        
    def getSprite(self):
        sprite = pygame.Surface((self.width, self.size))
        sprite.blit(self.sheet, (0, 0), (self.x, self.y, self.width, self.height))
        sprite.set_colorkey(self.colour)
        return sprite

class block:
    def __init__(self, game, room, x, y):
        self.game = game
        self.room = room

        self.x = x * self.room.tileWidth
        self.y = y * self.room.tileHeight
        self.width = self.room.tileWidth
        self.height = self.room.tileHeight

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.sprite = spritesheet(self.game.terrainSheet, 128, 480, self.width, self.height, colour["black"])
        self.game.window.blit(self.sprite, (self.rect.x, self.rect.y))

class floor:
    def __init__(self, game, room, x, y):
        self.game = game
        self.room = room

        self.x = x * self.room.tileWidth
        self.y = y * self.room.tileHeight
        self.width = self.room.tileWidth
        self.height = self.room.tileHeight

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.sprite = spritesheet(self.game.terrainSheet, 416, 96, self.width, self.height, colour["black"])
        self.game.window.blit(self.sprite, (self.rect.x, self.rect.y))