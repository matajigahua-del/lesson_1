import math
import random
import pygame 
screen_height=500
screen_width=800
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
PLAYER_SIZE=(50,50)
ENEMY_SIZE=(40,40)
BULLET_SIZE=(16,32)
ICON_SIZE=(32,32)
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load('background.jpg')
pygame.display.set_caption("Space Invader")
icon=pygame.image.load('spaceship.jpg')
pygame.display.set_icon(icon)
player_image=pygame.image.load('ship1')
playerx=player_start_x
playery=player_start_y
player_x_change=0
enemy_image=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemies=7
for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('spaceship2'))
    enemy_x.append(random.randint(0,screen_width-ENEMY_SIZE[0]))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)
bullet_image=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=player_start_y
bullet_x_change=0
bullet_y_change=BULLET_SPEED_Y
bullet_state="ready"
score=0
font=pygame.font.Font('freesansbold.ttf',32)
text_x=10
text_y=10
overfont=pygame.font.Font('freesansbold',64)
def show_score(x,y):
    score=font.render("score: "+str(score),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over():
    overtext=overfont.render("game over",True,(255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(player_image,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_image,(x+16,y+10))
def collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance=math.sqrt((enemy_x-bullet_x)**2+(enemy_y-bullet_y)**2)
    return distance<COLLISION_DISTANCE
running=True 
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_x_change=-5
            if event.key==pygame.K_RIGHT:
                player_x_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bullet_x=playerx
                bullet(bullet_x,bullet_y)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            player_x_change=0
        playerx+=player_x_change
        playerx=max(0,min(playerx,screen_width-64))
        for i in range(num_of_enemies):
            if enemy_y[i]>340:
                for j in range(num_of_enemies):
                    enemy_y[j]=2000
                game_over()
                break
            enemy_x[i]+=enemy_x_change[i]
            if enemy_x[i]<=0 or enemy_x[i]>=screen_width-64:
                enemy_x_change[i]*=-1
                enemy_y[i]+=enemy_y_change[i]
       
        
