import pygame
from terrain import *

class map:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.numFloor = 1
        self.floor2D = []
        self.floor1D = []  
        self.roomContainer = []
        
    def generate(self):
        self.floorList()
        
    def floorList(self):
        self.floor1D = [0 for x in range(self.floorWidth)]
        for i in range(self.floorHeight):
            self.floor2D.append(self.floor1D)   

class room(map):
    def __init__(self, game):
        self.game = game
        self.currentRoom = 1

    def newRoom(self, tilemap):
        self.blockRects = []
        for y, row in enumerate(tilemap): 
            for x, tile in enumerate(row):
                if tile == "B":
                    b = block(self.game, x, y)
                    self.blockRects.append(b.rect)

    def draw(self, tilemap):
        for y, row in enumerate(tilemap): 
            for x, tile in enumerate(row):
                if tile == "B":
                    b = block(self.game, x, y)
                    b.draw()
                if tile == "F":
                    f = floor(self.game, x, y)
                    f.draw()