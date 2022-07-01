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
        self.prevState = "main menu"
        self.state = "main menu"
        self.running = True
        self.clock = pygame.time.Clock()

        self.resolution = [[1280 ,720], [1600, 900], [1920, 1080]]
        self.prevResolution = 0
        self.currentResolution = 0
        self.width = self.resolution[self.currentResolution][0]
        self.height = self.resolution[self.currentResolution][1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.terrainSheet = pygame.image.load("Assets/terrain.png")
        self.wizardSheet = pygame.image.load("Assets/wizard.png")
        self.rangeSpellSprite = pygame.image.load("Assets/fire.png")
        self.meleeSpellSprite = pygame.image.load("Assets/firesword.png")

        self.Scale = scale(self)
        self.widthScale = self.Scale.widthScale
        self.heightScale = self.Scale.heightScale

        self.saveLastUpdated = 0
        self.saveCD = 5000

        self.Save = save(self)
        self.Load = load(self)

        self.Menu = menu(self)
        self.Menu.initialize()

    def newGame(self):
        self.Map = maps(self)
        self.Map.newMap()
        self.Player = player(self, playerStats)
        self.UI = ui(self)

    def loadGame(self):
        p = self.Load.loadPlayer()
        m = self.Load.loadMap()

        self.Map = maps(self)

        if m:
            self.Map.loadMap()
        else:
            self.Map.newMap()

        if p:
            self.Player = player(self, self.loadedPlayerStats)
        else:
            self.Player = player(self, playerStats)

        self.UI = ui(self)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self): 
        self.Player.update()
        for i, enemy in enumerate(self.Map.roomData[self.Map.currentRoom].enemies):
            enemy.update()
            if enemy.hp < 1:
                self.Map.roomData[self.Map.currentRoom].enemies.pop(i)
        self.UI.update()
        if self.keysPressed[pygame.K_ESCAPE]:
            #self.Save.save()
            self.state = "pause"
        #if self.currentTime  - self.saveLastUpdated > self.saveCD:
                #self.saveLastUpdated = self.currentTime 
                #self.Save.save()

    def draw(self):
        self.window.fill(colour["white"])
        self.Map.draw()
        self.Player.draw()
        for enemy in self.Map.roomData[self.Map.currentRoom].enemies:
            enemy.draw()
        self.UI.draw()
        pygame.display.update() 

    def main(self):
        while self.running: 
            self.event()
            self.clock.tick(self.fps)
            self.currentTime = pygame.time.get_ticks()
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            self.mousePos = pygame.mouse.get_pos()
            if self.state == "main menu":
                self.Menu.mainUpdate()
                self.Menu.mainDraw()
            if self.state == "pre game":
                self.Menu.preGameUpdate()
                self.Menu.preGameDraw()
            if self.state == "game over":
                self.Menu.gameOverUpdate()
                self.Menu.gameOverDraw()
            if self.state == "settings":
                self.Menu.settingsUpdate()
                self.Menu.settingsDraw()
            if self.state == "pause":
                self.Menu.pauseUpdate()
                self.Menu.pauseDraw()
            if self.state == "game":
                self.update()
                self.draw()
        #self.Save.save()
        pygame.quit()
        sys.exit()

Game = game()

if __name__ == "__main__":
    Game.main()