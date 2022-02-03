import pygame
import json
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

class animate:
    def __init__(self):
        return

class load:
    def __init__(self):
        return

class button:
    def __init__(self, game, font, size, text, x, y):
        self.game = game

        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, colour["gold"])
        self.hoverText = self.font.render(text, True, colour["cream"])
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (x + self.rect.width/2, y + self.rect.height/2)
        self.game.window.blit(self.text, (x, y))

    def pressed(self):
        if self.rect.collidepoint(self.game.mousePos):
            if self.game.mousePressed[0]:
                return True
            return False
        return False
        
class drawText:
    def __init__(self, game, font, size, text, colour):
        self.game = game

        self.font = pygame.font.Font(font, size)
        self.rect = self.font.get_rect()
        self.text = self.render(text, True, colour)
        self.game.window.blit(text, (x, y))

class scale:
    def __init__(self, game):
        self.game = game

    def tileScale(self, baseMap):
        self.tileWidth = self.game.width / len(baseMap[0])
        self.tileHeight = self.game.height / len(baseMap)

    def npcScale(self, baseMap):
        self.npcWidth = (self.game.width / len(baseMap[0])) * 0.6
        self.npcHeight = (self.game.height / len(baseMap)) * 0.6