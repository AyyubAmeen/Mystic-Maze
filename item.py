import pygame
import math
import os
import sys
from player import *
from enemy import *
from main import *
from UI import *
from maps import *
from sprites import *
from constants import *

class spell:
    def __init__(self, projLife, baseDmg, numShots, spd, size):
        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots = numShots 
        self.spd = spd
        self.size = size
        self.projList = []
        self.cooldown = 0
        
    def update(self, roomObj):
        for index, bullet in enumerate(self.projList):
            if (bullet[0] + bullet[2]) <= roomObj.borderX or (bullet[0] + bullet[2]) >= (roomObj.borderX + roomObj.borderWidth):
                self.projList.pop(index)
            else:
                bullet[0] += bullet[2]

            if (bullet[1] + bullet[3]) <= roomObj.borderY or (bullet[1] + bullet[3]) >= (roomObj.borderY + roomObj.borderHeight):
                self.projList.pop(index)
            else:
                bullet[1] += bullet[3]
    
    def math(self, playerObj):
            mouseX, mouseY = pygame.mouse.get_pos()
            distanceX = mouseX - playerObj.playerRect.x
            distanceY = mouseY - playerObj.playerRect.y
            angle = math.atan2(distanceY, distanceX)
            projVelX = self.spd * math.cos(angle)
            projVelY = self.spd * math.sin(angle)
            posX = playerObj.playerRect.x + (playerObj.width/2)
            posY = playerObj.playerRect.y + (playerObj.height/2) 
            self.projList.append([posX, posY, projVelX, projVelY])

    def draw(self, window, colour):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(window, colour["red"], (posX, posY), self.size)
