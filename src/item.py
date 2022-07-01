import pygame
import math
import random
from constants import *
from framework import *

class passives:
    def __init__(self, game):
        self.game = game

    def hpUp(self):
        return

    def mpUp(self):
        return

    def mpRegenUp(self):
        return

    def attackUp(self):
        return

    def speedUp(self):
        return

    def defenseUp(self):
        return

class rangeSpell:
    def __init__(self, game, stats):
        self.game = game

        self.name = stats["name"]
        self.type = stats["type"]
        self.dmg = stats["dmg"]
        self.numShots = stats["numShots"]
        self.lifetime = stats["lifetime"] * 1000
        self.spd = stats["spd"]
        self.size = stats["size"] * self.game.widthScale
        self.mpCost = stats["mpCost"]

        self.cooldown = stats["cooldown"] * 1000
        self.cdLastUpdated = 0

    def straightSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.Player.mp >= self.mpCost:
                if self.game.currentTime  - self.cdLastUpdated > self.cooldown:
                    self.cdLastUpdated = self.game.currentTime 
                    self.game.Player.mp += -self.mpCost
                    rect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size, self.size)
                    rect.center = self.game.Player.rect.center
                    distanceX = self.game.mousePos[0] - rect.center[0]
                    distanceY = self.game.mousePos[1] - rect.center[1]
                    angle = math.atan2(distanceY, distanceX)
                    velX = self.spd * math.cos(angle) * self.game.widthScale
                    velY = self.spd * math.sin(angle) * self.game.heightScale
                    self.game.Map.roomData[self.game.Map.currentRoom].playerProj.append([rect, velX, velY, self.game.currentTime, self.name])

    def spreadSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.Player.mp >= self.mpCost:
                if self.game.currentTime  - self.cdLastUpdated > self.cooldown:
                    self.cdLastUpdated = self.game.currentTime
                    self.game.Player.mp += -self.mpCost
                    rect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size, self.size)
                    rect.center = self.game.Player.rect.center
                    distanceX = self.game.mousePos[0] - rect.center[0]
                    distanceY = self.game.mousePos[1] - rect.center[1]
                    angle = math.atan2(distanceY, distanceX)
                    velX = self.spd * math.cos(angle) * self.game.widthScale
                    velY = self.spd * math.sin(angle) * self.game.heightScale
                    self.game.Map.roomData[self.game.Map.currentRoom].playerProj.append([rect, velX, velY, self.game.currentTime, self.name])

    def shotgunSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.Player.mp >= self.mpCost:
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
                        self.game.Map.roomData[self.game.Map.currentRoom].playerProj.append([rect, velX, velY, self.game.currentTime, self.name])

    def spawn(self):
        match self.type:
            case "straight":
                self.straightSpawn()
            case "spread":
                self.spreadSpawn()
            case "shotgun":
                self.shotgunSpawn()
        
    def update(self):
        for index, bullet in enumerate(self.game.Map.roomData[self.game.Map.currentRoom].playerProj):
            if bullet[-1] == self.name:
                for block in self.game.Map.roomData[self.game.Map.currentRoom].blockRects:
                    collide = pygame.Rect.colliderect(block.rect, bullet[0])
                    if collide:
                        try:
                            self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                        except:
                            pass
                if bullet[0].center[0] >= self.game.width or bullet[0].center[0] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                    except:
                        pass                
                if bullet[0].center[1] >= self.game.height or bullet[0].center[1] <= 0:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                    except:
                        pass
                if self.game.currentTime - bullet[3] > self.lifetime:
                    try:
                        self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                    except:
                        pass
                for enemy in self.game.Map.roomData[self.game.Map.currentRoom].enemies:
                    if pygame.Rect.colliderect(bullet[0], enemy.rect):
                        try:
                            self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                            enemy.takeDmg(self.dmg)
                        except:
                            pass
                bullet[0].x += bullet[1]
                bullet[0].y += bullet[2]

    def draw(self):
        for bullet in self.game.Map.roomData[self.game.Map.currentRoom].playerProj:
            if bullet[-1] == self.name:
                posX = int(bullet[0].center[0])
                posY = int(bullet[0].center[1])
                pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (0.5 * self.size))
                pygame.draw.circle(self.game.window, colour["red"], (posX, posY), ((0.5 * self.size) * (3/5)))

class meleeSpell:
    def __init__(self, game, stats):
        self.game = game

        self.name = stats["name"]
        self.type = stats["type"]
        self.dmg = stats["dmg"]
        self.distance = stats["distance"]

        if self.type == "rectangle":
            self.size = [stats["size"][0] * self.game.widthScale, stats["size"][1] * self.game.heightScale]
        if self.type == "circle":
            self.size = stats["size"] * self.game.widthScale

        self.lifetime = stats["lifetime"] * 1000
        self.cooldown = stats["cooldown"] * 1000
        self.cdLastUpdated = 0

    def rectangleSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.currentTime - self.cdLastUpdated > self.cooldown:
                self.cdLastUpdated = self.game.currentTime 
                rect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size[0], self.size[1])
                secRect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size[0] * 4/5, self.size[1] * 4/5)
                rect.center = self.game.Player.rect.center
                distanceX = self.game.mousePos[0] - rect.center[0]
                distanceY = self.game.mousePos[1] - rect.center[1]
                angle = math.atan2(distanceY, distanceX)
                spawnX = math.cos(angle) * (self.size[1])
                spawnY = math.sin(angle) * (self.size[0])
                rect.x += spawnX
                rect.y += spawnY
                secRect.center = rect.center
                self.game.Map.roomData[self.game.Map.currentRoom].playerProj.append([self.game.currentTime, rect, secRect, self.name])

    def circleSpawn(self):
        if self.game.mousePressed[0]:
            if self.game.currentTime - self.cdLastUpdated > self.cooldown:
                self.cdLastUpdated = self.game.currentTime 
                rect = pygame.Rect(self.game.Player.rect.x, self.game.Player.rect.y, self.size, self.size)
                rect.center = self.game.Player.rect.center
                distanceX = self.game.mousePos[0] - rect.center[0]
                distanceY = self.game.mousePos[1] - rect.center[1]
                angle = math.atan2(distanceY, distanceX)
                spawnX = math.cos(angle) * (self.size)
                spawnY = math.sin(angle) * (self.size)
                rect.x += spawnX
                rect.y += spawnY
                self.game.Map.roomData[self.game.Map.currentRoom].playerProj.append([self.game.currentTime, rect, self.name])

    def spawn(self):
        match self.type:
            case "rectangle":
                self.rectangleSpawn()
            case "circle":
                self.circleSpawn()

    def update(self):
        for index, melee in enumerate(self.game.Map.roomData[self.game.Map.currentRoom].playerProj):
            if melee[-1] == self.name:
                if self.game.currentTime - melee[0] > self.lifetime:
                    try:
                        self.meleeList.pop(index)
                    except:
                        pass
                for enemy in self.game.Map.roomData[self.game.Map.currentRoom].enemies:
                    if pygame.Rect.colliderect(melee[1], enemy.rect):
                        try:
                            self.game.Map.roomData[self.game.Map.currentRoom].playerProj.pop(index)
                            enemy.takeDmg(self.dmg)
                        except:
                            pass
                
    def draw(self):
        for melee in self.game.Map.roomData[self.game.Map.currentRoom].playerProj:
            if melee[-1] == self.name:
                if self.type == "rectangle":
                    pygame.draw.rect(self.game.window, colour["orange"], melee[1])
                    pygame.draw.rect(self.game.window, colour["red"], melee[2])
                if self.type == "circle":
                    posX = int(melee[1].center[0])
                    posY = int(melee[1].center[1])
                    pygame.draw.circle(self.game.window, colour["orange"], (posX, posY), (0.5 * self.size))
                    pygame.draw.circle(self.game.window, colour["red"], (posX, posY), ((0.5 * self.size) * (4/5)))

class itemDrops:
    def __init__(self, game):
        self.game = game

    def active(self):
        return

    def passive(self):
        return