import pygame
import random
from terrain import *
from constants import *
from framework import *

class room:
    def __init__(self, game):
        self.game = game
        self.directions = {"left":False, "right":False, "up":False, "down":False}
        self.enemies = []
        self.items = []
        self.projectiles = []

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
                    case "L":
                        l = leftRoom(self.game, x, y)
                        l.draw()
                    case "R":
                        r = rightRoom(self.game, x, y)
                        r.draw()
                    case "U":
                        u = upRoom(self.game, x, y)
                        u.draw()
                    case "D":
                        d = downRoom(self.game, x, y)
                        d.draw()

class map:
    def __init__(self):
        self.width = 15
        self.height = 15
        self.numFloors = random.randint(1,3)
        self.numRooms = 6
        self.floorTilemap = []
        self.roomData = {}
        self.currentRoom = 1
        
    def newMap(self):
        self.counter = 1
        self.blankTilemap()
        self.generateFloor()
        print(self.floorTilemap)

    def generateFloor(self):
        if self.counter < self.numRooms + 1:
            self.Room1 = self.Room2

            directionConfirmed = False

            while directionConfirmed == False:
                directionDict = {"left":False, "right":False, "up":False, "down":False}
                directionRandom = random.randint(1,4)
                if directionRandom == 1:
                    tempRoomIndex = self.Room1[1] - 1
                    if tempRoomIndex > 0: 
                        if self.floorTilemap[self.Room1[0]][tempRoomIndex] == 0:  
                            directionDict["left"] = True
                            directionConfirmed = True
                            self.Room2 = [self.Room1[0],tempRoomIndex]
                if directionRandom == 2:
                    tempRoomIndex = self.Room1[1] + 1
                    if tempRoomIndex < self.width: 
                        if self.floorTilemap[self.Room1[0]][tempRoomIndex] == 0:  
                            directionDict["right"] = True
                            directionConfirmed = True
                            self.Room2 = [self.Room1[0],tempRoomIndex]
                if directionRandom == 3:
                    tempRoomIndex = self.Room1[0] - 1
                    if tempRoomIndex > 0: 
                        if self.floorTilemap[tempRoomIndex][self.Room1[1]] == 0:  
                            directionDict["up"] = True
                            directionConfirmed = True
                            self.Room2 = [tempRoomIndex,self.Room1[1]]
                if directionRandom == 4:
                    tempRoomIndex = self.Room1[0] + 1
                    if tempRoomIndex < self.height: 
                        if self.floorTilemap[tempRoomIndex][self.Room1[1]] == 0:  
                            directionDict["down"] = True
                            directionConfirmed = True
                            self.Room2 = [tempRoomIndex,self.Room1[1]]

            self.floorTilemap[self.Room2[0]][self.Room2[1]] = self.counter

            self.roomData[f"main{self.counter}"] = [directionDict]
            self.counter += 1
            self.generateFloor()

    def blankTilemap(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(0)
            self.floorTilemap.append(row)   
        self.Room2 = [int(self.height/2) - 1, int(self.width/2) - 1]

Map = map()
Map.newMap()