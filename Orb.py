import pygame, sys, math

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 255, 255, 255
#Makes bounding box
base = pygame.Surface((110, 110))
baseR = base.get_rect(bottomleft = (200, 200))
#Color inside of bounding
filling = pygame.Surface((100, 100))
#fills color
filling.fill((255,0,0))

fillR = filling.get_rect(bottomleft = (5,105))#5,105
size = 100;
sizeD = -1

base.blit(filling, fillR);

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    bgColor = r,g,b
    
    size += sizeD
    
    filling = pygame.transform.scale(filling, [100, size])
    fillR = filling.get_rect(bottomleft = (5,105))
    base.fill((0,0,0))
    base.blit(filling, fillR);
    
    if size >= 100 or size <=20:
        sizeD *= -1
    
    screen.fill(bgColor)
    screen.blit(base, baseR)

    
    pygame.display.flip()
    clock.tick(60)
