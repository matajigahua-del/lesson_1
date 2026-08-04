import pygame
# Basics of game building:

# Drawing a rectangle using pygame.Rect: It combines four values, left, right,top and width into a singular area.
# Example:

# pygame.init()
# screen=pygame.display.set_mode((400,300))
# done=False
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#     pygame.draw.rect(screen,(0,125,255),pygame.Rect(67,7,67,7))

#     pygame.display.flip()


# Solid shapes and Outlines Shapes: Using pygame.draw shape function accepts an extra width argument that decides whether the shape will be hollow or solid.

# pygame.init()
# screen=pygame.display.set_mode((400,300))
# lavendar=(0,255,0)
# done=False
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done=True
#     pygame.draw.circle(screen,(255,0,0),(150,150),50) # Solid Circle
#     pygame.draw.circle(screen,(0,255,0),(100,100),50,6) # Outlined Circle

#     pygame.display.flip()

# Moving a sprite using arrow keys: pygame.key.get_pressed() 

# Example:

def main():
    pygame.init()
    screen_width,screen_height=500,500
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Change color of square using arrow keys.')

    colors={
        'crimson':pygame.Color('crimson'),
        'white':pygame.Color('white'),
        'cyan':pygame.Color('cyan'),
        'lavender':pygame.Color('lavender'),
        'yellow':pygame.Color('yellow')
    }
    current_color=colors['white']

    x,y=30,30
    height,width=60,60

    clock=pygame.time.Clock()
    done=False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - width)
        y = min(max(0, y), screen_height - height)

        # Change color based on boundary contact
        if x == 0: current_color = colors['cyan']
        elif x == screen_width - width: current_color = colors['yellow']
        elif y == 0: current_color = colors['crimson']
        elif y == screen_height - height:
            current_color = colors['lavender']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, width, height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()

