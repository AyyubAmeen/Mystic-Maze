import pygame


class spritesheet:
    def __init__ (self,width,height,sheet):
        self.sheet = pygame.image.load(sheet).convert
        
    def getSprite(self, x, y, width, height, scale, colour):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.sheet, (0, 0), (i * width, 0, width, height))
        sprite = pygame.transform.scale(self.sheet, (width * scale, height * scale))
        sprite.set_colorkey(colour)