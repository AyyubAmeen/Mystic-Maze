import pygame
import math
import random
from constants import *

class spell:
    def __init__(self, game, stats):
        self.game = game

        self.type = stats["type"]
        self.dmg = stats["dmg"]
        self.numShots = stats["numShots"]
        self.limit = stats["limit"] 
        self.spd = stats["spd"]
        self.size = stats["size"]
        self.mpCost = stats["mpCost"]

        self.cooldown = stats["cooldown"]
        self.lastUpdated = 0

        self.projList = []
    
    def move(self):
        for index, bullet in enumerate(self.projList):
            for block in self.game.roomObj.blocks:
                collide = pygame.Rect.collidepoint(block.rect, (bullet[0], bullet[1]))
                if collide == True:
                    self.projList.pop(index)
            if bullet[0] >= self.game.width or bullet[0] <= 0:
                self.projList.pop(index)
            if bullet[1] >= self.game.height or bullet[1] <= 0:
                self.projList.pop(index)
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]

    def straightSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.playerObj.mp >= self.mpCost:
                currentTime = pygame.time.get_ticks()
                if currentTime - self.lastUpdated > self.cooldown:
                    self.lastUpdated = currentTime
                    mouseX, mouseY = self.game.mousePos
                    x = self.game.playerObj.rect.center[0]
                    y = self.game.playerObj.rect.center[1]
                    distanceX = mouseX - x
                    distanceY = mouseY - y
                    angle = math.atan2(distanceY, distanceX)
                    velX = self.spd * math.cos(angle)
                    velY = self.spd * math.sin(angle)
                    self.projList.append([x, y, velX, velY])
                    self.game.playerObj.mp += -self.mpCost

    def shotgunSpawn(self):
        return

    def update(self):
        self.move()
        if self.type == "straight":
            self.straightSpawn()

    def draw(self):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.size)

class melee:
    def __init__(self):
        return