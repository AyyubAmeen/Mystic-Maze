import pygame
import math
import os
from terrain import *

class player:
    def __init__(self, game, maxHp, hp, maxMp, mp, mpRegen, atk, defe, spd):
        self.game = game

        self.maxHp = maxHp
        self.hp = hp
        self.maxMp = maxMp
        self.mp = mp
        self.mpRegen = mpRegen
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.baseSpd = 5
        self.velX = 0
        self.velY = 0
        self.regenLastUpdated = 0

        self.scale = 1.2
        self.width = self.game.tileWidth * self.scale
        self.height = self.game.tileHeight * self.scale
        self.x = (self.game.width / 2) - (self.width / 2)
        self.y = (self.game.height / 2) - (self.height / 2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.spritesheet = spritesheet(self.game.wizardSheet)

        self.currentFrame = 0
        self.lastUpdated = 0
        self.facing = "down"
        self.spriteState = "idle"

        self.rightIdleList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard05.png')),
                              pygame.image.load(os.path.join('Assets/Player Frames/Wizard06.png'))]

        self.downIdleList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard00.png')),
                             pygame.image.load(os.path.join('Assets/Player Frames/Wizard01.png'))]

        self.upIdleList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard10.png')),
                           pygame.image.load(os.path.join('Assets/Player Frames/Wizard11.png'))]

        self.rightList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard07.png')),
                          pygame.image.load(os.path.join('Assets/Player Frames/Wizard08.png')),
                          pygame.image.load(os.path.join('Assets/Player Frames/Wizard09.png')),
                          pygame.image.load(os.path.join('Assets/Player Frames/Wizard08.png'))]

        self.downList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard02.png')),
                         pygame.image.load(os.path.join('Assets/Player Frames/Wizard03.png')),
                         pygame.image.load(os.path.join('Assets/Player Frames/Wizard04.png')),
                         pygame.image.load(os.path.join('Assets/Player Frames/Wizard03.png'))]

        self.upList = [pygame.image.load(os.path.join('Assets/Player Frames/Wizard12.png')),
                       pygame.image.load(os.path.join('Assets/Player Frames/Wizard13.png')),
                       pygame.image.load(os.path.join('Assets/Player Frames/Wizard14.png')),
                       pygame.image.load(os.path.join('Assets/Player Frames/Wizard13.png'))]

        self.currentSprite = self.downIdleList[0] 
        
    def movement(self):
        self.velX = 0
        self.velY = 0
        self.vel = self.baseSpd * self.spd
        self.diagVel = math.sqrt(1/2) * self.vel

        if self.game.keysPressed[pygame.K_a]:      
            self.velX += -self.vel
        if self.game.keysPressed[pygame.K_d]:
            self.velX += self.vel
        if self.game.keysPressed[pygame.K_s]:
            self.velY += self.vel
        if self.game.keysPressed[pygame.K_w]:
            self.velY += -self.vel

    def normalisation(self):
        if self.velX == self.vel and self.velY == self.vel:
            self.velX = self.diagVel
            self.velY = self.diagVel
        elif self.velX == self.vel and self.velY == -self.vel:
            self.velX = self.diagVel
            self.velY = -self.diagVel
        elif self.velX == -self.vel and self.velY == self.vel:
            self.velX = -self.diagVel
            self.velY = self.diagVel
        elif self.velX == -self.vel and self.velY == -self.vel:
            self.velX = -self.diagVel
            self.velY = -self.diagVel

    def setState(self):
        self.state = "idle"

        if self.game.keysPressed[pygame.K_a]:
            self.state = "left" 
            self.facing = "left"
        if self.game.keysPressed[pygame.K_d]:
            self.state = "right"  
            self.facing = "right"
        if self.game.keysPressed[pygame.K_s]:
            self.state = "down"
            self.facing = "down"
        if self.game.keysPressed[pygame.K_w]:
            self.state = "up"
            self.facing = "up"

    def blockCollision(self):
        for block in self.game.roomObj.blockRects:
            collide = pygame.Rect.colliderect(self.rect, block)
            if self.rect.x == block.right: 
                if collide:
                    self.rect.y += self.velY
            elif self.rect.right ==  block.x:
                if collide:
                    self.rect.y += self.velY
            elif self.rect.bottom == block.y:
                if collide:
                    self.rect.x += self.velX
            elif self.rect.y == block.bottom:
                if collide:
                    self.rect.x += self.velX
            else:
                self.rect.x += self.velX
                self.rect.y += self.velY

    def regeneration(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.regenLastUpdated > 50:
            self.regenLastUpdated = currentTime
            if self.mp != self.maxMp:
                self.mp += self.mpRegen

    def animation(self): 
        currentTime = pygame.time.get_ticks()      
        if self.state == "idle":
            if currentTime - self.lastUpdated > 200:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                if self.facing == "left":
                    self.currentSprite = pygame.transform.flip(self.rightIdleList[self.currentFrame], True, False)
                if self.facing == "right":
                    self.currentSprite = self.rightIdleList[self.currentFrame]
                if self.facing == "down":
                    self.currentSprite = self.downIdleList[self.currentFrame]
                if self.facing == "up":        
                    self.currentSprite = self.upIdleList[self.currentFrame]
        else:
            if currentTime - self.lastUpdated > 150:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downList)
                if self.state == "left":
                    self.currentSprite = pygame.transform.flip(self.rightList[self.currentFrame], True, False)
                if self.state == "right":
                    self.currentSprite = self.rightList[self.currentFrame]
                if self.state == "down":
                    self.currentSprite = self.downList[self.currentFrame]
                if self.state == "up":
                    self.currentSprite = self.upList[self.currentFrame]

    def update(self):
        self.movement()
        self.normalisation()
        self.setState()
        self.animation() 
        self.regeneration()
        #self.blockCollision()
        self.rect.x += self.velX
        self.rect.y += self.velY
        
    def draw(self):    
        self.game.window.blit(pygame.transform.scale(self.currentSprite, (self.width,self.height)), self.rect)