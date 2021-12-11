import pygame
import os

class player:
    def __init__(self, hp, atk, defe, spd):
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.width, self.height = 70, 70
        
    def movement(self, keysPressed, player):
        if keysPressed[pygame.K_a]: #Left
            player.x -= vel
        if keysPressed[pygame.K_d]: #Right
            player.x += vel
        if keysPressed[pygame.K_s]: #Down
            player.y += vel
        if keysPressed[pygame.K_w]: #Up
            player.y -= vel

    
class enemy:
    def __init__(self, hp, atk, defe, spd):
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
    
def gameScreen(player): 
        window.fill(colour["white"])
        window.blit(playerSprite, (player.x , player.y))
        pygame.display.update()  

def main(p):
    playerS = pygame.Rect(500, 250, p.width, p.height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keysPressed = pygame.key.get_pressed()
        p.movement(keysPressed, playerS)
        gameScreen(playerS)            
        
    pygame.quit()
    
width, height = 1000, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mystic Maze")

colour = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
playerStats = {"hp" : 100, "atk" : 1, "def" : 1, "spd" : 1}

fps = 60 
vel = 5
p = player(playerStats["hp"],playerStats["atk"],playerStats["def"],playerStats["spd"])       
playerSpriteSheetImage = pygame.image.load(os.path.join('Assets', 'Wizard Spritesheet.png'))
playerSpriteImage = pygame.image.load(os.path.join('Assets', 'Wizard.png'))
playerSprite = pygame.transform.scale(playerSpriteImage, (p.width, p.height))
    
if __name__ == "__main__":
    main(p)
