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
        self.prevState = "main menu"
        self.state = "main menu"
        self.running = True
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mystic Maze")

        self.pauseLastUpdated = 0
        self.pauseCooldown = 500

        self.terrainSheet = pygame.image.load("Assets/terrain.png").convert_alpha()
        self.wizardSheet = pygame.image.load("Assets/wizard.png").convert_alpha()

        self.Scale = scale(self)
        self.Scale.tileSize()
        self.Scale.npcSize()
        self.Scale.scale()

        self.widthScale = self.Scale.widthScale
        self.heightScale = self.Scale.heightScale
        self.tileWidth = self.Scale.tileWidth
        self.tileHeight = self.Scale.tileHeight
        self.npcWidth = self.Scale.npcWidth
        self.npcHeight = self.Scale.npcHeight

        #Main Menu
        self.mainPlayButton = button(self, "Play", 0.5 * self.width, 0.4 * self.height)
        self.mainSettingsButton = button(self, "Settings", 0.5 * self.width, 0.6 * self.height)
        self.mainQuitButton = button(self, "Quit", 0.5 * self.width, 0.8 * self.height)
        self.mainButtonList = [self.mainPlayButton, self.mainSettingsButton, self.mainQuitButton]

        #Pre Game
        self.preGameNewGameButton = button(self, "New Game", 0.5 * self.width, 0.5 * self.height)
        self.preGameLoadGameButton = button(self, "Load Game", 0.5 * self.width, 0.7 * self.height)
        self.preGameBackButton = button(self, "Back", 0.5 * self.width, 0.9 * self.height)
        self.preGameButtonList = [self.preGameNewGameButton, self.preGameLoadGameButton, self.preGameBackButton]

        #Pause Menu
        self.pauseResumeButton = button(self, "Resume", 0.5 * self.width, 0.4 * self.height)
        self.pauseSettingsButton = button(self, "Settings", 0.5 * self.width, 0.6 * self.height)
        self.pauseQuitButton = button(self, "Quit", 0.5 * self.width, 0.8 * self.height)
        self.pauseButtonList = [self.pauseResumeButton, self.pauseSettingsButton, self.pauseQuitButton]

        #Settings Menu
        self.settingsSaveApplyButton = button(self, "Save & Apply", 0.3 * self.width, 0.9 * self.height)
        self.settingsBackButton = button(self, "Back", 0.7 * self.width, 0.9 * self.height)
        self.settingsButtonList = [self.settingsSaveApplyButton, self.settingsBackButton]

    def newGame(self):
        self.Room = room(self)
        self.Player = player(self, playerStats)
        self.Spell = spell(self, straightSpell)
        self.UI = ui(self)
        self.Room.newRoom(baseMap)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def mainMenuUpdate(self):
        if self.mainPlayButton.pressed():
            self.prevState = "main menu"
            self.state = "pre game"
        if self.mainSettingsButton.pressed():
            self.prevState = "main menu"
            self.state = "settings"
        if self.mainQuitButton.pressed():
            self.runnning = False

    def mainMenuDraw(self):
        self.window.fill(colour["black"])
        title(self, "MYSTIC MAZE", 0.5 * self.width, 0.1 * self.height)
        for button in self.mainButtonList:
            button.draw()
        pygame.display.update()
        
    def preGameUpdate(self):
        if self.preGameNewGameButton.pressed():
            self.newGame()
            self.prevState = "pre game"
            self.state = "game"
        if self.preGameLoadGameButton.pressed():
            self.newGame()
            self.prevState = "pre game"
            self.state = "game"
        if self.preGameBackButton.pressed():
            self.prevState = "pre game"
            self.state = "main menu"

    def preGameDraw(self):
        self.window.fill(colour["black"])
        for button in self.preGameButtonList:
            button.draw()
        pygame.display.update()

    def pauseUpdate(self):
        if self.pauseResumeButton.pressed():
            self.prevState = "pause"
            self.state = "game"
        if self.pauseSettingsButton.pressed():
            self.prevState = "pause"
            self.state = "settings"
        if self.mainQuitButton.pressed():
            self.runnning = False

    def pauseDraw(self):
        self.window.fill(colour["black"])
        title(self, "Paused", 0.5 * self.width, 0.1 * self.height)
        for button in self.pauseButtonList:
            button.draw()
        pygame.display.update()

    def settingsUpdate(self):
        if self.settingsSaveApplyButton.pressed:
            self.prevState = "settings"
            self.state = "pre game"
        if self.settingsBackButton.pressed:
            if self.prevState == "pause":
                self.prevState = "settings"
                self.state == "pause"
            if self.prevState == "main menu":
                self.prevState = "settings"
                self.state == "main menu"

    def settingsDraw(self):
        self.window.fill(colour["black"])
        for button in self.settingsButtonList:
            button.draw()
        pygame.display.update()

    def gameUpdate(self):
        self.Spell.update()   
        self.Player.update()
        self.UI.update()
        if self.keysPressed[pygame.K_ESCAPE]:
            self.state = "pause"

    def gameDraw(self):
        self.window.fill(colour["white"])
        self.Room.draw(baseMap)
        self.Spell.draw()
        self.Player.draw()
        self.UI.draw()
        pygame.display.update() 

    def main(self):
        self.newGame()
        while self.running:
            self.event()
            self.clock.tick(self.fps)
            self.keysPressed = pygame.key.get_pressed()
            self.mousePressed = pygame.mouse.get_pressed()
            self.mousePos = pygame.mouse.get_pos()
            match self.state: 
                case "main menu":
                    self.mainMenuUpdate()
                    self.mainMenuDraw()
                case "pre game":
                    self.preGameUpdate()
                    self.preGameDraw()
                case "settings":
                    self.settingsUpdate()
                    self.settingsDraw()
                case "pause":
                    self.pauseUpdate()
                    self.pauseDraw()
                case "game":
                    self.gameUpdate()
                    self.gameDraw()
        pygame.quit()
        sys.exit()

Game = game()

if __name__ == "__main__":
    Game.main()