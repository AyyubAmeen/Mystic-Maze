import pygame
import pickle
import json
from constants import *

class spritesheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        pygame.transform.scale(sprite, (width, height))
        return sprite

class save:
    def __init__(self, game):
        self.game = game

    def save(self):
        with open("map.txt","w") as f:
            f.write(json.dumps(self.game.Map.roomTilemap))
            f.write(json.dumps(self.game.Map.currentRoom))

        with open("roomData.pkl", "wb") as f:
            pickle.dump(self.game.Map.roomData, f)

        with open("player.txt","w") as f:
            f.write(json.dumps(self.game.Player.activeItems))
            f.write(json.dumps(self.game.Player.passiveItems))

class load:
    def __init__(self, game):
        self.game = game
    
    def loadMap(self):
        try:
            with open("map.txt", "r") as f:
                line = f.readline()
                self.game.loadedRoomTilemap = json.load(line)
                line = f.readline()
                self.game.loadedCurrentRoom = json.load(line)

            with open("roomData.pkl", "rb") as f:
                self.game.loadedRoomData = pickle.load(f)
            return True
        except:
            return False

    def loadPlayer(self):
        try:
            with open("player.txt", "r") as f:
                line = f.readline()
                activeItems = json.load(line)
                line = f.readline()
                passiveItems = json.load(line)
                self.game.loadedPlayerStats = {
                    "maxHp" : 100,
                    "hp" : 100,
                    "maxMp" : 100,
                    "mp" : 100,
                    "mpRegen" : 0.5,
                    "atk" : 1,
                    "def" : 1,
                    "spd" : 1,
                    "activeItems" : activeItems,
                    "passiveItems" : passiveItems} 
            return True
        except:
            return False

class scale:
    def __init__(self, game):
        self.game = game
        self.baseRes = [1280, 720]
        self.widthScale = self.game.width / self.baseRes[0]
        self.heightScale = self.game.height / self.baseRes[1]

class button:
    def __init__(self, game, text, size, x, y, center):
        self.game = game

        self.x = x
        self.y = y
        self.characters = text
        self.centered = center
        self.font = pygame.font.Font("Assets/prstart.ttf", int(size * self.game.widthScale))
        self.text = self.font.render(self.characters, True, colour["white"])

        if self.centered:
            self.rect = self.text.get_rect(center=(self.x, self.y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

    def draw(self):
        if self.rect.collidepoint(self.game.mousePos):
            self.text = self.font.render(f"<{self.characters}>", True, colour["cream"])
        else:
            self.text = self.font.render(self.characters, True, colour["white"])

        if self.centered:
            self.rect = self.text.get_rect(center=(self.x, self.y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

        self.game.window.blit(self.text, self.rect)

    def pressed(self):
        if self.rect.collidepoint(self.game.mousePos):
            if self.game.mousePressed[0]:
                return True
            return False
        return False

class text:
    def __init__(self, game, text, color, size, x, y, center):
        self.game = game

        self.font = pygame.font.Font("Assets/prstart.ttf", int(size * self.game.widthScale)) 
        self.text = self.font.render(text, True, colour[color])

        if center:
            self.rect = self.text.get_rect(center=(x, y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = x
            self.rect.y = y

        self.game.window.blit(self.text, self.rect)

class title:
    def __init__(self, game, text, color, size, x, y, center):
        self.game = game

        self.font = pygame.font.Font("Assets/prstartk.ttf", int(size * self.game.widthScale)) 
        self.text = self.font.render(text, True, colour[color])

        if center:
            self.rect = self.text.get_rect(center=(x, y))
        else:
            self.rect = self.text.get_rect()
            self.rect.x = x
            self.rect.y = y

        self.game.window.blit(self.text, self.rect)