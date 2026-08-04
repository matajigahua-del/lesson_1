import pygame

# Pygame basic functions: 
# pygame.init() : used to initialise all of the required modules for pygame.
# pygame.display.set_mode((width,height)) : Used to  create a specific size window. Its like a canvas on which grapics are drawn.
# pygame.event.get(): Its used to clear the backlogs of events.
# pygame.QUIT : Its used when we click on the close button of the window. It's used to end the event.
# pygame.display.flip(): It used to make changes to the game screen so that they are visible.

pygame.init()
screen_height,screen_width=500,500   
screen=pygame.display.set_mode((screen_height,screen_width))

imae=pygame.transform.scale(pygame.image.load('67676776.webp').convert_alpha(),(200,200))
y=imae.get_rect(center=(screen_width//2,screen_height//2-30))

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




# import pygame

# # Initialize Pygame and screen dimensions
# pygame.init()
# SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# # Initialize display surface and set title
# display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Adding image and background image')

# Load and scale images directly
# # background_image = pygame.transform.scale(
# #     pygame.image.load('background.png').convert(),
# #     (SCREEN_WIDTH, SCREEN_HEIGHT))

# penguin_image = pygame.transform.scale(
#     pygame.image.load('67676776.webp').convert_alpha(), (200, 200))
# penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2,
#     SCREEN_HEIGHT // 2 - 30))

# # # Initialize font, render text, and set text position
# # text = pygame.font.Font(None, 36).render('Hello World ', True,
# #     pygame.Color('black'))
# # text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

# def game_loop():
#     # clock = pygame.time.Clock()
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         display_surface.blit(penguin_image, penguin_rect)
#         # display_surface.blit(text, text_rect)

#         pygame.display.flip()

#         # clock.tick(30)

#     pygame.quit()

# if __name__ == '__main__':
#     game_loop()