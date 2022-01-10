import pygame
import math
import os

class mysticMaze:
    def __init__(self):
        self.fps = 60
        self.width = 1280
        self.height = 720

class gameUI:
    def __init__(self):
        self.healthSize = 5
        self.healthX = 15
        self.healthY = 15
        self.healthHeight = 25
        self.itemBoxesX = 750
        self.itemBoxesY = 450
        self.itemBoxesWidth = 25
        self.itemBoxesHeight = 25

    def healthbarUpdate(self, playerObj):
        self.healthWidth = (100 * (playerObj.currentHp / playerObj.hp)) * self.healthSize
        self.healthBackWidth = 100 * self.healthSize

        self.healthRect = pygame.Rect(self.healthX, self.healthY, self.healthWidth, self.healthHeight)
        self.healthBackRect = pygame.Rect(self.healthX, self.healthY, self.healthBackWidth, self.healthHeight)

    def healthbarDraw(self, window, colour):
        pygame.draw.rect(window, colour["black"], self.healthBackRect)
        pygame.draw.rect(window, colour["red"], self.healthRect)        

    def itemBoxesDraw(self, window, colour):
        for i in range(5):
            self.itemBoxesX += i * 10
            self.itemBoxesRect = pygame.Rect(self.itemBoxesX, self.itemBoxesY, self.itemBoxesWidth, self.itemBoxesHeight)
            pygame.draw.rect(window, colour["brown"], self.itemBoxesRect)
    
    def update(self, playerObj):
        self.healthbarUpdate(playerObj)

    def draw(self, window, colour):
        self.itemBoxesDraw(window, colour)
        self.healthbarDraw(window, colour)

class items:
    def __init__(self, type):
        self.type = type

class map:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.numFloor = 1
        self.floor2D = []
        self.floor1D = []  
        self.roomContainer = []
        
    def generate(self):
        self.floorList()
        
    def floorList(self):
        self.floor1D = [0 for x in range(self.floorWidth)]
        for i in range(self.floorHeight):
            self.floor2D.append(self.floor1D)   

class room(map):
    def __init__(self, mysticMazeObj):
        self.borderSize = 10
        self.borderX = 50
        self.borderY = 50
        self.borderWidth = mysticMazeObj.width - (2 * self.borderX)
        self.borderHeight = mysticMazeObj.height - (2 * self.borderY)

    def basicRoomDraw(self, window, colour, mysticMazeObj):
        self.wallsRect = pygame.Rect(0, 0, mysticMazeObj.width, mysticMazeObj.height)
        pygame.draw.rect(window, colour["brown"], self.wallsRect)
        self.borderRect = pygame.Rect(self.borderX, self.borderY, self.borderWidth, self.borderHeight)
        pygame.draw.rect(window, colour["light brown"], self.borderRect)

    def draw(self, window, colour, mysticMazeObj):
        self.basicRoomDraw(window, colour, mysticMazeObj)

class stats:
    def __init__(self, hp, atk, defe, spd):
        self.hp = hp
        self.currentHp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd

class player(stats):
    def __init__(self, hp, atk, defe, spd, mysticMazeObj):
        stats.__init__(self, hp, atk, defe, spd)
        self.vel = 5
        self.velX = 0
        self.velY = 0
        self.width = 100
        self.height = 100
        self.spriteScale = 2
        self.faceLeft, self.faceRight, self.faceUp, self.faceDown = False, False, False, False
        self.left, self.right, self.up, self.down = False, False, False, False
        self.playerRect = pygame.Rect((mysticMazeObj.width / 2) - (self.width / 2), (mysticMazeObj.height / 2) - self.height / 2, self.width, self.height)
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
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard09.png')),
                          pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard08.png'))]

        self.downList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard02.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard03.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard04.png')),
                         pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard03.png'))]

        self.upList = [pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard12.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard14.png')),
                       pygame.image.load(os.path.join('Assets', 'Player Frames', 'Wizard13.png'))]

        self.currentSprite = self.downIdleList[0] 
        
    def movement(self, roomObj, keysPressed):
        self.velX = 0
        self.velY = 0
        self.state = "idle"
        if keysPressed[pygame.K_a]:
            self.state = "left"           
            self.velX += -self.vel * self.spd
        if keysPressed[pygame.K_d]:
            self.state = "right"  
            self.velX += self.vel * self.spd
        if keysPressed[pygame.K_s]:
            self.state = "down"
            self.velY += self.vel * self.spd
        if keysPressed[pygame.K_w]:
            self.state = "up"
            self.velY += -self.vel * self.spd

        if ((self.playerRect.x + (self.width * 0.2))+ self.velX) <= roomObj.borderX or ((self.playerRect.x + (self.width * 0.8)) + self.velX) >= (roomObj.borderX + roomObj.borderWidth):
            self.playerRect.x = self.playerRect.x
        else:
            self.playerRect.x += self.velX
        if ((self.playerRect.y + (self.height * 0.2)) + self.velY) <= roomObj.borderY or ((self.playerRect.y + (self.height * 0.8)) + self.velY) >= (roomObj.borderY + roomObj.borderHeight):
            self.playerRect.y = self.playerRect.y
        else:
            self.playerRect.y += self.velY


    def animate(self): 
        currentTime = pygame.time.get_ticks()      
        if self.state == "idle":
            if currentTime - self.lastUpdated > 200:
                self.lastUpdated = currentTime
                self.currentFrame = (self.currentFrame + 1) % len(self.downIdleList)
                if self.faceRight == True:
                    self.currentSprite = self.rightIdleList[self.currentFrame]
                if self.faceRight == True:
                    self.currentSprite = pygame.transform.flip(self.rightIdleList[self.currentFrame])
                if self.faceDown == True:
                    self.currentSprite = self.downIdleList[self.currentFrame]
                if self.faceUp == True:        
                    self.currentSprite = self.upIdleList[self.currentFrame]
        else:
            if currentTime - self.lastUpdated > 150:
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

    def update(self, roomObj, keysPressed):
        self.movement(roomObj, keysPressed)
        self.animate()    

    def draw(self, window):    
        window.blit(pygame.transform.scale(self.currentSprite, (self.width,self.height)), (self.playerRect.x, self.playerRect.y))

class playerProjectile:
    def __init__(self, projLife, baseDmg, numShots, spd, size):
        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots = numShots 
        self.spd = spd
        self.size = size
        self.projList = []
        self.cooldown = 0
        
    def update(self, roomObj):
        for index, bullet in enumerate(self.projList):
            if (bullet[0] + bullet[2]) <= roomObj.borderX or (bullet[0] + bullet[2]) >= (roomObj.borderX + roomObj.borderWidth):
                self.projList.pop(index)
            else:
                bullet[0] += bullet[2]

            if (bullet[1] + bullet[3]) <= roomObj.borderY or (bullet[1] + bullet[3]) >= (roomObj.borderY + roomObj.borderHeight):
                self.projList.pop(index)
            else:
                bullet[1] += bullet[3]
    
    def math(self, playerObj):
            mouseX, mouseY = pygame.mouse.get_pos()
            distanceX = mouseX - playerObj.playerRect.x
            distanceY = mouseY - playerObj.playerRect.y
            angle = math.atan2(distanceY, distanceX)
            projVelX = self.spd * math.cos(angle)
            projVelY = self.spd * math.sin(angle)
            posX = playerObj.playerRect.x + (playerObj.width/2)
            posY = playerObj.playerRect.y + (playerObj.height/2) 
            self.projList.append([posX, posY, projVelX, projVelY])

    def draw(self, window, colour):
        for bullet in self.projList:
            posX = int(bullet[0])
            posY = int(bullet[1])
            pygame.draw.circle(window, colour["orange"], (posX, posY), (self.size * (5/3)))
            pygame.draw.circle(window, colour["red"], (posX, posY), self.size)
                       
class enemy(stats):
    def __init__(self, hp, atk, defe, spd):
        stats.__init__(self, hp, atk, defe, spd)
    
class enemyProjectile:
    def __init__(self, projLife, baseDmg, numShots, spd, size):
        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots = numShots 
        self.spd = spd
        self.size = size
     
def gameScreen(mysticMazeObj, playerObj, playerProjObj, gameUIObj, roomObj, window, colour): 
        window.fill(colour["white"])
        roomObj.draw(window, colour, mysticMazeObj)
        playerProjObj.draw(window, colour)
        playerObj.draw(window)
        gameUIObj.draw(window, colour)
        pygame.display.update()  

def main(mysticMazeObj, playerObj, playerProjObj, roomObj, gameUIObj, colour):
    window = pygame.display.set_mode((mysticMazeObj.width, mysticMazeObj.height))
    pygame.display.set_caption("Mystic Maze")
    state = "game"
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(mysticMazeObj.fps)
        if state == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
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
            keysPressed = pygame.key.get_pressed()
            playerProjObj.update(roomObj)   
            playerObj.update(roomObj, keysPressed)
            gameUIObj.update(playerObj)
            gameScreen(mysticMazeObj, playerObj, playerProjObj, gameUIObj, roomObj, window, colour)
    pygame.quit()

playerStats = {"hp" : 100,
               "atk" : 1,
               "def" : 1,
               "spd" : 1}

basicWand = {"projLife" : 10,
             "baseDmg" : 1,
             "numShots" : 1,
             "spd" : 7.5,
             "size" : 5}

colour = {"white" : (255, 255, 255),
         "black" : (0, 0, 0),
         "gray" : (128, 128, 128),
         "brown" : (102, 51, 0),
         "light brown" : (153, 102, 0),
         "red" : (255, 0, 0),
         "green" : (0, 255, 0),
         "blue" : (0, 0, 255),
         "yellow" : (255, 255, 0),
         "cream" : (255, 204, 102),
         "gold" : (204, 153, 0),
         "orange" : (255, 102, 0),
         "purple" : (102, 0, 102)} 

mysticMazeObj = mysticMaze()
playerObj = player(playerStats["hp"], playerStats["atk"], playerStats["def"], playerStats["spd"], mysticMazeObj)
playerProjObj = playerProjectile(basicWand["projLife"], basicWand["baseDmg"], basicWand["numShots"], basicWand["spd"], basicWand["size"])
gameUIObj = gameUI()
roomObj = room(mysticMazeObj)

if __name__ == "__main__":
    main(mysticMazeObj, playerObj, playerProjObj, roomObj, gameUIObj, colour)