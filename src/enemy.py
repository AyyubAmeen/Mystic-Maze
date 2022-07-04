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

    def takeDmg(self, dmg):
        self.hp += -dmg

class turret(enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "turret"

        self.maxHp = 100
        self.hp = 100
        self.dmg = 5

        self.bulletSize = 25
        self.bulletSpd = 2

        self.atk1Cooldown = 750
        self.atk1LastUpdated = 0

    def attack1(self):
         if self.game.currentTime - self.atk1LastUpdated > self.atk1Cooldown:
            self.atk1LastUpdated = self.game.currentTime 
            rect = pygame.Rect(self.rect.x, self.rect.y, self.bulletSize, self.bulletSize)
            rect.center = self.rect.center
            distanceX = self.game.Player.rect.center[0] - rect.center[0]
            distanceY = self.game.Player.rect.center[1] - rect.center[1]
            angle = math.atan2(distanceY, distanceX)
            velX = self.bulletSpd * math.cos(angle) * self.game.widthScale
            velY = self.bulletSpd * math.sin(angle) * self.game.heightScale
            self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.append([rect, velX, velY, self.game.currentTime, self.name])

    def moveBullet(self):
        for index, bullet in enumerate(self.game.Map.roomData[self.game.Map.currentRoom].enemyProj):
            if bullet[-1] == self.name:
                for block in self.game.Map.roomData[self.game.Map.currentRoom].blockRects:
                    collide = pygame.Rect.colliderect(block.rect, bullet[0])
                    if collide:
                        try:
                            self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                        except:
                            pass
                if bullet[0].center[0] >= self.game.width or bullet[0].center[0] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                    except:
                        pass                
                if bullet[0].center[1] >= self.game.height or bullet[0].center[1] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                    except:
                        pass
                if pygame.Rect.colliderect(bullet[0], self.game.Player.rect):
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                        self.game.Player.takeDmg(self.dmg)
                    except:
                        pass
                bullet[0].x += bullet[1]
                bullet[0].y += bullet[2]

    def update(self):
        self.attack1()
        self.moveBullet()
        self.spriteRect.center = self.rect.center

    def draw(self):
        pygame.draw.rect(self.game.window, colour["red"], self.spriteRect)
        for bullet in self.game.Map.roomData[self.game.Map.currentRoom].enemyProj:
            posX = int(bullet[0].center[0])
            posY = int(bullet[0].center[1])
            pygame.draw.circle(self.game.window, colour["purple"], (posX, posY), (0.5 * self.bulletSize))
            pygame.draw.circle(self.game.window, colour["blue"], (posX, posY), ((0.5 * self.bulletSize) * (3/5)))

class chaser(enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "chaser"

        self.maxHp = 100
        self.hp = 100
        self.spd = 2
        self.dmg = 5
        self.numShots = 3

        self.bulletSize = 25
        self.bulletSpd = 2
        self.bulletLifetime = 1000

        self.atk1Cooldown = 1000
        self.atk1LastUpdated = 0

    def attack1(self):
        if self.game.currentTime - self.atk1LastUpdated > self.atk1Cooldown:
            self.atk1LastUpdated = self.game.currentTime 
            for i in range(self.numShots):
                rect = pygame.Rect(self.rect.x, self.rect.y, self.bulletSize, self.bulletSize)
                rect.center = self.rect.center
                distanceX = self.game.Player.rect.center[0] - rect.center[0]
                distanceY = self.game.Player.rect.center[1] - rect.center[1]
                angleMod = random.uniform(-0.05,0.05)
                while angleMod == 0:
                    angleMod = random.uniform(-0.05,0.05)
                angle = math.atan2(distanceY, distanceX) + (math.pi * angleMod)
                velX = self.bulletSpd * math.cos(angle) * self.game.widthScale 
                velY = self.bulletSpd * math.sin(angle) * self.game.heightScale
                self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.append([rect, velX, velY, self.game.currentTime, self.name])

    def moveBullet(self):
        for index, bullet in enumerate(self.game.Map.roomData[self.game.Map.currentRoom].enemyProj):
            if bullet[-1] == self.name:
                for block in self.game.Map.roomData[self.game.Map.currentRoom].blockRects:
                    collide = pygame.Rect.colliderect(block.rect, bullet[0])
                    if collide:
                        try:
                            self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                        except:
                            pass
                if bullet[0].center[0] >= self.game.width or bullet[0].center[0] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                    except:
                        pass                
                if bullet[0].center[1] >= self.game.height or bullet[0].center[1] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                    except:
                        pass
                if self.game.currentTime - bullet[3] > self.bulletLifetime:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                    except:
                        pass
                if pygame.Rect.colliderect(bullet[0], self.game.Player.rect):
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].enemyProj.pop(index)
                        self.game.Player.takeDmg(self.dmg)
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
        self.moveBullet()
        self.spriteRect.center = self.rect.center

    def draw(self):
        self.spriteRect.center = self.rect.center
        pygame.draw.rect(self.game.window, colour["blue"], self.spriteRect)
        for bullet in self.game.Map.roomData[self.game.Map.currentRoom].enemyProj:
            posX = int(bullet[0].center[0])
            posY = int(bullet[0].center[1])
            pygame.draw.circle(self.game.window, colour["purple"], (posX, posY), (0.5 * self.bulletSize))
            pygame.draw.circle(self.game.window, colour["blue"], (posX, posY), ((0.5 * self.bulletSize) * (3/5)))