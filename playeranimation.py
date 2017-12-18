import sys, pygame, math
from main import *
from Player import *


class PlayerAnimation():
    def __init__(self, pos):
        self.rImage = [p.i.land("path/player"),
              [p.i.land("path/playeranimation1"),
              [p.i.land("path/playeranimation2"),
              [p.i.land("path/playeranimation1"),
              [p.i.land("path/playeranimation3")]

    self.frame = 0
    self.maxframe = len(self.rImage)-1)
    self.image = self.rImage[self.frame]
    self.AnimationTimer = 0
    self.AnimationTimerMax = 30/10
        if AnimationTimer < AnimationTimerMax:
            AnimationTimer += 1
        else
            AnimationTimer = 0
            if self.frame < self.maxframe
                self.frame += 1
        self.image = self.rImage[self.frame]
