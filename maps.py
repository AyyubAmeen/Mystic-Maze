import pygame
import random
from enemy import *
from terrain import *
from constants import *
from framework import *

class room:
    def __init__(self):
        self.directions = {"left":False, "right":False, "up":False, "down":False}
        self.enemies = []
        self.items = []
        self.projectiles = []
        self.enemyProj = []
        self.tilemap = [
            ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],  
            ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
            ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
            ]
        self.position = []

        self.blockRects = []
        self.leftTransRects = []
        self.rightTransRects = []
        self.upTransRects = []
        self.downTransRects = []

class maps:
    def __init__(self, game):
        self.game = game

        self.width = 15
        self.height = 15
        self.numFloors = random.randint(1,3)
        self.numRooms = 10
        self.roomData = []
        self.roomTilemap = []
        self.floorList = []
        self.currentRoom = 0
        
    def newMap(self):
        self.generateBlankRoomTilemap()
        self.generateRoomTilemap()
        self.setTilemap()
        self.setRectLists()
        self.setEnemies()
        for y, row in enumerate(self.roomTilemap): 
            print(*self.roomTilemap[y])

    def loadMap(self, roomData, roomTilemap, currentRoom):
        self.roomData = roomData
        self.roomTilemap = roomTilemap
        self.currentRoom = currentRoom
        for y, row in enumerate(self.roomTilemap): 
            print(*self.roomTilemap[y])

    def setDirections(self):
        directionConfirmed = False

        while directionConfirmed == False:
            directionRandom = random.randint(1,4)
            if directionRandom == 1:
                tempRoomIndex = self.Room1[1] - 1
                if tempRoomIndex > 0: 
                    if self.roomTilemap[self.Room1[0]][tempRoomIndex] == "x":  
                        self.roomObj.directions["left"] = True
                        directionConfirmed = True
                        self.Room2 = [self.Room1[0], tempRoomIndex]
            if directionRandom == 2:
                tempRoomIndex = self.Room1[1] + 1
                if tempRoomIndex < len(self.roomTilemap[0]): 
                    if self.roomTilemap[self.Room1[0]][tempRoomIndex] == "x":  
                        self.roomObj.directions["right"] = True
                        directionConfirmed = True
                        self.Room2 = [self.Room1[0], tempRoomIndex]
            if directionRandom == 3:
                tempRoomIndex = self.Room1[0] - 1
                if tempRoomIndex > 0: 
                    if self.roomTilemap[tempRoomIndex][self.Room1[1]] == "x":  
                        self.roomObj.directions["up"] = True
                        directionConfirmed = True
                        self.Room2 = [tempRoomIndex, self.Room1[1]]
            if directionRandom == 4:
                tempRoomIndex = self.Room1[0] + 1
                if tempRoomIndex < len(self.roomTilemap): 
                    if self.roomTilemap[tempRoomIndex][self.Room1[1]] == "x":  
                        self.roomObj.directions["down"] = True
                        directionConfirmed = True
                        self.Room2 = [tempRoomIndex, self.Room1[1]]

    def confirmDirections(self):
        for roomObj in self.roomData:
            room = roomObj.position
            tempRoomIndex = room[1] - 1
            if tempRoomIndex > 0: 
                value = self.roomTilemap[room[0]][tempRoomIndex]
                if value != "x":  
                    roomObj.directions["left"] = True
            tempRoomIndex = room[1] + 1
            if tempRoomIndex < len(self.roomTilemap[0]): 
                value = self.roomTilemap[room[0]][tempRoomIndex]
                if value != "x":  
                    roomObj.directions["right"] = True
            tempRoomIndex = room[0] - 1
            if tempRoomIndex > 0: 
                value = self.roomTilemap[tempRoomIndex][room[1]]
                if value != "x":  
                    roomObj.directions["up"] = True
            tempRoomIndex = room[0] + 1
            if tempRoomIndex < len(self.roomTilemap): 
                value = self.roomTilemap[tempRoomIndex][room[1]]
                if value != "x":  
                    roomObj.directions["down"] = True
    
    def setPosition(self):
        for i, roomObj in enumerate(self.roomData):
            for y, row in enumerate(self.roomTilemap): 
                for x, room in enumerate(row):
                    if room == i:
                        roomObj.position = [y,x]

    def setTilemap(self):
        for roomObj in self.roomData:
            if roomObj.directions["left"] == True:
                roomObj.tilemap[4][0] = "L"
            if roomObj.directions["right"] == True:
                roomObj.tilemap[4][15] = "R"
            if roomObj.directions["up"] == True:
                roomObj.tilemap[0][7] = "U"
                roomObj.tilemap[0][8] = "U"
            if roomObj.directions["down"] == True:
                roomObj.tilemap[8][7] = "D"
                roomObj.tilemap[8][8] = "D"

    def setEnemies(self):
        for room in self.roomData:
            for i in range(random.randint(1,4)):
                enemyType = random.randint(1,2)
                if enemyType == 1:
                    room.enemies.append(turret(self.game, random.randint(100, 1000), random.randint(100, 600)))
                if enemyType == 2:
                    room.enemies.append(chaser(self.game, random.randint(100, 1000), random.randint(100, 600)))

    def setRectLists(self):
        for roomObj in self.roomData:
            for y, row in enumerate(roomObj.tilemap): 
                for x, tile in enumerate(row):
                    if tile == "B":
                        b = block(self.game, x, y)
                        roomObj.blockRects.append(b)
                    if tile == "L":
                        l = leftRoom(self.game, x, y)
                        roomObj.leftTransRects.append(l)
                    if tile == "R":
                        r = rightRoom(self.game, x, y)
                        roomObj.rightTransRects.append(r)
                    if tile == "U":
                        u = upRoom(self.game, x, y)
                        roomObj.upTransRects.append(u)
                    if tile == "D":
                        d = downRoom(self.game, x, y)
                        roomObj.downTransRects.append(d)

    def generateRoomTilemapP1(self):
        if self.counter < self.numRooms:
            self.Room1 = self.Room2

            self.roomObj = room()
            self.setDirections()
            self.roomTilemap[self.Room2[0]][self.Room2[1]] = self.counter

            self.roomData.append(self.roomObj)
            self.counter += 1
            
            self.generateRoomTilemapP1()

    def generateRoomTilemapP2(self):
        self.roomData.pop(0)
        self.Room1 = self.Room2
        self.roomObj = room()
        self.roomObj.position = self.Room1
        self.roomData.append(self.roomObj)

    def generateRoomTilemap(self):
        self.counter = 0
        self.Room2 = [int(self.height/2) - 1, int(self.width/2) - 1]

        self.generateRoomTilemapP1()
        self.generateRoomTilemapP2()
        self.setPosition()
        self.confirmDirections()

    def generateBlankRoomTilemap(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append("x")
            self.roomTilemap.append(row)

    def draw(self):
        for y, row in enumerate((self.roomData[self.currentRoom]).tilemap): 
            for x, tile in enumerate(row):
                if tile == "B":
                    b = block(self.game, x, y)
                    b.draw()
                if tile == "F":
                    f = floor(self.game, x, y)
                    f.draw()
                if tile == "L":
                    l = leftRoom(self.game, x, y)
                    l.draw()
                if tile == "R":
                    r = rightRoom(self.game, x, y)
                    r.draw()
                if tile == "U":
                    u = upRoom(self.game, x, y)
                    u.draw()
                if tile == "D":
                    d = downRoom(self.game, x, y)
                    d.draw()
        text(self.game, f"{self.currentRoom}", "black", 24, self.game.rect.center[0], self.game.rect.center[1], True)