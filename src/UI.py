import pygame
from item import *
from constants import *
from framework import * 

class ui:
    def __init__(self, game):
        self.game = game

        self.hpSize = 500 * self.game.widthScale
        self.hpX = 15 * self.game.widthScale
        self.hpY = 15 * self.game.heightScale
        self.hpHeight = 25 * self.game.heightScale

        self.mpSize = 400 * self.game.widthScale
        self.mpX = 25 * self.game.widthScale
        self.mpY = 40 * self.game.heightScale
        self.mpHeight = 20 * self.game.heightScale

        self.itemBoxesY = 600 * self.game.heightScale
        self.itemBoxesWidth = 100 * self.game.widthScale
        self.itemBoxesHeight = 100 * self.game.heightScale

        self.itemName = " "

    def barUpdate(self):
        self.hpWidth = (self.game.Player.hp / self.game.Player.maxHp) * self.hpSize
        self.hpBackWidth = self.hpSize
        self.mpWidth =  (self.game.Player.mp / self.game.Player.maxMp) * self.mpSize
        self.mpBackWidth = self.mpSize

        self.hpRect = pygame.Rect(self.hpX, self.hpY, self.hpWidth, self.hpHeight)
        self.hpBackRect = pygame.Rect(self.hpX, self.hpY, self.hpBackWidth, self.hpHeight)
        self.mpRect = pygame.Rect(self.mpX, self.mpY, self.mpWidth, self.mpHeight)
        self.mpBackRect = pygame.Rect(self.mpX, self.mpY, self.mpBackWidth, self.mpHeight)

    def barDraw(self):
        pygame.draw.rect(self.game.window, colour["black"], self.hpBackRect)
        pygame.draw.rect(self.game.window, colour["red"], self.hpRect)
        text(self.game, f"{int(self.game.Player.hp)}/{self.game.Player.maxHp}", "white", 24, self.hpX, self.hpY, False) 

        pygame.draw.rect(self.game.window, colour["black"], self.mpBackRect)
        pygame.draw.rect(self.game.window, colour["blue"], self.mpRect) 
        text(self.game, f"{int(self.game.Player.mp)}/{self.game.Player.maxMp}", "white", 24, self.mpX, self.mpY, False) 

    def itemBoxesDraw(self):
        self.itemBoxesX = 600 * self.game.widthScale
        for i in range(5):
            self.itemBoxesX += 110 * self.game.widthScale
            self.itemBoxesRect = pygame.Rect(self.itemBoxesX, self.itemBoxesY, self.itemBoxesWidth, self.itemBoxesHeight)

            if self.game.Player.currentItem == i:
                pygame.draw.rect(self.game.window, colour["gold"], self.itemBoxesRect)
            else:
                pygame.draw.rect(self.game.window, colour["brown"], self.itemBoxesRect)
            
            if self.game.Player.activeItems[i] != 0:
                if isinstance(self.game.Player.activeItems[i], rangeSpell):
                    self.game.window.blit(pygame.transform.scale(self.game.rangeSpellSprite, (self.itemBoxesWidth, self.itemBoxesHeight)), self.itemBoxesRect)
                if isinstance(self.game.Player.activeItems[i], meleeSpell):
                    self.game.window.blit(pygame.transform.scale(self.game.meleeSpellSprite, (self.itemBoxesWidth, self.itemBoxesHeight)), self.itemBoxesRect)

                if pygame.Rect.collidepoint(self.itemBoxesRect, self.game.mousePos):
                    self.itemName = f"{self.game.Player.activeItems[i].name}"

        text(self.game, self.itemName, "black", 24, self.game.mousePos[0] - len(self.itemName) * 24, self.game.mousePos[1] - 24, False)
        self.itemName = " "

    def update(self):
        self.barUpdate()

    def draw(self):
        self.itemBoxesDraw()
        self.barDraw()