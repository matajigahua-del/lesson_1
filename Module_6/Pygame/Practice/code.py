import pygame
# pygame.display.set_mode(("width,height"))
# pygame.event.get()
# pygame.QUIT
# pygame.display.flip()

pygame.init()
screen_width,screen_height=667,800
screen=pygame.display.set_mode(("screen_width,screen_height"))
imae=pygame.transform.scale(pygame.image.load('67676776.webp').convert_alpha(),(200,200))
y=imae.rect(centre= (screen_width//2,screen_height//2-30))

def game_loop():
    done=True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=False
        screen.blit(imae,y)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__': 
    game_loop()
'crimson'pygame.Color('crimson')