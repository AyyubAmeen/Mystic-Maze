import pygame
import os

class spritesheet:
    def __init__ (self,width,height,sheet):
        self.width = width
        self.height = height
        self.sheet = sheet
        
    def getSprites(self, noSprite, scale, colour):
        spriteList = []
        sprite = pygame.Surface((self.width, self.height))
        for i in range(noSprite):
            sprite.fill(colour)
            sprite.blit(self.sheet, (0, 0), (i * self.width, 0, self.width, self.height))
            sprite = pygame.transform.scale(self.sheet, (self.width * scale, self.height * scale))
            sprite.set_colorkey(colour)
            spriteList.append(sprite)
        return spriteList