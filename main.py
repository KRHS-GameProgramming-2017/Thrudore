import sys, pygame, math

from Player import *
from UIManager import *



#Inital stuff
pygame.init()
clock = pygame.time.Clock()
width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0, 0, 0

player = Player([width/2, height-150])
UIManager = UIManager()

#Move UI Elements
UIManager.MBRect = UIManager.MBRect.move(UIManager.MBPose)
UIManager.HBRect = UIManager.HBRect.move(UIManager.HBPose)
while True:
    
    #Handles Key Presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
                #Detects keys presses
        if event.type == pygame.KEYDOWN:
            #Sets y direction
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                None
                #player.go("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                None
                #player.go("down")
            #Sets x direction
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
        #Detects Key Releases
        if event.type == pygame.KEYUP:
            #Stops y
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                None
                #player.go("stop up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                None
                #player.go("stop down")
            #Stops x
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop x")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop x")

    #Move Stuff Here
    player.move()
    
    
    screen.fill(bgColor)
    #Blit other things here
    screen.blit(player.image, player.rect)
    UIManager.drawElements(screen)
    pygame.display.flip()
    clock.tick(60)
