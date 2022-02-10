import pygame
import math
from constants import *
from framework import *

class player:
    def __init__(self, game, stats):
        self.game = game

        self.maxHp = stats["maxHp"]
        self.hp = stats["hp"]
        self.maxMp = stats["maxMp"]
        self.mp = stats["mp"]
        self.mpRegen = stats["mpRegen"]
        self.atk = stats["atk"]
        self.defe = stats["def"]
        self.spd = stats["spd"]
        self.baseSpd = 5
        self.change = pygame.Vector2()

        self.width = self.game.npcWidth
        self.height = self.game.npcHeight
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.game.rect.center

        self.spriteWidth = self.game.tileWidth
        self.spriteHeight = self.game.tileHeight
        self.spriteRect = pygame.Rect(self.rect.x, self.rect.y, self.spriteWidth, self.spriteHeight)

        self.activeItems = []
        self.passiveItems = []

        self.spritesheet = spritesheet(self.game.wizardSheet)
        self.moveAnimCd = 150
        self.idleAnimCd = 300
        self.currentFrame = 0
        self.animLastUpdated = 0
        self.regenLastUpdated = 0
        self.facing = "down"

        #Loading sprites rather then using spritesheet module to keep black outlines
        self.rightIdleList = [pygame.image.load('Assets/Player Frames/Wizard05.png'),
                              pygame.image.load('Assets/Player Frames/Wizard06.png')]

        self.downIdleList = [pygame.image.load('Assets/Player Frames/Wizard00.png'),
                             pygame.image.load('Assets/Player Frames/Wizard01.png')]

        self.upIdleList = [pygame.image.load('Assets/Player Frames/Wizard10.png'),
                           pygame.image.load('Assets/Player Frames/Wizard11.png')]

        self.rightList = [pygame.image.load('Assets/Player Frames/Wizard07.png'),
                          pygame.image.load('Assets/Player Frames/Wizard08.png'),
                          pygame.image.load('Assets/Player Frames/Wizard09.png'),
                          pygame.image.load('Assets/Player Frames/Wizard08.png')]

        self.downList = [pygame.image.load('Assets/Player Frames/Wizard02.png'),
                         pygame.image.load('Assets/Player Frames/Wizard03.png'),
                         pygame.image.load('Assets/Player Frames/Wizard04.png'),
                         pygame.image.load('Assets/Player Frames/Wizard03.png')]

        self.upList = [pygame.image.load('Assets/Player Frames/Wizard12.png'),
                       pygame.image.load('Assets/Player Frames/Wizard13.png'),
                       pygame.image.load('Assets/Player Frames/Wizard14.png'),
                       pygame.image.load('Assets/Player Frames/Wizard13.png')]

        self.sprite = self.downIdleList[0] 
     
    def movement(self):
        self.state = "idle"

        self.change.x = 0
        self.change.y = 0
        self.vel = self.baseSpd * self.spd
        self.diagVel = (1 / math.sqrt(1**2 + 1**2)) * self.vel

        if self.game.keysPressed[pygame.K_a]:      
            self.change.x = -self.vel
            self.state = "left" 
            self.facing = "left"
        if self.game.keysPressed[pygame.K_d]:
            self.change.x = self.vel
            self.state = "right"  
            self.facing = "right"
        if self.game.keysPressed[pygame.K_s]:
            self.change.y = self.vel
            self.state = "down"
            self.facing = "down"
        if self.game.keysPressed[pygame.K_w]:
            self.change.y = -self.vel
            self.state = "up"
            self.facing = "up"

        #Normalizes Change
        if self.change.x == self.vel and self.change.y == self.vel:
            self.change.x = self.diagVel
            self.change.y = self.diagVel
        elif self.change.x == self.vel and self.change.y == -self.vel:
            self.change.x = self.diagVel
            self.change.y = -self.diagVel
        elif self.change.x == -self.vel and self.change.y == self.vel:
            self.change.x = -self.diagVel
            self.change.y = self.diagVel
        elif self.change.x == -self.vel and self.change.y == -self.vel:
            self.change.x = -self.diagVel
            self.change.y = -self.diagVel

        self.windowCollision()
        self.rect.x += self.change.x
        self.axis = "x"
        self.blockCollision()
        self.rect.y += self.change.y
        self.axis = "y"
        self.blockCollision()
        self.spriteRect.center = self.rect.center

    def windowCollision(self):
        if (self.rect.x + self.width + self.change.x) >= (self.game.width):
            self.change.x = 0
        if (self.rect.x + self.change.x) <= 0:
            self.change.x = 0
        if (self.rect.y + self.height + self.change.y) >= (self.game.height):
            self.change.y = 0
        if (self.rect.y + self.change.y) <= 0:
            self.change.y = 0

    def blockCollision(self):
        match self.axis:
            case "x":
                for block in self.game.Room.blocks:
                    if pygame.Rect.colliderect(self.rect, block.rect):
                            if self.change.x < 0:
                                self.rect.left = block.rect.right
                            if self.change.x > 0:
                                self.rect.right = block.rect.left

            case "y":
                for block in self.game.Room.blocks:
                    if pygame.Rect.colliderect(self.rect, block.rect):
                            if self.change.y > 0:
                                self.rect.bottom = block.rect.top
                            if self.change.y < 0:
                                self.rect.top = block.rect.bottom

    def regeneration(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.regenLastUpdated > 50:
            self.regenLastUpdated = currentTime
            if self.mp != self.maxMp:
                self.mp += self.mpRegen

    def animation(self): 
        currentTime = pygame.time.get_ticks()      
        if self.state == "idle":
            if currentTime - self.animLastUpdated > self.idleAnimCd:
                self.animLastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                match self.facing:
                    case "left":
                        self.sprite = pygame.transform.flip(self.rightIdleList[self.currentFrame], True, False)
                    case "right":
                        self.sprite = self.rightIdleList[self.currentFrame]
                    case "down":
                        self.sprite = self.downIdleList[self.currentFrame]
                    case "up":        
                        self.sprite = self.upIdleList[self.currentFrame]
        else:
            if currentTime - self.animLastUpdated > self.moveAnimCd:
                self.animLastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downList)
                match self.state:
                    case "left":
                        self.sprite = pygame.transform.flip(self.rightList[self.currentFrame], True, False)
                    case "right":
                        self.sprite = self.rightList[self.currentFrame]
                    case "down":
                        self.sprite = self.downList[self.currentFrame]
                    case "up":
                        self.sprite = self.upList[self.currentFrame]

    def update(self):
        self.movement()
        self.animation() 
        self.regeneration()
        
    def draw(self):    
        self.game.window.blit(pygame.transform.scale(self.sprite, (self.spriteWidth, self.spriteHeight)), self.spriteRect)