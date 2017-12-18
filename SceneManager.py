import sys, pygame, math

from CreateImage import *

class SceneManager():
    def __init__(self):
        
        #Number list of scenes
        self.s1 = CreateImage(0,600, "test1", 
                            "Images/Other/Scenes/TestScene1.png")
        self.s2 = CreateImage(0,600, "test2", 
                            "Images/Other/Scenes/TestScene2.png")
        self.s3 = CreateImage(0,600, "test3", 
                            "Images/Other/Scenes/TestScene3.png")
        
        self.currentScene = self.s1
        
    def drawElements(self, screen, scene):
        screen.blit(scene.image, scene.rect)
        
    def changeScene(self, newScene):
        self.currentScene = newScene
