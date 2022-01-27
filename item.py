import pygame
import math
from constants import *

class spell:
    def __init__(self, game, projLife, baseDmg, numShots, spd, size):
        self.game = game

        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots = numShots 
        self.spd = spd
        self.size = size
        self.mpCost = 10
        self.lastUpdated = 0
        self.delay = 300

        self.projList = []
        
    def update(self):
        for index, bullet in enumerate(self.projList):
            #for block in self.game.roomObj.blockRects:
            #    collide = pygame.Rect.collidepoint(block, (bullet[0], bullet[1]))
            #    if collide == True:
            #        self.projList.pop(index)
            #    elif collide == False:
                    bullet[0] += bullet[2]
                    bullet[1] += bullet[3]
        self.spawn()
    
    def spawn(self):
        if self.game.mousePressed[0]:
            if self.game.playerObj.mp >= self.mpCost:
                currentTime = pygame.time.get_ticks()
                if currentTime - self.lastUpdated > self.delay:
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

    def draw(self):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.size)

class melee:
    def __init__(self):
        return