import sys, pygame, math

class UIManager():
    def __init__(self):
        self.mainDisplay = pygame.image.load("Images/Other/UIElements/UIStatsDisplay.png")
        self.MDRect = self.mainDisplay.get_rect()


    def drawElements(self, screen):
        screen.blit(self.mainDisplay, self.MDRect)
