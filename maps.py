import pygame
import random
from terrain import *
from constants import *
from framework import *

class room:
    def __init__(self, game):
        self.game = game

    def newRoom(self, tilemap):
        self.blocks = []
        for y, row in enumerate(tilemap): 
            for x, tile in enumerate(row):
                if tile == "B":
                    b = block(self.game, x, y)
                    self.blocks.append(b)

    def draw(self, tilemap):
        for y, row in enumerate(tilemap): 
            for x, tile in enumerate(row):
                match tile:
                    case "B":
                        b = block(self.game, x, y)
                        b.draw()
                    case "F":
                        f = floor(self.game, x, y)
                        f.draw()

class map:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.numFloors = random.randint(1,3)
        self.numRooms = 10
        self.roomTilemap = []
        self.roomData = {}
        self.currentRoom = "0"
        
    def newMap(self):
        self.blankTilemap()
        self.counter = 1
        self.generate()
        print(self.roomTilemap)
        
    def generate(self):
        if self.counter != self.numRooms:
            self.Room1 = self.Room2

            directionDict = {"left":False, "right":False, "up":False, "down":False}
            directionRandom = random.randint(1,4)
            match directionRandom:
                case 1:
                    directionDict["left"] = True
                case 2:
                    directionDict["right"] = True
                case 3:
                    directionDict["up"] = True
                case 4:
                    directionDict["down"] = True

            numEnemyRandom = random.randint(1,10)


            self.roomData[f"{self.counter}"] = [directionDict]
            self.counter += 1
            self.generate()

    def blankTilemap(self):
        self.room1D = [0 for x in range(self.width)]
        for i in range(self.height):
            self.roomTileMap.append(self.roomRow)   
        self.Room2 = self.roomTileMap[0][0]