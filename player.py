import pygame
import math
from item import *
from constants import *
from framework import *

class player:
    def __init__(self, game, stats):
        self.game = game

        self.baseStats = stats

        self.maxHp = self.baseStats["maxHp"]
        self.hp = self.baseStats["hp"]
        self.maxMp = self.baseStats["maxMp"]
        self.mp = self.baseStats["mp"]
        self.mpRegen = self.baseStats["mpRegen"]
        self.atk = self.baseStats["atk"]
        self.defe = self.baseStats["def"]
        self.spd = self.baseStats["spd"]
        self.baseSpd = 6.5
        self.change = pygame.Vector2()

        self.width = 48 * self.game.widthScale
        self.height = 48 * self.game.heightScale
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.game.rect.center

        self.spriteWidth = 80 * self.game.widthScale
        self.spriteHeight = 80 * self.game.heightScale
        self.spriteRect = pygame.Rect(self.rect.x, self.rect.y, self.spriteWidth, self.spriteHeight)

        self.activeItems = []
        self.passiveItems = self.baseStats["passiveItems"]
        self.currentItem = 0

        for i in range(len(self.baseStats["activeItems"])):
            if self.baseStats["activeItems"][i] != 0:
                if self.baseStats["activeItems"][i][0] == "r":
                    for item in rangeWeapons:
                        if item["name"] == self.baseStats["activeItems"][i][1:]:
                            self.activeItems.append(rangeSpell(self.game, item))
                            break
                if self.baseStats["activeItems"][i][0] == "m":
                    for item in meleeWeapons:
                        if item["name"] == self.baseStats["activeItems"][i][1:]:
                            self.activeItems.append(meleeSpell(self.game, item))
                            break
            else:
                self.activeItems.append(0)

        self.moveAnimCd = 150
        self.idleAnimCd = 300
        self.animLastUpdated = 0
        self.regenLastUpdated = 0

        self.spritesheet = spritesheet(self.game.wizardSheet)
        self.currentFrame = 0
        self.state = "idle"
        self.facing = "down"

        self.rightIdleList = [pygame.image.load("Assets/Player Frames/Wizard05.png"),
                              pygame.image.load("Assets/Player Frames/Wizard06.png")]

        self.downIdleList = [pygame.image.load("Assets/Player Frames/Wizard00.png"),
                             pygame.image.load("Assets/Player Frames/Wizard01.png")]

        self.upIdleList = [pygame.image.load("Assets/Player Frames/Wizard10.png"),
                           pygame.image.load("Assets/Player Frames/Wizard11.png")]

        self.rightList = [pygame.image.load("Assets/Player Frames/Wizard07.png"),
                          pygame.image.load("Assets/Player Frames/Wizard08.png"),
                          pygame.image.load("Assets/Player Frames/Wizard09.png"),
                          pygame.image.load("Assets/Player Frames/Wizard08.png")]

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
        self.change.x = self.change.x * self.game.widthScale
        self.rect.x += self.change.x
        self.axis = "x"
        self.blockCollision()
        self.change.y = self.change.y * self.game.heightScale
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
                for block in self.game.Map.roomData[self.game.Map.currentRoom].blockRects:
                    if pygame.Rect.colliderect(self.rect, block.rect):
                        if self.change.x < 0:
                            self.rect.left = block.rect.right
                        if self.change.x > 0:
                            self.rect.right = block.rect.left

            case "y":
                for block in self.game.Map.roomData[self.game.Map.currentRoom].blockRects:
                    if pygame.Rect.colliderect(self.rect, block.rect):
                        if self.change.y > 0:
                            self.rect.bottom = block.rect.top
                        if self.change.y < 0:
                            self.rect.top = block.rect.bottom

    def roomTransfer(self):
        if (self.rect.x + self.change.x) <= 0:
            room = self.game.Map.roomData[self.game.Map.currentRoom].position
            newRoom = [room[0], room[1] - 1]
            for i, roomObj in enumerate(self.game.Map.roomData):
                if roomObj.position == newRoom:
                    self.game.Map.currentRoom = i
                    self.rect.x = self.game.width - self.rect.width 
                    break

        if (self.rect.x + self.width + self.change.x) >= (self.game.width):
            room = self.game.Map.roomData[self.game.Map.currentRoom].position
            newRoom = [room[0], room[1] + 1]
            for i, roomObj in enumerate(self.game.Map.roomData):
                if roomObj.position == newRoom:
                    self.game.Map.currentRoom = i
                    self.rect.x = 0 + self.rect.width
                    break

        if (self.rect.y + self.change.y) <= 0:
            room = self.game.Map.roomData[self.game.Map.currentRoom].position
            newRoom = [room[0] - 1, room[1]]
            for i, roomObj in enumerate(self.game.Map.roomData):
                if roomObj.position == newRoom:
                    self.game.Map.currentRoom = i
                    self.rect.y = self.game.height - self.rect.height
                    break

        if (self.rect.y + self.height + self.change.y) >= (self.game.height):
            room = self.game.Map.roomData[self.game.Map.currentRoom].position
            newRoom = [room[0] + 1, room[1]]
            for i, roomObj in enumerate(self.game.Map.roomData):
                if roomObj.position == newRoom:
                    self.game.Map.currentRoom = i
                    self.rect.y = 0 + self.rect.height
                    break

    def regeneration(self):
        if self.game.currentTime  - self.regenLastUpdated > 50:
            self.regenLastUpdated = self.game.currentTime 
            if self.mp < self.maxMp:
                self.mp += self.mpRegen
            if self.mp > self.maxMp:
                self.mp = self.maxMp

    def takeDmg(self, dmg):
        self.hp += -dmg * 1 - self.defe / (100 + self.defe)

    def chooseItem(self):
        if self.game.keysPressed[pygame.K_1]:
            self.currentItem = 0
        if self.game.keysPressed[pygame.K_2]:
            self.currentItem = 1
        if self.game.keysPressed[pygame.K_3]:
            self.currentItem = 2
        if self.game.keysPressed[pygame.K_4]:
            self.currentItem = 3
        if self.game.keysPressed[pygame.K_5]:
            self.currentItem = 4

    def animation(self): 
        if self.state == "idle":
            if self.game.currentTime  - self.animLastUpdated > self.idleAnimCd:
                self.animLastUpdated = self.game.currentTime 
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
            if self.game.currentTime  - self.animLastUpdated > self.moveAnimCd:
                self.animLastUpdated = self.game.currentTime 
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
        self.chooseItem()
        self.roomTransfer()
        for item in self.activeItems:
            if item != 0:
                item.update()
        if self.activeItems[self.currentItem] != 0:
            self.activeItems[self.currentItem].spawn()
        if self.hp < 1:
            self.game.state = "game over"
        
    def draw(self):    
        for item in self.activeItems:
            if item != 0:
                item.draw()
        self.game.window.blit(pygame.transform.scale(self.sprite, (self.spriteWidth, self.spriteHeight)), self.spriteRect)