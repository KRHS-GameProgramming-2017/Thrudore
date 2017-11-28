import sys, pygame, math

class Player():
    def __init__(self, pos):
        self.rImage = pygame.image.load("Images\Player\StickFigure\LPlayerPlaceHolder.png")
        self.rImage = pygame.transform.scale(self.rImage,[80,240])
        self.lImage = pygame.image.load("Images\Player\StickFigure\RPlayerPlaceHolder.png")
        self.lImage = pygame.transform.scale(self.lImage,[80,240])
        self.facing = "right"
        self.image = self.rImage
        self.rect = self.image.get_rect(center = pos)
        
        #Stats
        self.maxHealth = 100
        self.maxMana = 100
        self.maxCorruption = 100
        self.health = 100
        self.mana = 100
        self.speed = [x,y] = [4,0]
        #Corruption and armor
        self.corruption = 100
        self.corruptionResistance = 0
        self.armor = 0
        #Xp vars
        self.lvl = 1
        self.xpToNextLvl = 100
        self.xp = 0
        self.xpMult = 0
        #Damage
        self.damage = 2
        self.lifesteal = 0
        self.attackSpeed = 1.0
        self.gold = 0
        #20 total inventory slots
        self.inventory = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #Other things that are not stat related
        
        
        
    #def move(self, speed):
        #self.rect.move(speed)
        
    def go(self, movement):
        if movement == "right":
            #move(self.speed)
            self.rect.move(self.speed)
            print "Moved Right"
        elif movement == "left":
            #move(self.speed[0]*-1)
            self.rect.move(self.speed)
            print "Moved Left"
    
    
    
    
    
    
    
    
    
