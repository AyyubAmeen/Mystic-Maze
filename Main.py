import pygame
import math
import sys
from player import *
from enemy import *
from item import *
from UI import *
from maps import *
from terrain import *
from framework import *
from constants import *

class game:
    def __init__(self):
        pygame.init()
        self.fps = 60
        self.width = 1280
        self.height = 720
        self.rect = pygame.Rect(0, 0, 1280, 720)
        self.state = "game"
        self.running = True
        self.clock = pygame.time.Clock()
        self.terrainSheet = pygame.image.load("Assets/terrain.png")
        self.wizardSheet = pygame.image.load("Assets/wizard.png")

    def gameScale(self, baseMap):
        self.tileWidth = self.width / len(baseMap[0])
        self.tileHeight = self.height / len(baseMap)

    def newGame(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.gameScale(baseMap)
        self.roomObj = room(self)
        self.roomObj.newRoom(baseMap)
        self.playerObj = player(self, playerStats)
        self.spellObj = spell(self, basicSpell)
        self.gameUIObj = gameUI(self)

    def gameUpdate(self):
        self.spellObj.update()   
        self.playerObj.update()
        self.gameUIObj.update()

    def gameDraw(self):
        self.window.fill(colour["white"])
        self.roomObj.draw(baseMap)
        self.spellObj.draw()
        self.playerObj.draw()
        self.gameUIObj.draw()
        pygame.display.update()  

    def mainMenuUpdate(self):
        return

    def mainMenuDraw(self):
        return

    def pauseMenuUpdate(self):
        return

    def pauseMenuDraw(self):
        return

    def settingsUpdate(self):
        return

    def settingsDraw(self):
        return

    def main(self):
        self.newGame()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.clock.tick(self.fps)
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            self.mousePos = pygame.mouse.get_pos()
            if self.state == "game":
                self.gameUpdate()
                self.gameDraw()
        pygame.quit()
        sys.exit()

g = game()

if __name__ == "__main__":
    g.main()