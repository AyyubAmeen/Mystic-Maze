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
        self.text = self.font.render(text, True, colour)
        self.hoverText = self.font.render(text, True, colour)

        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.textRect = self.text.get_rect()
        self.textRect.center = (x + self.textRect.width/2, y + self.textRect.height/2)

        self.state = "no"

    def pressed(self):
        if self.textRect.collidepoint(self.game.mousePos):
            if self.game.mousePressed[0]:
                return True
            return False
        return False

    def draw(self, window, text, bold, colour, x, y):
        text = self.font.render(text, True, colour)
        hoverText = self.font.render(text, True, colour)
        textRect = text.get_rect()
        textRect.center = (x + textRect.width/2, y + textRect.height/2)
        self.game.window.blit(text, (x, y))

    def update(self):
        self.pressed()

class drawText:
    def __init__(self, game, font, size, text, colour):
        self.game = game
        self.font = pygame.font.Font(font, size)
        self.rect = font.get_rect()
        self.text = font.render(text, True, colour)
        self.game.window.blit(text, (x, y))


class sizeScaling:
    def __init__(self):
        return

class statScaling:
    def __init__(self):
        return