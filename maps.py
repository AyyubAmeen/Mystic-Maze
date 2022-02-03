import pygame
import random
from terrain import *

class room:
    def __init__(self, game):
        self.game = game
        self.currentRoom = 0

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
                if tile == "B":
                    b = block(self.game, x, y)
                    b.draw()
                if tile == "F":
                    f = floor(self.game, x, y)
                    f.draw()

class map(room):
    def __init__(self):
        self.width = 5
        self.height = 5
        self.numFloors = 1
        self.numRooms = 10
        self.floorTileMap = []
        self.roomData = {}
        
    def newMap(self):
        self.floorList()
        self.counter = 1
        self.generate()
        print(self.floorTileMap)
        
    def generate(self):
        if self.counter != self.numRooms:
            self.Room1 = self.Room2
            directionDict = {"left":False, "right":False, "up":False, "down":False}

            directionRandom = random.randint(1,4)
            if directionRandom == 1:
                directionDict["left"] = True
            if directionRandom == 2:
                directionDict["right"] = True
            if directionRandom == 3:
                directionDict["up"] = True
            if directionRandom == 4:
                directionDict["down"] = True

            self.roomData[f"room{self.counter}"] = [directionDict]
            self.counter += 1
            self.generate()

    def lists(self):
        self.floor1D = [0 for x in range(self.width)]
        for i in range(self.floorHeight):
            self.floorTileMap.append(self.floor1D)   
        self.Room2 = self.floorTileMap