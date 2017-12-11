import sys, pygame, math

class UIManager():
    def __init__(self):
        #Creates primary UI Element
        self.mainDisplay = pygame.image.load("Images/Other/UIElements/UIStatsDisplay.png")
        self.MDRect = self.mainDisplay.get_rect()
        #Adds Boxes behind spheres
            #mana
        self.manaBoxImage = pygame.Surface((65,65))#pygame.image.load("Images/Other/UIElements/ManaBox.png")
        self.manaBoxImage.fill((0,0,255))
        self.MBRect = self.manaBoxImage.get_rect(bottomleft = (721,84))
            #health
        self.healthBoxImage = pygame.Surface((65, 65))#pygame.image.load("Images/Other/UIElements/HealthBox.png")
        self.healthBoxImage.fill((255,0,0))
        self.HBRect = self.healthBoxImage.get_rect(bottomleft = (17,84))
        
    def drawElements(self, screen):
        #Move elements
        #self.MBRect = self.MBRect.move(0,0)
        
        #Draw Elements
        screen.blit(self.manaBoxImage, self.MBRect)
        screen.blit(self.healthBoxImage, self.HBRect)
        screen.blit(self.mainDisplay, self.MDRect)
        
    def updateGlobes(self, health, maxHealth, mana, maxMana):
        healthPercent = int((float(health)/float(maxHealth))*65)
        manaPercent = int((float(mana)/float(maxMana))*65)
        self.healthBoxImage = pygame.transform.scale(self.healthBoxImage,[65,healthPercent])
        self.HBRect = self.healthBoxImage.get_rect(bottomleft = (17,84))
        self.manaBoxImage = pygame.transform.scale(self.manaBoxImage,[65,manaPercent])
        self.MBRect = self.manaBoxImage.get_rect(bottomleft = (721,84))
        #self.HBRect = self.healthBoxImage.get_rect(center = self.HBRect.bottomleft)
        #self.manaBoxImage = pygame.transform.scale(self.manaBoxImage,[65,manaPercent])
        
