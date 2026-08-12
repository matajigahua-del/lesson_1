import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Smart Traffic Control Stimulator")
clock=pygame.time.clock()
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((80,40))
        self.image.fill("blue")
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=350
        self.velocity=3
        def update(self):
            self.rect.x+=self.velocity

car=Car()
car_group=pygame.sprite.Group()
car_group.add(car)
signal="RED"
CHANGE_SIGNAL=pygame.USEREVENT+1
pygame.event.post=(pygame.event.Event(CHANGE_SIGNAL))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            if event.type==CHANGE_SIGNAL:
                if signal=="RED":
                    signal=="GREEN"
                    car.image.fill("green")
                else:
                    signal="RED"
                    car.image.fill("blue")
                    car_group.update()
                if car.rect.right>=700:
                    car.rect.x=100
                    pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))
                screen.fill("lightblue")
                pygame.draw.rect(screen,"gray",(0,300,800,150))
                for x in range(0,800,80):
                    pygame.draw.rect(screen,"white",(x,370,40,5))
                pygame.draw.rect(screen,"black",(650,50,80,200))
                if signal=="RED":
                    pygame.draw.circle(screen,"'red",(690,100,25))
                else:
                     pygame.draw.circle(screen,"'darkred",(690,100,25))
                if signal=="GREEN":
                    pygame.draw.circle(screen,"'green",(690,200,25))
                
                else:
                     pygame.draw.circle(screen,"'darkgreen",(690,200,25))
                car_group.draw(screen)
                pygame.display.flip()
                clock.tick(60)
        pygame.quit()
        sys.exit()


                   