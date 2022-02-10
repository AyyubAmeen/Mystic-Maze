import pygame
import json
from constants import *

class spritesheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        pygame.transform.scale(sprite, (width, height))
        return sprite

class load:
    def __init__(self):
        return

class scale:
    def __init__(self, game):
        self.game = game
        self.ratio = [16, 9]
        self.baseRes = [1280, 720]

    def tileSize(self):
        self.tileWidth = self.game.width / self.ratio[0]
        self.tileHeight = self.game.height / self.ratio[1]

    def npcSize(self):
        self.npcWidth = (self.game.width / self.ratio[0]) * 0.6
        self.npcHeight = (self.game.height / self.ratio[1]) * 0.6

    def scale(self):
        self.widthScale = self.game.width / self.baseRes[0]
        self.heightScale = self.game.height / self.baseRes[1]

class button:
    def __init__(self, game, text, x, y):
        self.game = game

        self.font = pygame.font.Font("Assets/prstart.ttf", 36)
        self.text = self.font.render(text, True, colour["white"])
        self.rect = self.text.get_rect(center=(x, y))

    def draw(self):
        #if self.rect.collidepoint(self.game.mousePos):
        #    self.text = self.font.render(self.text, True, colour["cream"])
        #else:
        #    self.text = self.font.render(self.text, True, colour["white"])
        #self.rect = self.text.get_rect(center=(x, y))
        self.game.window.blit(self.text, self.rect)

    def pressed(self):
        if self.rect.collidepoint(self.game.mousePos):
            if self.game.mousePressed[0]:
                return True
            return False
        return False

class text:
    def __init__(self, game, text, x, y):
        self.game = game

        self.font = pygame.font.Font("Assets/prstart.ttf", 24) 
        self.text = self.font.render(text, True, colour["white"])
        self.rect = self.text.get_rect(center=(x, y))
        self.game.window.blit(self.text, self.rect)

class title:
    def __init__(self, game, text, x, y):
        self.game = game

        self.font = pygame.font.Font("Assets/prstartk.ttf", 48) 
        self.text = self.font.render(text, True, colour["white"])
        self.rect = self.text.get_rect(center=(x, y))
        self.game.window.blit(self.text, self.rect)