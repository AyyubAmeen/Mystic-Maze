import pygame
import os
from main import *
from spritesheet import *

class player(pygame.sprite.Sprite):
    def __init__(self, game, hp, atk, defe, spd):
        self.game = game
        self.hp = hp
        self.currentHp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.baseSpd = 7
        self.velX = 0
        self.velY = 0
        self.width = 100
        self.height = 100
        self.spriteScale = 2
        self.image
        self.layer = playerLayer
        self.layerGroup = self.game.sprites
        pygame.sprite.Sprite.__init__(self, self.layerGroup)
        self.faceLeft, self.faceRight, self.faceUp, self.faceDown = False, False, False, False
        self.left, self.right, self.up, self.down = False, False, False, False
        self.playerRect = pygame.Rect((self.game.width / 2) - (self.width / 2), (self.game.height / 2) - self.height / 2, self.width, self.height)
        self.currentFrame = 0
        self.lastUpdated = 0
        self.state = "idle"
        self.rightIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard05.png')),
                              pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard06.png'))]

        self.downIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard00.png')),
                             pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard01.png'))]

        self.upIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard10.png')),
                           pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard11.png'))]

        self.rightList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard07.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard08.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard09.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard08.png'))]

        self.downList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard02.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard03.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard04.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard03.png'))]

        self.upList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard12.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard14.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png'))]

        self.currentSprite = self.downIdleList[0] 
        
    def movement(self, roomObj, keysPressed):
        self.velX = 0
        self.velY = 0
        self.vel = self.baseSpd * self.spd
        self.diagVel = math.sqrt(1/2) * self.vel
        self.state = "idle"

        if keysPressed[pygame.K_a]:
            self.state = "left"           
            self.velX += -self.vel
        if keysPressed[pygame.K_d]:
            self.state = "right"  
            self.velX += self.vel
        if keysPressed[pygame.K_s]:
            self.state = "down"
            self.velY += self.vel
        if keysPressed[pygame.K_w]:
            self.state = "up"
            self.velY += -self.vel

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

        if ((self.playerRect.x + (self.width * 0.2))+ self.velX) <= roomObj.borderX or ((self.playerRect.x + (self.width * 0.8)) + self.velX) >= (roomObj.borderX + roomObj.borderWidth):
            self.playerRect.x = self.playerRect.x
        else:
            self.playerRect.x += self.velX
        if ((self.playerRect.y + (self.height * 0.2)) + self.velY) <= roomObj.borderY or ((self.playerRect.y + (self.height * 0.8)) + self.velY) >= (roomObj.borderY + roomObj.borderHeight):
            self.playerRect.y = self.playerRect.y
        else:
            self.playerRect.y += self.velY


    def animate(self): 
        currentTime = pygame.time.get_ticks()      
        if self.state == "idle":
            if currentTime - self.lastUpdated > 200:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                if self.faceRight == True:
                    self.currentSprite = self.rightIdleList[self.currentFrame]
                if self.faceRight == True:
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

    def update(self, roomObj, keysPressed):
        self.movement(roomObj, keysPressed)
        self.animate()    

    def draw(self, window):    
        window.blit(pygame.transform.scale(self.currentSprite, (self.width,self.height)), (self.playerRect.x, self.playerRect.y))