import sys, pygame, math


class Item():
    def __init__(self, name = "Unnamed", image = "Images/Other/Items/NoImage", description = "This is a description", visable = False):
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.visable = visable
        #Stat Changes
        self.statList(
            maxHealth = 0,#0
            maxMana = 0,#1
            maxCorruption = 0,#2
            health = 0,#3
            mana = 0,#4
            speed = [0,0],#5
            maxSpeed = [0,0],#6
        #Corruption and armor
            corruption = 0,#7
            corruptionResistance = 0,#8
            armor = 0,#9
        #Xp vars
            lvl = 1,#10
            xp = 0,#11
            xpMult = 0,#12
        #Damage
            damage = 0,#13
            lifesteal = 0,#14
            attackSpeed = 0,#15
            cost = 0, #16
        #Other
            duration = 0) #17

    def randomizeStats():
        for stat in statList:
