import sys, pygame, math, random


class Item():
    def __init__(self, name = "Unnamed", image = "Images/Other/Items/NoImage.png", description = "This is a description", visable = False):
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.visable = visable
        self.lvl = 1
        self.cost = 0
        #Stat Changes
        self.statList = [
            0,#0 maxHealth
            0,#1 maxMana
            0,#2 maxCorruption
            0,#3 speed
            0,#4 maxSpeed
        #Corruption and armor
            0,#5 corruption
            0,#6 corruptionResistance
            0,#7 armor
        #Xp vars
            0,#8 xpMult
        #Damage
            0,#9 damage
            0,#10 lifesteal
            0]#11 attackspeed

    def randomizeStats(self,show = False, probability = False):
        
        if probability == True:
            print "vvv:Probability Active:vvv"
            numOfStats = 0
            probabilityOfStat = 0.0
            spawn = 1000
            totalTrials = 0
            numberTracker = [0,0,0,0,0,0,0,0,0,0,0,0]
            while spawn > 0:
                statnumber = 0
                id = 0
                for stat in self.statList:
                    stat = random.randint(0,100)
                    if stat > 15:
                        stat = 0
                    elif stat <= 14:
                        stat = 1
                    if stat != 0:
                        statnumber += 1
                        numberTracker[id] += 1
                    id += 1
                spawn -=1
                numOfStats += statnumber
                totalTrials += 12
            #Results -----------------------------------------------
            print numOfStats
            print "------"
            print totalTrials
            probabilityOfStat = float(numOfStats)/float(totalTrials)
            print "+++Number of stats per each 12 trials per item+++"
            tag = 0
            yesTotal = 0
            addativeProb = 0.0
            for num in numberTracker:
                if tag < 10:
                    print tag, "  = ", num, "    Prob. = ", (float(num)/float(totalTrials))/probabilityOfStat
                else:
                    print tag, " = ", num, "    Prob. = ", (float(num)/float(totalTrials))/probabilityOfStat
                addativeProb +=(float(num)/float(totalTrials))/probabilityOfStat
                tag += 1
                yesTotal += num
            print "~~~~~~~~~~~~~~~~~~~~~"
            print "Total = ", yesTotal, "   Average Prob. = ", addativeProb/12
            print "Probability of stat: ", probabilityOfStat
            print "^^^^^Results^^^^^"
            
        else:
            id = 0
            statnumber = 0
            print "++++Randomize Stats Initiated++++"
            for stat in self.statList:
                stat = random.randint(0,100)
                if stat > 15:
                    stat = 0
                elif stat <= 14:
                    stat = random.randint(1,10)*self.lvl
                self.statList[id] = stat
                if show and stat != 0:
                    print "++++Randomizing++++"
                    print id, " is: ", stat
                id += 1
                if stat != 0:
                    statnumber += 1
            print "^^^^Final Stat Count^^^^"
            print statnumber
        
    def displayStats(self):
        print "===========Item Stats==========="
        for stat in self.statList:
            print stat
    def displayStat(self,number):
        print "===========Single Stat==========="
        print self.statList[number]
