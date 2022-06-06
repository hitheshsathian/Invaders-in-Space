import pygame
from pygame import mixer
import random
import math


#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('space_background.png')

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Player
player_image = pygame.image.load('arcade-game.png')
player_X_coordinates = 370
player_Y_coordinates = 480

playerX_change = 0
playerY_change = 0

# Enemy
enemy_image = []
enemy_X_coordinates = []
enemy_Y_coordinates =[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 12
for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('alien.png'))
    enemy_X_coordinates.append(random.randint(0,735))
    enemy_Y_coordinates.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(20)

# Bullet

bullet_image = pygame.image.load('bullet.png')
bullet_X_coordinates = 0
bullet_Y_coordinates = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('Starborn.ttf', 27)

textX = 10
textY = 10

#Game Over
over_font = pygame.font.Font('Starborn.ttf', 64)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (160,250))

def player(x,y):
    screen.blit(player_image, (x, y))

def enemy(x,y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+2,y+1))

def collision(enemy_X_coordinates, enemy_Y_coordinates, bullet_X_coordinates, bullet_Y_coordinates):
    distance = math.sqrt(math.pow(enemy_X_coordinates-bullet_X_coordinates,2) + math.pow(enemy_Y_coordinates-bullet_Y_coordinates,2))
    if distance < 27:
        return True
    return False
    
#Title and Icon
pygame.display.set_caption("Space Invaders")
# Game Loop
running = True 
while running:
    #RGB - Red, Green, Blue
    #Screen drawn
    screen.fill((0,0,0))
    #Background Image
    screen.blit(background, (0,0))
    #player_X_coordinates += 0.1
    #print(player_X_coordinates)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if key pressed check if right or left
        if event.type == pygame.KEYDOWN:
            print("Key is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet_X_coordinates = player_X_coordinates
                    fire_bullet(player_X_coordinates, bullet_Y_coordinates)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key had been released")
                playerX_change = 0

# Prevention of out-of-bounds for player
    player_X_coordinates += playerX_change

    if player_X_coordinates <= 0:
        player_X_coordinates = 0
    elif player_X_coordinates >= 736:
        player_X_coordinates = 736

#Enemy movement
    for i in range (num_of_enemies):

        #Game Over
        if enemy_Y_coordinates[i] > 440:
            for j in range(num_of_enemies):
                enemy_Y_coordinates[j] = 2000
            game_over()
            break


        enemy_X_coordinates[i] += enemyX_change[i]
        if enemy_X_coordinates[i] <= 0:
            enemyX_change[i] = 0.8
            enemy_Y_coordinates[i] += enemyY_change[i]
        elif enemy_X_coordinates[i] >= 736:
            enemyX_change[i] = -0.8
            enemy_Y_coordinates[i] += enemyY_change[i]

        #Collision 
        a_collision = collision(enemy_X_coordinates[i], enemy_Y_coordinates[i], bullet_X_coordinates, bullet_Y_coordinates)
        if a_collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bullet_Y_coordinates = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemy_X_coordinates[i] = random.randint(0,735)
            enemy_Y_coordinates[i] = random.randint(50,150)
        enemy(enemy_X_coordinates[i], enemy_Y_coordinates[i],i)

#Bullet movement
    if bullet_Y_coordinates <= 0:
        bullet_Y_coordinates = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet_X_coordinates, bullet_Y_coordinates)
        bullet_Y_coordinates -= bulletY_change


    player(player_X_coordinates, player_Y_coordinates)
    show_score(textX,textY)
    pygame.display.update()
     