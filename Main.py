import pygame
import math
import sys
from player import *
from enemy import *
from item import *
from UI import *
from maps import *
from sprites import *
from constants import *

class game:
    def __init__(self):
        pygame.init()
        self.fps = 60
        self.width = 1280
        self.height = 720
        self.state = "game"
        self.running = True
        self.clock = pygame.time.Clock()
        self.terrainSheet = pygame.image.load('Assets/terrain.png')
        self.wizardSheet = pygame.image.load('Assets/wizard.png')

    def gameScale(self, baseMap):
        self.tileWidth = self.width / len(baseMap[0])
        self.tileHeight = self.height / len(baseMap)

    def newGame(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.gameScale(baseMap)
        self.roomObj = room(self)
        self.playerObj = player(self, playerStats["maxHp"], playerStats["hp"], playerStats["maxMp"], playerStats["mp"], playerStats["mpRegen"], playerStats["atk"], playerStats["def"], playerStats["spd"])
        self.spellObj = spell(self, self.playerObj, basicSpell["projLife"], basicSpell["baseDmg"], basicSpell["numShots"], basicSpell["spd"], basicSpell["size"])
        self.gameUIObj = gameUI(self)

    def gameEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    self.playerObj.left, self.playerObj.faceLeft = True, True
                if event.type == pygame.K_d:
                    self.playerObj.right, self.playerObj.faceRight = True, True
                if event.type == pygame.K_s:
                    self.playerObj.down, self.playerObj.faceDown = True, True
                if event.type == pygame.K_w:
                    self.playerObj.up, self.playerObj.faceUp = True, True
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_a:
                    self.playerObj.left, self.playerObj.faceRight, self.playerObj.faceUp, self.playerObj.faceDown = False, False, False, False
                if event.type == pygame.K_d:
                    self.playerObj.right, self.playerObj.faceLeft, self.playerObj.faceUp, self.playerObj.faceDown = False, False, False, False
                if event.type == pygame.K_s:
                    self.playerObj.down, self.playerObj.faceRight, self.playerObj.faceUp, self.playerObj.faceLeft = False, False, False, False
                if event.type == pygame.K_w:
                    self.playerObj.up, self.playerObj.faceRight, self.playerObj.faceLeft, self.playerObj.faceDown = False, False, False, False

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

    def mainMenuEvent(self):
        return 

    def mainMenuUpdate(self):
        return

    def mainMenuDraw(self):
        return

    def pauseMenuEvent(self):
        return

    def pauseMenuUpdate(self):
        return

    def pauseMenuDraw(self):
        return

    def settingsEvent(self):
        return

    def settingsUpdate(self):
        return

    def settingsDraw(self):
        return

    def main(self):
        self.newGame()
        while self.running:
            self.clock.tick(self.fps)
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            if self.state == "game":
                self.gameEvent()
                self.gameUpdate()
                self.gameDraw()
        pygame.quit()
        sys.exit()

g = game()

if __name__ == "__main__":
    g.main()