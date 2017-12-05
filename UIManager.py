import sys, pygame, math

class UIManager():
    def __init__(self):
        #Creates primary UI Element
        self.mainDisplay = pygame.image.load("Images/Other/UIElements/UIStatsDisplay.png")
        self.MDRect = self.mainDisplay.get_rect()
        #Adds Boxes behind spheres
            #mana
        self.manaBox = pygame.image.load("Images/Other/UIElements/ManaBox.png")
        self.MBRect = self.manaBox.get_rect()
        self.MBPose = [725,19]
            #health
        self.healthBox = pygame.image.load("Images/Other/UIElements/HealthBox.png")
        self.HBRect = self.healthBox.get_rect()
        self.HBPose = [16,18]
    def drawElements(self, screen):
        #Move elements
        #self.MBRect = self.MBRect.move(self.MBPose)
        #Draw Elements
        screen.blit(self.manaBox, self.MBRect)
        screen.blit(self.healthBox, self.HBRect)
        
        screen.blit(self.mainDisplay, self.MDRect)
