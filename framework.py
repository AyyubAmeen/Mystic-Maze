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

class save:
    def __init__(self, game):
        self.game = game
    
    def saveMap(self):
        return

    def savePlayer(self):
        with open("player.txt","r") as file:
            file.write(json.dump())

class load:
    def __init__(self, game):
        self.game = game
    
    def loadMap(self):
        return

    def loadPlayer(self):
        return

class scale:
    def __init__(self, game):
        self.game = game
        self.baseRes = [1280, 720]
        self.widthScale = self.game.width / self.baseRes[0]
        self.heightScale = self.game.height / self.baseRes[1]

class button:
    def __init__(self, game, text, size, x, y, center):
        self.game = game

        self.x = x
        self.y = y
        self.characters = text
        self.centered = center
        self.font = pygame.font.Font("Assets/prstart.ttf", int(size * self.game.widthScale))
        self.text = self.font.render(self.characters, True, colour["white"])

        if self.centered:
            self.rect = self.text.get_rect(center=(self.x, self.y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def draw(self):
        if self.rect.collidepoint(self.game.mousePos):
            self.text = self.font.render(f"<{self.characters}>", True, colour["cream"])
        else:
            self.text = self.font.render(self.characters, True, colour["white"])

        if self.centered:
            self.rect = self.text.get_rect(center=(self.x, self.y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        self.game.window.blit(self.text, self.rect)

    def pressed(self):
        if self.rect.collidepoint(self.game.mousePos):
            if self.game.mousePressed[0]:
                return True
            return False
        return False

class text:
    def __init__(self, game, text, color, size, x, y, center):
        self.game = game

        self.font = pygame.font.Font("Assets/prstart.ttf", int(size * self.game.widthScale)) 
        self.text = self.font.render(text, True, colour[color])

        if center:
            self.rect = self.text.get_rect(center=(x, y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = x
            self.rect.y = y

        self.game.window.blit(self.text, self.rect)

class title:
    def __init__(self, game, text, color, size, x, y, center):
        self.game = game

        self.font = pygame.font.Font("Assets/prstartk.ttf", int(size * self.game.widthScale)) 
        self.text = self.font.render(text, True, colour[color])

        if center:
            self.rect = self.text.get_rect(center=(x, y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = x
            self.rect.y = y

        self.game.window.blit(self.text, self.rect)