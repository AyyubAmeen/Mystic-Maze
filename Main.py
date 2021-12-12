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
        self.velX = 0
        self.velY = 0
        self.vel = 5
        self.width = 64
        self.height = 64
        self.noSprites = 36
        self.spriteScale = 2 
        self.currentFrame = 0
        self.lastUpdated = 0
        self.state = "idle"
        self.rightIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard05.png')),
                              pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard06.png'))]
        self.downIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard00.png')),
                             pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard01.png'))]
        self.upIdleList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard10.png')),
                           pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard11.png'))]
        self.rightList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard07.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard08.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard09.png'))]
        self.downList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard02.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard03.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard04.png'))]
        self.upList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard12.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard14.png'))]
        self.currentSprite = self.downIdleList[0] 
        self.faceLeft, self.faceRight, self.faceUp, self.faceDown = False, False, False, False
        self.left, self.right, self.up, self.down = False, False, False, False
        
    def update(self, playerRect, keysPressed):
        self.setState()
        self.movement(playerRect, keysPressed)
        self.animate()    
        
    def movement(self, playerRect, keysPressed):
        self.velX = 0
        self.velY = 0
        if keysPressed[pygame.K_a]:
            self.velX += -self.vel * self.spd
        if keysPressed[pygame.K_d]:
            self.velX += self.vel * self.spd
        if keysPressed[pygame.K_s]:
            self.velY += self.vel * self.spd
        if keysPressed[pygame.K_w]:
            self.velY += -self.vel * self.spd
        playerRect.x += self.velX
        playerRect.y += self.velY
        
    def draw(self, playerRect, window):    
        window.blit(pygame.transform.scale(self.currentSprite, (self.width,self.height)), (playerRect.x, playerRect.y))
        
    def setState(self):
        self.state = "idle"
        if self.velX < 0:
            self.state = "left"           
        elif self.velX > 0:
            self.state = "right"  
        if self.velY > 0:
            self.state = "down"  
        if self.velY < 0:
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
                    self.currentSprite = pygame.transform.flip(self.rightList[self.currentFrame], True, False)
                if self.state == "right":
                    self.currentSprite = self.rightList[self.currentFrame]
                if self.state == "down":
                    self.currentSprite = self.downList[self.currentFrame]
                if self.state == "up":
                    self.currentSprite = self.upList[self.currentFrame]

class playerProjectile:
    def __init__(self, projRange, projLife, projDmg, projShots):
        self.projRange = projRange
        self.projLife = projLife
        self.projDmg = projDmg
        self.projShots = projShots 
        self.projSpd = 5
        self.projSize = 7
        self.projList = []
        
    def update(self):
        for item in self.projList:
            item[0] += item[2]
            item[1] += item[3]
    
    def math(self, p , playerRect):
            mouseX, mouseY = pygame.mouse.get_pos()
            distanceX = mouseX - playerRect.x
            distanceY = mouseY - playerRect.y
            angle = math.atan2(distanceY, distanceX)
            projVelX = self.projSpd * math.cos(angle)
            projVelY = self.projSpd * math.sin(angle)
            spawnPointX = playerRect.x + (p.width/2)
            spawnPointY = playerRect.y + (p.height/2) 
            self.projList.append([spawnPointX, spawnPointY, projVelX, projVelY])
    
    def draw(self, colour, window):
        for posX, posY, projVelX, projVelY in self.projList:
            posX = int(posX)
            posY = int(posY)
            pygame.draw.circle(window, colour, (posX, posY), self.projSize)
                       
class enemy(stats):
    def __init__(self, hp, atk, defe, spd):
        stats.__init__(self, hp, atk, defe, spd)
    
class enemyProjectile:
    def __init__(self, projRange, projLife, projDmg, projShots, projEff):
     self.projRange = projRange
     self.projLife = projLife
     self.projDmg = projDmg
     self.projShots = projShots
     
def gameScreen(p, pProj, playerRect, window): 
        colour = {"white" : (255, 255, 255)
                  , "black" : (0, 0, 0)
                  , "red" : (255, 0, 0)
                  , "green" : (0, 255, 0)
                  , "blue" : (0, 0, 255)}

        window.fill(colour["white"])
        pProj.draw(colour["red"], window)
        p.draw(playerRect, window)
        pygame.display.update()  

def main(p, pProj):
    width, height = 1000, 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mystic Maze")

    playerRect = pygame.Rect(500, 250, p.width, p.height)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                pProj.math(p, playerRect)
        
        keysPressed = pygame.key.get_pressed()
        pProj.update()   
        p.update(playerRect, keysPressed)
        gameScreen(p, pProj, playerRect, window)
    pygame.quit()

playerStats = {"hp" : 100, "atk" : 1, "def" : 1, "spd" : 1}
basicWandStats = {""}

fps = 60 

p = player(playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"])
pProj = playerProjectile(1, 1, 1, 1)
    
if __name__ == "__main__":
    main(p, pProj)