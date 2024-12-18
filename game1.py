import pygame 
pygame.init()
display_surface = pygame.display.set_mode((750,500))
display_surface.set_caption("adding random word to fill up space")

background_image=pygame.transform.scale(pygame.image.load("by.jpg"))

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
        display_surface.blit(background_image(0,0))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__" :
    game_loop()





    
    
    