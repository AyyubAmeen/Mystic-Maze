import pygame
import math
import random
from constants import *
from framework import *

class enemy:
    def __init__(self, game, x, y):
        self.game = game

        self.x = x
        self.y = y
        self.width = 80 * self.game.widthScale
        self.height = 80 * self.game.heightScale
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.change = pygame.Vector2()

        self.spriteWidth = self.width
        self.spriteHeight = self.height
        self.spriteRect = pygame.Rect(self.rect.x, self.rect.y, self.spriteWidth, self.spriteHeight)

class turret(enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.maxHp = 100
        self.hp = 100
        self.spd = 5
        self.dmg = 10

        self.bulletSize = 10
        self.bulletSpd = 5
        self.projList = []

        self.atk1Cooldown = 750
        self.atk1LastUpdated = 0

    def attack1(self):
        if self.game.currentTime  - self.atk1LastUpdated > self.atk1Cooldown:
            self.atk1LastUpdated = self.game.currentTime 
            playerX = self.game.Player.rect.center[0]
            playerY = self.game.Player.rect.center[1]
            x = self.rect.center[0]
            y = self.rect.center[1]
            distanceX = playerX - x
            distanceY = playerY - y
            angle = math.atan2(distanceY, distanceX)
            velX = self.bulletSpd * math.cos(angle)
            velY = self.bulletSpd * math.sin(angle)
            self.projList.append([x, y, velX, velY])

    def moveBullet(self):
        for index, bullet in enumerate(self.projList):
            for block in self.game.Room.blocks:
                collide = pygame.Rect.collidepoint(block.rect, (bullet[0], bullet[1]))
                if collide:
                    self.projList.pop(index)
                if bullet[0] >= self.game.width or bullet[0] <= 0:
                    self.projList.pop(index)
                if bullet[1] >= self.game.height or bullet[1] <= 0:
                    self.projList.pop(index)
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]

    def update(self):
        self.attack1()
        self.moveBullet()

    def draw(self):
        pygame.draw.rect(self.game.window, colour["red"], self.spriteRect)
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.bulletSize * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.bulletSize)

class chaser(enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.maxHp = 200
        self.hp = 200
        self.spd = 2
        self.dmg = 10
        self.numShots = 3

        self.bulletSize = 10
        self.bulletSpd = 5
        self.bulletLifetime = 100
        self.projList = []

        self.atk1Cooldown = 1000
        self.atk1LastUpdated = 0

    def attack1(self):
        if self.game.currentTime - self.cdLastUpdated > self.cooldown:
            self.cdLastUpdated = self.game.currentTime 
            self.game.Player.mp += -self.mpCost
            for i in range(self.numShots):
                rect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size, self.size)
                rect.center = self.game.Player.rect.center
                distanceX = self.game.mousePos[0] - rect.center[0]
                distanceY = self.game.mousePos[1] - rect.center[1]
                angleMod = random.uniform(-0.05,0.05)
                while angleMod == 0:
                    angleMod = random.uniform(-0.05,0.05)
                angle = math.atan2(distanceY, distanceX) + (math.pi * angleMod)
                velX = (self.spd + random.randint(1,5)) * math.cos(angle) * self.game.widthScale 
                velY = (self.spd + random.randint(1,5)) * math.sin(angle) * self.game.heightScale
                self.projList.append([rect, velX, velY, self.game.currentTime])

    def moveBullet(self):
        for index, bullet in enumerate(self.projList):
            for block in self.game.Room.blocks:
                collide = pygame.Rect.colliderect(block.rect, bullet[0])
                if collide:
                    try:
                        self.projList.pop(index)
                    except:
                        pass
                if bullet[0].center[0] >= self.game.width or bullet[0].center[0] <= 0:
                    try:
                        self.projList.pop(index)
                    except:
                        pass                
                if bullet[0].center[1] >= self.game.height or bullet[0].center[1] <= 0:
                    try:
                        self.projList.pop(index)
                    except:
                        pass
            if self.game.currentTime - bullet[3] > self.lifetime:
                try:
                    self.projList.pop(index)
                except:
                    pass
            bullet[0].x += bullet[1]
            bullet[0].y += bullet[2]

    def move(self):
        distanceX = self.game.Player.rect.center[0] - self.rect.center[0]
        distanceY = self.game.Player.rect.center[1] - self.rect.center[1]
        angle = math.atan2(distanceY, distanceX)
        self.change.x = self.spd * math.cos(angle) * self.game.widthScale
        self.change.y = self.spd * math.sin(angle) * self.game.heightScale
        self.rect.x += self.change.x
        self.rect.y += self.change.y

    def update(self):
        self.attack1()
        self.move()

    def draw(self):
        pygame.draw.rect(self.game.window, colour["blue"], self.spriteRect)