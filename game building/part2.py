# import math
# import random
# import pygame 
# screen_height=500
# screen_width=800
# player_start_x=370
# player_start_y=380
# enemy_start_y_min=50
# enemy_start_y_max=200
# PLAYER_SIZE=(50,50)
# ENEMY_SIZE=(40,40)
# BULLET_SIZE=(16,32)
# ICON_SIZE=(32,32)
# ENEMY_SPEED_X=4
# ENEMY_SPEED_Y=40
# BULLET_SPEED_Y=10
# COLLISION_DISTANCE=(ENEMY_SIZE[0]//2)+(BULLET_SIZE[0]//2)
# pygame.init()
# screen=pygame.display.set_mode((screen_width,screen_height))
# background=pygame.image.load('background.jpg')
# pygame.display.set_caption("Space Invader")
# icon=pygame.image.load('spaceship.jpg')
# pygame.display.set_icon(icon)
# player_image=pygame.image.load('ship1.png')
# player_image=pygame.transform.scale(player_image,PLAYER_SIZE)
# playerx=player_start_x
# playery=player_start_y
# player_x_change=0
# enemy_image=[]
# enemy_x=[]
# enemy_y=[]
# enemy_x_change=[]
# enemy_y_change=[]
# num_of_enemies=7
# for i in range(num_of_enemies):
#     img=pygame.image.load('spaceship2.png')
#     img=pygame.transform.scale(img,ENEMY_SIZE)
#     enemy_image.append(img)
#     enemy_x.append(random.randint(0,screen_width-ENEMY_SIZE[0]))
#     enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
#     enemy_x_change.append(ENEMY_SPEED_X)
#     enemy_y_change.append(ENEMY_SPEED_Y)
# bullet_image=pygame.image.load('bullet.png')

# bullet_image=pygame.transform.scale(bullet_image,BULLET_SIZE)
# bullet_x=0
# bullet_y=player_start_y
# bullet_x_change=0
# bullet_y_change=BULLET_SPEED_Y
# bullet_state="ready"
# score_value=0
# font=pygame.font.Font('freesansbold.ttf',32)
# text_x=10
# text_y=10
# overfont=pygame.font.Font('freesansbold.ttf',64)
# def show_score(x,y):
#     score=font.render("score: "+str(score_value),True,(255,255,255))
#     screen.blit(score,(x,y))
# def game_over():
#     overtext=overfont.render("game over",True,(255,255,255))
#     screen.blit(overtext,(200,250))
# def player(x,y):
#     screen.blit(player_image,(x,y))
# def enemy(x,y,i):
#     screen.blit(enemy_image[i],(x,y))
# def bullet(x,y):
#     global bullet_state
#     bullet_state="fire"
#     offset_x=(PLAYER_SIZE[0]-BULLET_SIZE[0])//2
#     screen.blit(bullet_image,(x+offset_x,y-BULLET_SIZE[1]//2))
# def collision(enemy_x,enemy_y,bullet_x,bullet_y):
#     distance=math.sqrt((enemy_x-bullet_x)**2+(enemy_y-bullet_y)**2)
#     return distance<COLLISION_DISTANCE
# running=True 
# while running:
#     screen.fill((0,0,0))
#     screen.blit(background,(0,0))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_LEFT:
#                 player_x_change=-5
#             if event.key==pygame.K_RIGHT:
#                 player_x_change=5
#             if event.key==pygame.K_SPACE and bullet_state=="ready":
#                 bullet_x=playerx
#                 bullet(bullet_x,bullet_y)
#         if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
#             player_x_change=0
#         playerx+=player_x_change
#         playerx=max(0,min(playerx,screen_width-64))
#         for i in range(num_of_enemies):
#             if enemy_y[i]>340:
#                 for j in range(num_of_enemies):
#                     enemy_y[j]=2000
#                 game_over()
#                 break
#             enemy_x[i]+=enemy_x_change[i]
#             if enemy_x[i]<=0 or enemy_x[i]>=screen_width-64:
#                 enemy_x_change[i]*=-1
#                 enemy_y[i]+=enemy_y_change[i]
#             if collision(enemy_x[i],enemy_y[i],bullet_x,bullet_y):
#                 bullet_y=player_start_ybullet_state="ready"
#                 score_value+=1
#                 enemy_x[i]=random.randint(0,screen_width-64)
#                 enemy_y[i]=random.randint(enemy_start_y_min,enemy_start_y_max)
#             enemy(enemy_x[i],enemy_y[i],i)
#     if bullet_y<=0:
#         bullet_y=player_start_y
#         bullet_state="ready"
#     elif bullet_state=="fire":
#         bullet(bullet_x,bullet_y)
#         bullet_y=bullet_y_change
#     player(playerx,playery)
#     show_score(text_x,text_y)
#     pygame.display.update()
   
            
    
# import math
# import random
# import pygame

# # Constants
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 500
# PLAYER_START_X = 370
# PLAYER_START_Y = 380
# ENEMY_START_Y_MIN = 50
# ENEMY_START_Y_MAX = 150
# ENEMY_SPEED_X = 4
# ENEMY_SPEED_Y = 40
# BULLET_SPEED_Y = 10
# COLLISION_DISTANCE = 27

# # Initialize Pygame
# pygame.init()

# # Create the screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # Background
# background = pygame.image.load('background.jpg')

# # Caption and Icon
# pygame.display.set_caption("Space Invader")
# icon = pygame.image.load('spaceship.jpg')
# pygame.display.set_icon(icon)

# # Player
# playerImg = pygame.image.load('ship1.png')
# playerX = PLAYER_START_X
# playerY = PLAYER_START_Y
# playerX_change = 0

# # Enemy
# enemyImg = []
# enemyX = []
# enemyY = []
# enemyX_change = []
# enemyY_change = []
# num_of_enemies = 6

# for _i in range(num_of_enemies):
#     enemyImg.append(pygame.image.load('spaceship2.png'))
#     enemyX.append(random.randint(0, SCREEN_WIDTH - 100))  # 64 is the size of the enemy
#     enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
#     enemyX_change.append(ENEMY_SPEED_X)
#     enemyY_change.append(ENEMY_SPEED_Y)

# # Bullet
# bulletImg = pygame.image.load('bullet.png')
# bulletX = 0
# bulletY = PLAYER_START_Y
# bulletX_change = 0
# bulletY_change = BULLET_SPEED_Y
# bullet_state = "ready"

# # Score
# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 10
# textY = 10

# # Game Over Text
# over_font = pygame.font.Font('freesansbold.ttf', 64)

# def show_score(x, y):
#     # Display the current score on the screen.
#     score = font.render("Score : " + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))

# def game_over_text():
#     # Display the game over text
#     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
#     screen.blit(over_text, (200, 250))

# def player(x, y):
#     # Draw the player on the screen
#     screen.blit(playerImg, (x, y))

# def enemy(x, y, i):
#     # Draw an enemy on the screen
#     screen.blit(enemyImg[i], (x, y))

# def fire_bullet(x, y):
#     # Fire a bullet from the player's position
#     global bullet_state
#     bullet_state = "fire"
#     screen.blit(bulletImg, (x + 16, y + 10))

# def isCollision(enemyX, enemyY, bulletX, bulletY):
#     # Check if there is a collision between the enemy and a bullet
#     distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
#     return distance < COLLISION_DISTANCE

# #Game loop
# running = True
# while running:
#     screen.fill((0, 0, 0))
#     screen.blit(background, (0, 0))

#     for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#           running = False
#       if event.type == pygame.KEYDOWN:
#           if event.key == pygame.K_LEFT:
#               playerX_change = -5
#           if event.key == pygame.K_RIGHT:
#               playerX_change = 5
#           if event.key == pygame.K_SPACE and bullet_state == "ready":
#               bulletX = playerX
#               fire_bullet(bulletX, bulletY)
#       if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#           playerX_change = 0

#     # Player Movement
#     playerX += playerX_change
#     playerX = max(0, min(playerX, SCREEN_WIDTH - 10))  # 64 is the size of the player

#     # Enemy Movement
#     for i in range(num_of_enemies):
#         if enemyY[i] > 340:  # Game Over Condition
#             for j in range(num_of_enemies):
#                 enemyY[j] = 2000
#             game_over_text()
#             break

#         enemyX[i] += enemyX_change[i]
#         if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
#             enemyX_change[i] *= -1
#             enemyY[i] += enemyY_change[i]

#         # Collision Check
#         if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
#             bulletY = PLAYER_START_Y
#             bullet_state = "ready"
#             score_value += 1
#             enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
#             enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

#         enemy(enemyX[i], enemyY[i], i)

#     # Bullet Movement
#     if bulletY <= 0:
#         bulletY = PLAYER_START_Y
#         bullet_state = "ready"
#     elif bullet_state == "fire":
#         fire_bullet(bulletX, bulletY)
#         bulletY -= bulletY_change

#     player(playerX, playerY)
#     show_score(textX, textY)
#     pygame.display.update()

import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Sprite sizes (width, height) — tweak these to taste
PLAYER_SIZE = (50, 50)
ENEMY_SIZE = (40, 40)
BULLET_SIZE = (16, 32)
ICON_SIZE = (32, 32)

PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 200
ENEMY_SPEED_X = 2
ENEMY_SPEED_Y = 20
BULLET_SPEED_Y = 6
PLAYER_SPEED = 4
FPS = 60

# Collision distance should roughly match half the enemy size + half the bullet size
COLLISION_DISTANCE = (ENEMY_SIZE[0] // 2) + (BULLET_SIZE[0] // 2)

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock to control frame rate (this is what actually controls game speed)
clock = pygame.time.Clock()

# Background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.jpg')
icon = pygame.transform.scale(icon, ICON_SIZE)
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ship1.png')
playerImg = pygame.transform.scale(playerImg, PLAYER_SIZE)
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    img = pygame.image.load('spaceship2.png')
    img = pygame.transform.scale(img, ENEMY_SIZE)
    enemyImg.append(img)
    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0]))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, BULLET_SIZE)
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    # Fire a bullet from the player's position, centered on the player sprite
    global bullet_state
    bullet_state = "fire"
    offset_x = (PLAYER_SIZE[0] - BULLET_SIZE[0]) // 2
    screen.blit(bulletImg, (x + offset_x, y - BULLET_SIZE[1] // 2))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

#Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -PLAYER_SPEED
          if event.key == pygame.K_RIGHT:
              playerX_change = PLAYER_SPEED
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
          playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_SIZE[0]))

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_SIZE[0]:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0])
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    clock.tick(FPS)  # caps the loop at FPS iterations/sec — this is what fixes the speed