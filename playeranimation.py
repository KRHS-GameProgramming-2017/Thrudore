import sys, pygame, math


class PlayerAnimation():
    def __init__(self, pos):
        self.rImages = [pygame.image.load("Images/Player/0playeranimation0.png"),
                        pygame.image.load("Images/Player/1playeranimation1.png"),
                        pygame.image.load("Images/Player/2playeranimation2.png"),
                        pygame.image.load("Images/Player/1playeranimation1.png"),
                        pygame.image.load("Images/Player/3playeranimation3.png")]
                        
        #self.lImages = [pygame.image.load("Images/Player/4playeranimation4.png"),
        #                pygame.image.load("Images/Player/5playeranimation5.png"),
        #                pygame.image.load("Images/Player/6playeranimation6.png"),
        #                pygame.image.load("Images/Player/5playeranimation5.png"),
        #                pygame.image.load("Images/Player/7playeranimation7.png")]

        self.frame = 0
        self.maxframe = len(self.rImages)-1
        self.image = self.rImages[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.AnimationTimer = 0
        self.AnimationTimerMax = 30/10
    
    
    def animate(self):
        if self.AnimationTimer < self.AnimationTimerMax:
            self.AnimationTimer += 1
        else:
            self.AnimationTimer = 0
            if self.frame < self.maxframe:
                self.frame += 1
            else:
                self.frame = 0
            #if self.facing == "right":
            self.image = self.rImages[self.frame]
