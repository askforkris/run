import pygame
import random

pygame.init()
FPS = 60
screen = pygame.display.set_mode((680, 480))
# initializing RGB color
color = (255, 255, 255, 0.0)
# changing surface color
screen.fill(color)
pygame.display.flip()
pygame.display.set_caption('Treasure_chest')
# initializing surface image
pygame.init()
imp = pygame.image.load('images/olchest.png').convert()
gem5 = pygame.image.load('images/gem5.png').convert()
gem4 = pygame.image.load("images/gem4.png").convert()

screen.blit(gem5, (20, 30))
screen.blit(imp, (226, 160))
screen.blit(gem4, (100, 30))
pygame.display.flip()

# paint screen one time
pygame.display.flip()
pygame.init()
# initializing exit
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.init()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y positions of the mouse click
            x, y = event.pos
            if gem5.get_rect().collidepoint(20, 30):
                print(random.randint(0, 9, ))
                # Initializing mouse click for gold star
            if event.type == pygame.MOUSEBUTTONUP:
                # Set the x, y  positions of the mouse click
                x, y = event.pos
                if gem4.get_rect().collidepoint(80, 20):
                    print(random.randint(25, 30))

                pygame.quit()
