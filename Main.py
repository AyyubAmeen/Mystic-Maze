import pygame
import math
import os
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
        self.font = pygame.font.Font("Arial", 32)
        self.state = "game"
        self.running = True
        self.clock = pygame.time.Clock()

    def objects(self):
        self.playerObj = player(self, playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"])
        self.spellObj = spell(basicSpell["projLife"], basicSpell["baseDmg"], basicSpell["numShots"], basicSpell["spd"], basicSpell["size"])
        self.gameUIObj = gameUI()
        self.roomObj = room(self)

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
           if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    playerProjObj.math(playerObj)

    def gameUpdate(self):
        self.spellObj.update(self.roomObj)   
        self.playerObj.update(self.roomObj, self.keysPressed)
        self.gameUIObj.update(self.playerObj)

    def gameDraw(self):
        self.window.fill(colour["white"])
        roomObj.draw(window, colour, mysticMazeObj)
        playerProjObj.draw(window, colour)
        playerObj.draw(window)
        gameUIObj.draw(window, colour)
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
        return

    def settingsDraw(self):
        return

    def main(self):
        self.objects()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")
        while self.running:
            self.clock.tick(self.fps)
            if self.state == "game":
                self.gameEvent()
                self.keysPressed = pygame.key.get_pressed()
                self.gameUpdate()
                self.gameDraw()
        pygame.quit()
        sys.exit()

g = game()

if __name__ == "__main__":
    g.main()