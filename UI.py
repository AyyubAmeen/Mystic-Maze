import pygame
from constants import *

class gameUI:
    def __init__(self, game):
        self.game = game

        self.hpSize = 5
        self.hpX = 15
        self.hpY = 15
        self.hpHeight = 25

        self.mpSize = 4
        self.mpX = 25
        self.mpY = 40
        self.mpHeight = 20

        self.itemBoxesY = 600
        self.itemBoxesWidth = 100
        self.itemBoxesHeight = 100

    def barUpdate(self):
        self.hpWidth = (100 * (self.game.playerObj.hp / self.game.playerObj.maxHp)) * self.hpSize
        self.hpBackWidth = 100 * self.hpSize
        self.mpWidth =  (100 * (self.game.playerObj.mp / self.game.playerObj.maxMp)) * self.mpSize
        self.mpBackWidth =  100 * self.mpSize

        self.hpRect = pygame.Rect(self.hpX, self.hpY, self.hpWidth, self.hpHeight)
        self.hpBackRect = pygame.Rect(self.hpX, self.hpY, self.hpBackWidth, self.hpHeight)
        self.mpRect = pygame.Rect(self.mpX, self.mpY, self.mpWidth, self.mpHeight)
        self.mpBackRect = pygame.Rect(self.mpX, self.mpY, self.mpBackWidth, self.mpHeight)

    def barDraw(self):
        pygame.draw.rect(self.game.window, colour["black"], self.hpBackRect)
        pygame.draw.rect(self.game.window, colour["red"], self.hpRect)        

        pygame.draw.rect(self.game.window, colour["black"], self.mpBackRect)
        pygame.draw.rect(self.game.window, colour["blue"], self.mpRect) 

    def itemBoxesDraw(self):
        self.itemBoxesX = 600
        for i in range(5):
            self.itemBoxesX += 110
            self.itemBoxesRect = pygame.Rect(self.itemBoxesX, self.itemBoxesY, self.itemBoxesWidth, self.itemBoxesHeight)
            pygame.draw.rect(self.game.window, colour["brown"], self.itemBoxesRect)

    def update(self):
        self.barUpdate()

    def draw(self):
        self.itemBoxesDraw()
        self.barDraw()

class button:
    def __init__(self):
        return