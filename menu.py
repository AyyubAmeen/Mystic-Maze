from framework import *
from constants import *

class menu:
    def __init__(self, game):
        self.game = game

        self.tempResolution = 0

    def initialize(self):
        #Main Menu
        self.mainPlayButton = button(self.game, "Play", 36, 0.5 * self.game.width, 0.4 * self.game.height, True)
        self.mainSettingsButton = button(self.game, "Settings", 36, 0.5 * self.game.width, 0.55 * self.game.height, True)
        self.mainQuitButton = button(self.game, "Quit", 36, 0.5 * self.game.width, 0.7 * self.game.height, True)
        self.mainButtonList = [self.mainPlayButton, self.mainSettingsButton, self.mainQuitButton]

        #Pre Game Menu
        self.preGameNewGameButton = button(self.game, "New Game", 36, 0.5 * self.game.width, 0.5 * self.game.height, True)
        self.preGameLoadGameButton = button(self.game, "Load Game", 36, 0.5 * self.game.width, 0.65 * self.game.height, True)
        self.preGameBackButton = button(self.game, "Back", 36, 0.5 * self.game.width, 0.8 * self.game.height, True)
        self.preGameButtonList = [self.preGameNewGameButton, self.preGameLoadGameButton, self.preGameBackButton]

        #Game Over Menu
        self.gameOverReturnButton = button(self.game, "Return To Main Menu", 36, 0.5 * self.game.width, 0.5 * self.game.height, True)
        self.gameOverRestartButton = button(self.game, "Restart", 36, 0.5 * self.game.width, 0.65 * self.game.height, True)
        self.gameOverSettingsButton = button(self.game, "Settings", 36, 0.5 * self.game.width, 0.8 * self.game.height, True)
        self.gameOverQuitButton = button(self.game, "Quit", 36, 0.5 * self.game.width, 0.95 * self.game.height, True)
        self.gameOverButtonList = [self.gameOverReturnButton, self.gameOverRestartButton, self.gameOverSettingsButton, self.gameOverQuitButton]

        #Pause Menu
        self.pauseResumeButton = button(self.game, "Resume", 36, 0.5 * self.game.width, 0.4 * self.game.height, True)
        self.pauseRestartButton = button(self.game, "Restart", 36, 0.5 * self.game.width, 0.55 * self.game.height, True)
        self.pauseSettingsButton = button(self.game, "Settings", 36, 0.5 * self.game.width, 0.7 * self.game.height, True)
        self.pauseQuitButton = button(self.game, "Quit", 36, 0.5 * self.game.width, 0.85 * self.game.height, True)
        self.pauseButtonList = [self.pauseResumeButton, self.pauseRestartButton, self.pauseSettingsButton, self.pauseQuitButton]

        #Settings Menu
        self.settingsSaveApplyButton = button(self.game, "Save & Apply", 36, 0.3 * self.game.width, 0.9 * self.game.height, True)
        self.settingsBackButton = button(self.game, "Back", 36, 0.7 * self.game.width, 0.9 * self.game.height, True)
        self.settingsResolution = button(self.game, f"{self.game.resolution[self.tempResolution][0]} x {self.game.resolution[self.tempResolution][1]}", 36, 0.6 * self.game.width, 0.2 * self.game.height, True)
        self.settingsButtonList = [self.settingsSaveApplyButton, self.settingsBackButton, self.settingsResolution]

    def mainUpdate(self):
        if self.mainPlayButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "pre game"
        if self.mainSettingsButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "settings"
        if self.mainQuitButton.pressed():
            self.game.running = False

    def mainDraw(self):
        self.game.window.fill(colour["black"])
        title(self.game, "MYSTIC MAZE", "white", 48, 0.5 * self.game.width, 0.1 * self.game.height, True)
        for button in self.mainButtonList:
            button.draw()
        pygame.display.update()
        
    def preGameUpdate(self):
        if self.preGameNewGameButton.pressed():
            self.game.newGame()
            self.game.prevState = self.game.state
            self.game.state = "game"
        if self.preGameLoadGameButton.pressed():
            self.game.loadGame()
            self.game.prevState = self.game.state
            self.game.state = "game"
        if self.preGameBackButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "main menu"

    def preGameDraw(self):
        self.game.window.fill(colour["black"])
        for button in self.preGameButtonList:
            button.draw()
        pygame.display.update()

    def gameOverUpdate(self):
        if self.gameOverReturnButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "main menu"
        if self.gameOverRestartButton.pressed():
            self.game.newGame()
            self.game.prevState = self.game.state
            self.game.state = "game"
        if self.gameOverSettingsButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "settings"
        if self.gameOverQuitButton.pressed():
            self.game.running = False

    def gameOverDraw(self):
        self.game.window.fill(colour["black"])
        title(self.game, "GAME OVER", "white", 64, 0.5 * self.game.width, 0.1 * self.game.height, True)
        for button in self.gameOverButtonList:
            button.draw()
        pygame.display.update()

    def pauseUpdate(self):
        if self.pauseResumeButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "game"
        if self.pauseRestartButton.pressed():
            self.game.newGame()
            self.game.prevState = self.game.state
            self.game.state = "game"
        if self.pauseSettingsButton.pressed():
            self.game.prevState = self.game.state
            self.game.state = "settings"
        if self.pauseQuitButton.pressed():
            self.game.running = False

    def pauseDraw(self):
        self.game.window.fill(colour["black"])
        title(self.game, "Paused", "white", 48, 0.5 * self.game.width, 0.1 * self.game.height, True)
        for button in self.pauseButtonList:
            button.draw()
        pygame.display.update()

    def settingsUpdate(self):
        if self.settingsSaveApplyButton.pressed():
            self.game.currentResolution = self.tempResolution
            self.game.prevResolution = self.game.currentResolution

            self.game.width = self.game.resolution[self.game.currentResolution][0]
            self.game.height = self.game.resolution[self.game.currentResolution][1]
            self.game.rect = pygame.Rect(0, 0, self.game.width, self.game.height)

            self.game.window = pygame.display.set_mode((self.game.width, self.game.height))
            pygame.display.set_caption("Mystic Maze")

            self.game.state = self.game.prevState
            self.game.prevState = "settings"

        if self.settingsBackButton.pressed():
            self.game.width = self.game.resolution[self.game.prevResolution][0]
            self.game.height = self.game.resolution[self.game.prevResolution][1]
            self.game.rect = pygame.Rect(0, 0, self.game.width, self.game.height)

            self.game.window = pygame.display.set_mode((self.game.width, self.game.height))
            pygame.display.set_caption("Mystic Maze")

            self.game.state = self.game.prevState
            self.game.prevState = "settings"

        if self.settingsResolution.pressed():
            self.tempResolution = (self.tempResolution + 1) % len(self.game.resolution)

            self.game.width = self.game.resolution[self.tempResolution][0]
            self.game.height = self.game.resolution[self.tempResolution][1]
            self.game.rect = pygame.Rect(0, 0, self.game.width, self.game.height)

            self.game.window = pygame.display.set_mode((self.game.width, self.game.height))
            pygame.display.set_caption("Mystic Maze")

            self.initialize()
            self.game.Scale = scale(self.game)
            self.game.widthScale = self.game.Scale.widthScale
            self.game.heightScale = self.game.Scale.heightScale
    
    def settingsDraw(self):
        self.game.window.fill(colour["black"])
        text(self.game, "Resolution: ", "white", 36, 0.2 * self.game.width, 0.2 * self.game.height, True)
        for button in self.settingsButtonList:
            button.draw()
        pygame.display.update()