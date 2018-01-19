import sys, pygame, math, random


class TextManager():
    def __init__(self,screen, scene):
        self.scene = scene
        self.screen = screen
        
    def creatText(self,text = "text",position = [0,0]):
        text = font.render("text", 1, (10,10,10))
        textpos = text.get_rect()
        screen.blit(text, textpos)
