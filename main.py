import sys, pygame, math

from Player import *
from UIManager import *


mult = 1
mult2 = 1
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
#UIManager.MBRect = UIManager.MBRect.move(UIManager.MBPose)
#UIManager.HBRect = UIManager.HBRect.move(UIManager.HBPose)
while True:
    #if player.health <= 2:
    #    mult *= -1
    #if player.health >= player.maxHealth:
    #    mult *= -1
    #if player.mana <= 2:
    #    mult2 *= -1
    #if player.mana >= player.maxMana:
    #    mult2 *= -1
    #player.health = player.health + mult
    #player.mana = player.mana + mult2
    #Handles Key Presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
                #Detects keys presses
        if event.type == pygame.KEYDOWN:
            #Sets y direction
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                pass
                #player.go("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pass
                #player.go("down")
            #Sets x direction
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
                
            #Other Key events:
            if event.key == pygame.K_p:
                player.health = player.health + 5
            if event.key == pygame.K_l:
                player.health = player.health - 5
            
        #Detects Key Releases
        if event.type == pygame.KEYUP:
            #Stops y
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                pass
                #player.go("stop up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pass
                #player.go("stop down")
            #Stops x
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")

    #Move Stuff Here
    player.move()
    #Update things
    screen.fill(bgColor)
    
    UIManager.updateGlobes(player.health, player.maxHealth, player.mana, player.maxMana)
    #Blit other things here
    screen.blit(player.image, player.rect)
    UIManager.drawElements(screen)
    pygame.display.flip()
    clock.tick(60)
