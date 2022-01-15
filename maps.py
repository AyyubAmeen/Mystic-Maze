import pygame
import math
import os
import sys
from player import *
from enemy import *
from item import *
from UI import *
from sprites import *
from constants import *

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
        self.borderSize = 10
        self.borderX = 50
        self.borderY = 50
        self.borderWidth = self.game.width - (2 * self.borderX)
        self.borderHeight = self.game.height - (2 * self.borderY)

    def drawRoom(self, mysticMazeObj):
        return
        
    def basicRoomDraw(self, window, colour, mysticMazeObj):
        self.wallsRect = pygame.Rect(0, 0, mysticMazeObj.width, mysticMazeObj.height)
        pygame.draw.rect(window, colour["brown"], self.wallsRect)
        self.borderRect = pygame.Rect(self.borderX, self.borderY, self.borderWidth, self.borderHeight)
        pygame.draw.rect(window, colour["light brown"], self.borderRect)

    def draw(self, window, colour, mysticMazeObj):
        self.basicRoomDraw(window, colour, mysticMazeObj)
