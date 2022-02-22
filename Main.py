import pygame
import sys
from menu import * 
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
        self.prevState = "main menu"
        self.state = "main menu"
        self.running = True
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.terrainSheet = pygame.image.load("Assets/terrain.png")
        self.wizardSheet = pygame.image.load("Assets/wizard.png")
        self.rangeSpellSprite = pygame.image.load("Assets/fire.png")
        self.meleeSpellSprite = pygame.image.load("Assets/firesword.png")

        self.Scale = scale(self)
        self.widthScale = self.Scale.widthScale
        self.heightScale = self.Scale.heightScale

        self.Load = load(self)

        self.Menu = menu(self)

    def newGame(self):
        self.Room = room(self)
        self.Player = player(self, playerStats)
        self.UI = ui(self)
        self.Room.newRoom(baseMap)

    def loadGame(self):
        return

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self): 
        self.Player.update()
        self.UI.update()
        if self.keysPressed[pygame.K_ESCAPE]:
            self.state = "pause"

    def draw(self):
        self.window.fill(colour["white"])
        self.Room.draw(baseMap)
        self.Player.draw()
        self.UI.draw()
        pygame.display.update() 

    def main(self):
        self.newGame()
        while self.running: 
            self.event()
            self.clock.tick(self.fps)
            self.currentTime = pygame.time.get_ticks()
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            self.mousePos = pygame.mouse.get_pos()
            match self.state: 
                case "main menu":
                    self.Menu.mainUpdate()
                    self.Menu.mainDraw()
                case "pre game":
                    self.Menu.preGameUpdate()
                    self.Menu.preGameDraw()
                case "game over":
                    self.Menu.gameOverUpdate()
                    self.Menu.gameOverDraw()
                case "settings":
                    self.Menu.settingsUpdate()
                    self.Menu.settingsDraw()
                case "pause":
                    self.Menu.pauseUpdate()
                    self.Menu.pauseDraw()
                case "game":
                    self.update()
                    self.draw()
        pygame.quit()
        sys.exit()

Game = game()

if __name__ == "__main__":
    Game.main()