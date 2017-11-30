import sys, pygame, math

class Player():
    def __init__(self, pos):
        self.rImage = pygame.image.load("Images/Player/Default/RPlayer.png")
        self.rImage = pygame.transform.scale(self.rImage,[110,240])
        self.lImage = pygame.image.load("Images/Player/Default/LPlayer.png")
        self.lImage = pygame.transform.scale(self.lImage,[110,240])
        self.facing = "right"
        self.image = self.rImage
        self.rect = self.image.get_rect(center = pos)
        
        #Stats
        self.maxHealth = 100
        self.maxMana = 100
        self.maxCorruption = 100
        self.health = 100
        self.mana = 100
        self.speed = [x,y] = [0,0]
        self.maxSpeed = [xm,ym] = [3,0]
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
        
        
    #Using the input in go, moves the player accordingly
    def move(self):
        self.rect = self.rect.move(self.speed)
    #Interprets input for the player
    def go(self, movement):
        if movement == "right":
            self.image = self.rImage
            self.facing = "right"
            self.speed[0] = self.maxSpeed[0]
            #print "Move Right"
        elif movement == "left":
            self.image = self.lImage
            self.facing = "left"
            self.speed[0] = -self.maxSpeed[0]
            #print "Moved Left"
        elif movement == "stop x":
            self.speed[0] = 0
    
    
    
    
    
    
    
    
    
