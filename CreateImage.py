import sys, pygame, math


class CreateImage():
    def __init__(self, spawnX, spawnY, tag,  image):
        
        self.name = tag
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(bottomleft = (spawnX,spawnY))
        
        
