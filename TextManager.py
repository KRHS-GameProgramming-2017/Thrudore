import sys, pygame, math, random


class TextManager():
    def __init__(self,screen, scene):
        self.scene = scene
        self.screen = screen
        self.font = pygame.font.Font(None,36)
        
    def creatText(self,text = "text",position = [0,0], color = [137,171,0]):
        words = self.font.render(text, 1, color)
        textpos = words.get_rect()
        #screen.blit(text, textpos)
    def inventoryLayout(self):
        self.creatText()

