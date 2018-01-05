import sys, pygame, math, random


class Item():
    def __init__(self, type = "item", subType = "universal", name = "Unnamed", description = "This is a description", image = "Images/Other/Items/NoImage.png", visable = False):
        self.name = name
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.visable = visable
        self.lvl = 1
        self.cost = 0
        self.type = type
        self.subType = subType
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
        
        
        self.stats = {
            "maxHealth": 0,
            "maxMana": 0,
            "maxCorruption":0,
            "speed":0,
            "maxSpeed":0,
            "corruptionResistance":0,
            "armor":0,
            "xpMult":0,
            "damage":0,
            "lifesteal":0,
            "attackspeed":0,
            "thorns":0,
            "goldChance":0,
            "corruption":0}
            
        
        #print self.stats.keys
    def randomizeStats(self,show = False, probability = False):
        for stat in self.stats:
            self.stats[stat] = 0
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
            balanceNeeded = 0
            val = 0
            statnumber = 0
            baseStatNum = 0
            if show:
                print "=== Item type:", self.type, "==="
            print "++++Randomize Stats Initiated++++"
            for stat in self.stats:
                perc = random.randint(1,100)
                baseStatNum = random.randint(1,10)
                if baseStatNum >= 8 and perc <= 15 and stat != "corruption":
                    balanceNeeded += 1
            #-----------------------------------------------
                if self.type == "item":
                    if perc > 15:
                        self.stats[stat] = 0
                    else:
                        val = baseStatNum*self.lvl
                        self.stats[stat] += val
            #-----------------------------------------------
                elif self.type == "weapon":
                    if stat == "armor" or stat == "thorns":
                        val = 0
                    elif perc > 15 and stat != "damage" :
                        self.stats[stat] = 0
                    else:
                        val = baseStatNum*self.lvl
                        self.stats[stat] += val
            #----------------------------------------------
                elif self.type == "armor":
                    if stat == "damage" or stat == "lifesteal" or stat == "attackspeed":
                        val = 0
                        #print "was big three"
                    elif perc > 15 and stat != "armor":
                        self.stats[stat] = 0
                        #print "unlucky"
                    else:
                        val = baseStatNum*self.lvl
                        self.stats[stat] += val
            #----------------------------------------------
                if stat == "corruption" and self.stats[stat] < balanceNeeded*self.lvl:
                    self.stats[stat] = balanceNeeded*self.lvl*3
                if show and self.stats[stat] != 0:
                    #print "++++Randomizing++++"
                    #print "                                  Corruption is:",self.stats["corruption"]
                    print stat,"is:", self.stats[stat]
                    if stat == "corruption":
                        pass
                    else:
                        statnumber += 1
            #---------------------------------------------
                if statnumber > 3:
                    balanceNeeded += 1
            print "^^^^Final Stat Count^^^^"
            print statnumber
            print "Balance Needed:",balanceNeeded
        
    def displayStats(self):
        print "===========Item Stats==========="
        for stat in self.statList:
            print stat
    def displayStat(self,number):
        print "===========Single Stat==========="
        print self.statList[number]
