import pygame
from tilemaps import *
from constants import *
import math
import os

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

    def new(self):
        self.sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = player(self, playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"])
        self.spell = playerProjectile(basicWand["projLife"], basicWand["baseDmg"], basicWand["numShots"], basicWand["spd"], basicWand["size"])
        self.gameUI = gameUI()
        self.room = room(self)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    playerObj.left, playerObj.faceLeft = True, True
                if event.type == pygame.K_d:
                    playerObj.right, playerObj.faceRight = True, True
                if event.type == pygame.K_s:
                    playerObj.down, playerObj.faceDown = True, True
                if event.type == pygame.K_w:
                    playerObj.up, playerObj.faceUp = True, True
           if event.type == pygame.KEYUP:
                if event.type == pygame.K_a:
                    playerObj.left, playerObj.faceRight, playerObj.faceUp, playerObj.faceDown = False, False, False, False
                if event.type == pygame.K_d:
                    playerObj.right, playerObj.faceLeft, playerObj.faceUp, playerObj.faceDown = False, False, False, False
                if event.type == pygame.K_s:
                    playerObj.down, playerObj.faceRight, playerObj.faceUp, playerObj.faceLeft = False, False, False, False
                if event.type == pygame.K_w:
                    playerObj.up, playerObj.faceRight, playerObj.faceLeft, playerObj.faceDown = False, False, False, False
           if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    playerProjObj.math(playerObj)

    def update(self):
        self.sprites.update()

    def draw(self):
        return

    def main(self):
        return

    def mainMenu(self):
        return
     
def gameScreen(mysticMazeObj, playerObj, playerProjObj, gameUIObj, roomObj, window, colour): 
        window.fill(colour["white"])
        roomObj.draw(window, colour, mysticMazeObj)
        playerProjObj.draw(window, colour)
        playerObj.draw(window)
        gameUIObj.draw(window, colour)
        pygame.display.update()  

def main(game, playerObj, playerProjObj, roomObj, gameUIObj, colour):
    window = pygame.display.set_mode((mysticMazeObj.width, mysticMazeObj.height))
    pygame.display.set_caption("Mystic Maze")
    while mysticMazeObj.running = True:
        mysticMazeObj.clock.tick(mysticMazeObj.fps)
        if mysticMazeObj.state == "game":
            keysPressed = pygame.key.get_pressed()
            playerProjObj.update(roomObj)   
            playerObj.update(roomObj, keysPressed)
            gameUIObj.update(playerObj)
            gameScreen(mysticMazeObj, playerObj, playerProjObj, gameUIObj, roomObj, window, colour)
    pygame.quit()


game = game()
playerObj = player(game, playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"])
playerProjObj = playerProjectile(basicWand["projLife"], basicWand["baseDmg"], basicWand["numShots"], basicWand["spd"], basicWand["size"])
gameUIObj = gameUI()
roomObj = room(game)

if __name__ == "__main__":
    main(game, playerObj, playerProjObj, roomObj, gameUIObj, colour)