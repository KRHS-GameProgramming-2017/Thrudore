import sys, pygame, math

class Player:
    def __init__(self, rImage, lImage):
        self.rImage = pygame.load.image(rImage)
        self.lImage = pygame.load.image(lImage)
        
        #Stats
        self.maxHealth = 100
        self.maxMana = 100
        self.maxCorruption = 100
        self.health = 100
        self.mana = 100
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
        self.gold = 0
        #20 total inventory slots
        self.inventory[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        
