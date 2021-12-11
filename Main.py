import pygame
import math
import os

class stats:
    def __init__(self, hp, atk, defe, spd):
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        
class map:
    def __init__(self):
        self.floorWidth = 5
        self.floorHeight = 5
        self.floorNum = 0
        self.floor2D = []
        self.floor1D = []  
        
    def generate(self):
        self.floorList()
        
    def floorList(self):
        self.floor1D = [0 for x in range(self.floorWidth)]
        for i in range(self.floorHeight):
            self.floor2D.append(self.floor1D)   

class player(stats):
    def __init__(self, hp, atk, defe, spd):
        stats.__init__(self, hp, atk, defe, spd)
        self.xVel = 0
        self.yVel = 0
        self.width = 32
        self.height = 32
        self.noSprites = 36
        self.spriteScale = 2 
        self.currentFrame = 0
        self.currentSprite = self.downIdleList[0]
        self.lastUpdated = 0
        self.state = "idle"
        self.faceLeft, self.faceRight, self.faceUp, self.faceDown = False, False, False, False
        self.left, self.right, self.up, self.down = False, False, False, False
        
    def update(self, playerH):
        self.movement(playerH)
        self.setState()
        self.loadSprites()
        self.animate()    
            
    def loadSprites(self):
        self.rightIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard6.png')),
                              pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard7.png'))]
        self.downIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard1.png')),
                             pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard2.png'))]
        self.upIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard11.png')),
                           pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard12.png'))]
        self.rightList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard8.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard9.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard10.png'))]
        self.downList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard3.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard4.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard5.png'))]
        self.upList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard14.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard15.png'))]
        
    def movement(self, playerH):
        self.xVel = 0
        self.yVel = 0
        if self.left == True:
            self.xVel = -1 * self.spd
        if self.right == True:
            self.xVel = 1 * self.spd
        if self.down == True:
            self.yVel = 1 * self.spd
        if self.up == True:
            self.yVel = -1 * self.spd
        playerH.x += self.xVel
        playerH.y += self.yVel
        
    def draw(self, playerH, window):    
        window.blit(self.currentSprite, (playerH.x, playerH.y))
        
    def setState(self):
        self.state = "idle"
        if self.xVel < 0:
            self.state = "left"           
        if self.xVel > 0:
            self.state = "right"  
        if self.yVel > 0:
            self.state = "down"  
        if self.yVel < 0:
            self.state = "up"     
            
    def animate(self): 
        currentTime = pygame.time.get_ticks()       
        if self.state == "idle":
            if currentTime - self.lastUpdated > 200:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                if self.faceRight is True:
                    self.currentSprite = self.rightIdleList[self.currentFrame]
                if self.faceRight is True:
                    self.currentSprite = pygame.transform.flip(self.rightIdleList[self.currentFrame])
                if self.faceDown is True:
                    self.currentSprite = self.downIdleList[self.currentFrame]
                if self.faceUp is True:        
                    self.currentSprite = self.upIdleList[self.currentFrame]
        else:
            if currentTime - self.lastUpdated > 100:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downList)
                if self.state == "left":
                    self.currentSprite = pygame.transform.flip(self.rightList[self.currentFrame])
                if self.state == "right":
                    self.currentSprite = self.rightList[self.currentFrame]
                if self.state == "down":
                    self.currentSprite = self.downList[self.currentFrame]
                if self.state == "up":
                    self.currentSprite = self.upList[self.currentFrame]

class playerProjectile:
    def __init__(self, projRange, projLife, projDmg, projShots, projEff, width, height):
     self.projRange = projRange
     self.projLife = projLife
     self.projDmg = projDmg
     self.projShots = projShots
     self.projEff = projEff
     self.width = width
     self.height = height
                       
class enemy(stats):
    def __init__(self, hp, atk, defe, spd):
        stats.__init__(self, hp, atk, defe, spd)
    
class enemyProjectile:
    def __init__(self, projRange, projLife, projDmg, projShots, projEff):
     self.projRange = projRange
     self.projLife = projLife
     self.projDmg = projDmg
     self.projShots = projShots
     self.projEff = projEff     
    
def gameScreen(p, playerH, colour, window): 
        window.fill(colour)
        p.draw(playerH, window)
        pygame.display.update()  

def main(p, colour, window):
    playerH = pygame.Rect(500, 250, p.width, p.height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_a:
                    p.left, p.faceLeft = True, True
                if event.type == pygame.K_d:
                    p.right, p.faceRight = True, True
                if event.type == pygame.K_s:
                    p.down, p.faceDown = True, True
                if event.type == pygame.K_w:
                    p.up, p.faceUp = True, True
            if event.type == pygame.KEYUP:
                if event.type == pygame.K_a:
                    p.left, p.faceRight, p.faceUp, p.faceDown = False, False, False, False
                if event.type == pygame.K_d:
                    p.right, p.faceLeft, p.faceUp, p.faceDown = False, False, False, False
                if event.type == pygame.K_s:
                    p.down, p.faceRight, p.faceUp, p.faceLeft = False, False, False, False
                if event.type == pygame.K_w:
                    p.up, p.faceRight, p.faceLeft, p.faceDown = False, False, False, False
                    
        p.update(playerH)
        gameScreen(p, playerH, colour, window)
    pygame.quit()
    
width, height = 1000, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mystic Maze")

colour = {"white" : (255, 255, 255), "black" : (0, 0, 0), "red" : (255, 0, 0), "green" : (0, 255, 0), "blue" : (0, 0, 255)}
playerStats = {"hp" : 100, "atk" : 1, "def" : 1, "spd" : 1}

fps = 60 

p = player(playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"])
    
if __name__ == "__main__":
    main(p, colour["white"], window)