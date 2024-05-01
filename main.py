import pygame
import pygame_gui
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("eternal empire")
manager=pygame_gui.UIManager ((640 , 480))
start=pygame_gui.elements.UIButton(pygame.Rect((350, 275), (100,50)),'hi', manager)

running = True

screen.fill((255, 0, 0))
deadeye_1=pygame.image.load('sprites/deadeye_1.png')
scaleddeadeye_1=pygame.transform.scale(deadeye_1,(100, 100))
zombobie_1=pygame.image.load('sprites/zombobie_1.png')
scaledzombobie_1=pygame.transform.scale(zombobie_1, (90, 90))
x=0
y=0
direction=1
font=pygame.font.Font(None, 60)
text=font.render('deadeye s place', True, (0, 0 ,0))

while running:
    screen.fill((55, 18, 140))
    screen.blit(text,(3 , 3))
    screen.blit(scaleddeadeye_1,(x + 50, y + 50))
    screen.blit(scaledzombobie_1,(x+ 400, y + 50))
    manager.draw_ui(screen)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            mods=pygame.key.get_mods()
            if event.key==pygame.K_z:
                pygame.quit()
                running = False
            # if  event.key==pygame.K_s:
            #     y=y+7
            # if event.key==pygame.K_w:
            #     y=y-7
            # if event.key==pygame.K_d:
            #     x=x+7
            # if event.key==pygame.K_a:
            #     x=x-7

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y=y-0.07
    if keys[pygame.K_s]:
        y=y+0.07
    if keys[pygame.K_d]:
        x=x+0.07
    if keys[pygame.K_a]:
        x=x-0.07