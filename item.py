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
        self.projList = []
        self.cooldown = 0
        
    def update(self):
        for index, bullet in enumerate(self.projList):
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
    
    def spawn(self):
            mouseX, mouseY = pygame.mouse.get_pos()
            distanceX = mouseX - self.game.playerObj.rect.x
            distanceY = mouseY - self.game.playerObj.rect.y
            angle = math.atan2(distanceY, distanceX)
            projVelX = self.spd * math.cos(angle)
            projVelY = self.spd * math.sin(angle)
            posX = self.game.playerObj.rect.x + (self.game.playerObj.width/2)
            posY = self.game.playerObj.rect.y + (self.game.playerObj.height/2) 
            self.projList.append([posX, posY, projVelX, projVelY])

    def draw(self):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.size)