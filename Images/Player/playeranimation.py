import sys, pygame, math



class PlayerAnimation():
    def __init__(self, pos):
        self.rImage = [p.i.land("path/player"),
              [pygame.image.load("path/playeranimation1")],
              [pygame.image.load("path/playeranimation2")],
              [pygame.image.load("path/playeranimation1")],
              [pygame.image.load("path/playeranimation3")]]

        
        self.frame = 0
        self.maxframe = len((self.rImage)-1)
        self.image = self.rImage[self.frame]
        self.AnimationTimer = 0
        self.AnimationTimerMax = 60/10
        
    def animate(self):
        if AnimationTimer < AnimationTimerMax:
            AnimationTimer += 1
        else:
            AnimationTimer = 0
            if self.frame < self.maxframe:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.rImage[self.frame]
