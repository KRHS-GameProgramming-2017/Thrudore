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
        self.maxHealth = 100#1
        self.maxMana = 100#2
        self.maxCorruption = 100#3
        self.health = 100#4
        self.mana = 100#5
        self.speed = [x,y] = [0,0]#6
        self.maxSpeed = [xm,ym] = [3,0]#7
        #Corruption and armor
        self.corruption = 100#8
        self.corruptionResistance = 0#9
        self.armor = 0#10
        #Xp vars
        self.lvl = 1
        self.xpToNextLvl = 100
        self.xp = 0#11
        self.xpMult = 0#12
        #Damage
        self.damage = 2#13
        self.lifesteal = 0#14
        self.attackSpeed = 1.0#15
        self.gold = 0#16
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
        elif movement == "stop right":
            if self.facing == "right":
                self.speed[0] = 0
        elif movement == "stop left":
            if self.facing == "left":
                self.speed[0] = 0

    def alterStat(self, stat, amount):
        self.stat += amount
    
    
    
    
    
    
    
    
    
