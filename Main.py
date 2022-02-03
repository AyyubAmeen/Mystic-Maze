import pygame
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
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.state = "game"
        self.running = True
        self.clock = pygame.time.Clock()
        self.terrainSheet = pygame.image.load("Assets/terrain.png")
        self.wizardSheet = pygame.image.load("Assets/wizard.png")

        self.UIObj = UI(self)

    def gameScale(self, baseMap):
        self.tileWidth = self.width / len(baseMap[0])
        self.tileHeight = self.height / len(baseMap)

    def newGame(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.scaleObj = scale(self)
        self.scaleObj.tileScale(baseMap)
        self.scaleObj.npcScale(baseMap)
        
        self.tileWidth = self.scaleObj.tileWidth
        self.tileHeight = self.scaleObj.tileHeight
        self.npcWidth = self.scaleObj.npcWidth
        self.npcHeight = self.scaleObj.npcHeight

        self.roomObj = room(self)
        self.roomObj.newRoom(baseMap)
        self.playerObj = player(self, playerStats)
        self.chaserObj = chaser(self, 600, 300)
        self.spellObj = spell(self, straightSpell)
        self.gameUIObj = gameUI(self)

    def event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def gameUpdate(self):
        self.spellObj.update()   
        self.playerObj.update()
        self.gameUIObj.update()
        self.chaserObj.update()

    def gameDraw(self):
        self.window.fill(colour["white"])
        self.roomObj.draw(baseMap)
        self.spellObj.draw()
        self.playerObj.draw()
        self.chaserObj.draw()
        self.gameUIObj.draw()
        pygame.display.update()  

    def main(self):
        self.newGame()
        while self.running:
            self.event()
            self.clock.tick(self.fps)
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            self.mousePos = pygame.mouse.get_pos()
            if self.state == "main menu":
                self.UIObj.mainMenuDraw()
            #if self.state == "settings":

            #if self.state == "pause":

            if self.state == "game":
                self.gameUpdate()
                self.gameDraw()
        pygame.quit()
        sys.exit()

g = game()

if __name__ == "__main__":
    g.main()