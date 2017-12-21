import sys, pygame, math


class Item():
    def __init__(self, name = "Unnamed", image = "Images/Other/Items/NoImage", description = "This is a description"):
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        #Stat Changes
        self.statList(
            maxHealth = 0,#1
            maxMana = 0,#2
            maxCorruption = 0,#3
            health = 0,#4
            mana = 0,#5
            speed = [0,0],#6
            maxSpeed = [0,0],#7
        #Corruption and armor
            corruption = 0,#8
            corruptionResistance = 0,#9
            armor = 0,#10
        #Xp vars
            lvl = 1,#11
            xp = 0,#12
            xpMult = 0,#13
        #Damage
            damage = 0,#14
            lifesteal = 0,#15
            attackSpeed = 0,#16
            cost = 0) #17

    def spawnRandom(self, type = "potion" ): None
