import pygame
def main():
    pygame.init()
    screen_width,screen_height=500,500
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Mini sprite display')
    colours={
        "white":pygame.color("white"),
        "cyan":pygame.color("cyan"),
        "crimson":pygame.color("crimson"),
        "yellow":pygame.color("yellow"),
        "lavender":pygame.color("lavender")
    }
    current_colour=colours["white"]
    x,y=30,30
    width,height=65,65
    clock=pygame.time.clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        x = min(max(0, x), screen_width - width)
        y = min(max(0, y), screen_height - height)
                
                        # Change color based on boundary contact
        if x == 0: 
              current_colour = colours['cyan']
        elif x == screen_width - width: current_color = colours['yellow']
        elif y == 0: current_colour = colours['crimson']
        elif y == screen_height - height:
                            current_colour = colours['lavender']
        else:
            current_colour = colours['white']
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                                                     (x, y, width, height))
        pygame.display.flip()
        clock.tick(90)
                            
    pygame.quit()
                            
                            
if __name__ == "__main__":
 main()
                            
                            
                