import pygame
from constants import *

class gameUI:
    def __init__(self, game):
        self.game = game

        self.healthSize = 5
        self.healthX = 15
        self.healthY = 15
        self.healthHeight = 25
        self.itemBoxesY = 600
        self.itemBoxesWidth = 100
        self.itemBoxesHeight = 100

    def healthbarUpdate(self):
        self.healthWidth = (100 * (self.game.playerObj.currentHp / self.game.playerObj.hp)) * self.healthSize
        self.healthBackWidth = 100 * self.healthSize

        self.healthRect = pygame.Rect(self.healthX, self.healthY, self.healthWidth, self.healthHeight)
        self.healthBackRect = pygame.Rect(self.healthX, self.healthY, self.healthBackWidth, self.healthHeight)

    def healthbarDraw(self):
        pygame.draw.rect(self.game.window, colour["black"], self.healthBackRect)
        pygame.draw.rect(self.game.window, colour["red"], self.healthRect)        

    def itemBoxesDraw(self):
        self.itemBoxesX = 600
        for i in range(5):
            self.itemBoxesX += 110
            self.itemBoxesRect = pygame.Rect(self.itemBoxesX, self.itemBoxesY, self.itemBoxesWidth, self.itemBoxesHeight)
            pygame.draw.rect(self.game.window, colour["brown"], self.itemBoxesRect)

    
    def update(self):
        self.healthbarUpdate()

    def draw(self):
        self.itemBoxesDraw()
        self.healthbarDraw()

class button:
    def __init__(self):
        return