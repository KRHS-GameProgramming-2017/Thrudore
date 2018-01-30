import sys, pygame, math

from Player import *
from UIManager import *
from SceneManager import *
from Item import *
from TextManager import *
from playeranimation import *
from Text import *

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


font = pygame.font.Font(None,36)


player = Player([width/2, height-150])
UIManager = UIManager()
SceneManager = SceneManager()


scene = None
testItem = Item()
testItem = Item("weapon")
TextManager = TextManager(screen, scene)

newText = Text("Testing", [20,20])

p = PlayerAnimation([width/2, height/2])

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
               SceneManager.changeScene(SceneManager.s2)
                #pass
                #player.go("up")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                SceneManager.changeScene(SceneManager.startRoom)
                #pass
                #player.go("down")
            #Sets x directionZ
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
            #Inventory Activation
            if event.key == pygame.K_TAB:
                if scene == SceneManager.inventory and event.key == pygame.K_TAB:
                    SceneManager.changeScene(lastScene)
                else:
                    lastScene = scene
                    SceneManager.changeScene(SceneManager.inventory)
            
                
                
            #Other Key events:
            if event.key == pygame.K_p:
                player.health = player.health + 5
            if event.key == pygame.K_l:
                player.health = player.health - 5
            
            
            if event.key == pygame.K_z:
                testItem.randomizeStats(True)
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
    #screen.fill(bgColor)
    p.animate()
    
    if SceneManager.currentScene == SceneManager.inventory:
        pass
    else:
        UIManager.updateGlobes(player.health, 
                               player.maxHealth, 
                               player.mana, 
                               player.maxMana)
        #Blit other things here
        #Blit Scene then UI then player
    #------------------------------------------------------
    if SceneManager.currentScene != scene:
        scene = SceneManager.currentScene
        SceneManager.drawElements(screen, scene)
        print "The scene has changed to: " + scene.name
    else:
        SceneManager.drawElements(screen, scene)
    #-----------------------------------------------------
    if SceneManager.currentScene == SceneManager.inventory:
        screen.blit(newText.words, newText.textpos)
    else:
        if (UIManager.playerRecordedHealth != player.health or 
            UIManager.playerRecordedMana != player.mana):
                UIManager.drawElements(screen)
        #Font Test Stuff Here
        
        
        text = font.render("Thrudore", 1, (137,171,0))#89AB00 = the green for fonts
        textpos = text.get_rect()
        screen.blit(text, textpos)
        screen.blit(p.image, p.rect)
        screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
