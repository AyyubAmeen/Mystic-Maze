import pygame
import math
import os
from sprites import *

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

        self.faceLeft, self.faceRight, self.faceUp, self.faceDown = False, False, False, False
        self.left, self.right, self.up, self.down = False, False, False, False
        self.currentFrame = 0
        self.lastUpdated = 0
        self.state = "idle"

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
        self.state = "idle"

        if self.game.keysPressed[pygame.K_a]:
            self.state = "left"           
            self.velX += -self.vel
        if self.game.keysPressed[pygame.K_d]:
            self.state = "right"  
            self.velX += self.vel
        if self.game.keysPressed[pygame.K_s]:
            self.state = "down"
            self.velY += self.vel
        if self.game.keysPressed[pygame.K_w]:
            self.state = "up"
            self.velY += -self.vel

        self.normalisation()

        self.rect.x += self.velX
        self.rect.y += self.velY

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

    def blockCollision(self):
        return

    def regen(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.regenLastUpdated > 1000:
            self.regenLastUpdated = currentTime
            if self.mp != self.maxMp:
                self.mp += self.mpRegen

    def animate(self): 
        currentTime = pygame.time.get_ticks()      
        if self.state == "idle":
            if currentTime - self.lastUpdated > 200:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                if self.faceRight == True:
                    self.currentSprite = self.rightIdleList[self.currentFrame]
                if self.faceLeft == True:
                    self.currentSprite = pygame.transform.flip(self.rightIdleList[self.currentFrame])
                if self.faceDown == True:
                    self.currentSprite = self.downIdleList[self.currentFrame]
                if self.faceUp == True:        
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
        self.animate() 
        self.regen()

    def draw(self):    
        self.game.window.blit(pygame.transform.scale(self.currentSprite, (self.width,self.height)), self.rect)