import pygame
import math
from constants import *

class spell:
    def __init__(self, game, player, projLife, baseDmg, numShots, spd, size):
        self.game = game
        self.player = player

        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots = numShots 
        self.spd = spd
        self.size = size
        self.mpCost = 10
        self.lastUpdated = 0
        self.cooldown = 300

        self.projList = []
        
    def update(self):
        for index, bullet in enumerate(self.projList):
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
        self.spawn()
    
    def spawn(self):
        if self.game.mousePressed[0]:
            if self.player.mp >= self.mpCost:
                currentTime = pygame.time.get_ticks()
                if currentTime - self.lastUpdated > self.cooldown:
                    self.lastUpdated = currentTime
                    mouseX, mouseY = pygame.mouse.get_pos()
                    distanceX = mouseX - self.game.playerObj.rect.x
                    distanceY = mouseY - self.game.playerObj.rect.y
                    angle = math.atan2(distanceY, distanceX)
                    projVelX = self.spd * math.cos(angle)
                    projVelY = self.spd * math.sin(angle)
                    posX = self.game.playerObj.rect.x + (self.game.playerObj.width/2)
                    posY = self.game.playerObj.rect.y + (self.game.playerObj.height/2) 
                    self.projList.append([posX, posY, projVelX, projVelY])
                    self.player.mp += -self.mpCost

    def draw(self):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.size)