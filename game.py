import pygame  
pygame.init()

pygame.display.set_mode((750,500))
done = False

while not done :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

pygame.display.flip()