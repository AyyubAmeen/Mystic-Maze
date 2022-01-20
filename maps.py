import pygame
from sprites import *

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

    #    self.borderSize = 10
    #    self.borderX = 50
    #    self.borderY = 50
    #    self.borderWidth = self.game.width - (2 * self.borderX)
    #    self.borderHeight = self.game.height - (2 * self.borderY)

    def calcTileSize(self, tilemap):

        self.tileWidth = self.game.width / len(tilemap[0])
        self.tileHeight = self.game.height / len(tilemap)

    def draw(self, tilemap):
        self.blocksRects = []
        self.floorRects = []

        for y, row in enumerate(tilemap): 
            for x, tile in enumerate(row):
                if tile == "B":
                    b = block(self.game, self, x, y)
                    b.draw()
                if tile == "F":
                    f = floor(self.game, self, x, y)
                    f.draw()
        
    #def basicRoomDraw(self, colour):
    #    self.wallsRect = pygame.Rect(0, 0, self.game.width, self.game.height)
    #    pygame.draw.rect(self.game.window, colour["brown"], self.wallsRect)
    #    self.borderRect = pygame.Rect(self.borderX, self.borderY, self.borderWidth, self.borderHeight)
    #    pygame.draw.rect(self.game.window, colour["light brown"], self.borderRect)

    #def draw(self, colour):
    #    self.basicRoomDraw(colour)