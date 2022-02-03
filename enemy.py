import pygame
from constants import*
import numpy
import random
import math

class enemy:
    def __init__(self, game, x, y):
        self.game = game

        self.x = x
        self.y = y
        self.width = self.game.tileWidth
        self.height = self.game.tileHeight
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.spriteWidth = self.game.tileWidth
        self.spriteHeight = self.game.tileHeight
        self.spriteRect = pygame.Rect(self.rect.x, self.rect.y, self.spriteWidth, self.spriteHeight)

    def draw(self):
        self.game.window.blit(self.sprite, self.rect)

class chaser(enemy):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.maxHp = 100
        self.hp = 100
        self.atk = 1
        self.spd = 1
        self.dmg = 1

        self.bulletSize = 10
        self.bulletSpd = 5
        self.projList = []

        self.atk1Cooldown = 750
        self.atk1LastUpdated = 0

    def movement(self):
        playerPos = pygame.Vector2(self.game.playerObj.rect.center)
        chaserPos = pygame.Vector2(self.rect.center)
        self.towards = (chaserPos - playerPos).normalize() / 4
        self.x -= self.towards[0]
        self.y -= self.towards[1]
        self.spriteRect.center = self.rect.center

    def attack1(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.atk1LastUpdated > self.atk1Cooldown:
            self.atk1LastUpdated = currentTime
            playerX = self.game.playerObj.rect.center[0]
            playerY = self.game.playerObj.rect.center[1]
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

    def update(self):
        self.movement()
        self.moveBullet()
        self.attack()

    def draw(self):
        pygame.draw.rect(self.game.window, colour["blue"], self.rect)
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (self.bulletSize * (5/3)))
            pygame.draw.circle(self.game.window, colour["red"], (posX, posY), self.bulletSize)