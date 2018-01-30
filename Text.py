import sys, pygame, math

from CreateImage import *

class Text():
    def __init__(self,text = "text",position = [0,0], color = [137,171,0]):
        self.font = pygame.font.Font(None,36)
        self.words = self.font.render(text, 1, color)
        self.textpos = self.words.get_rect()


