import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('arcade-game.png')
player_X_coordinates = 360
player_Y_coordinates = 490

def player():
    screen.blit(player_image, (player_X_coordinates, player_Y_coordinates))
    
#Title and Icon
pygame.display.set_caption("Space Invaders")
# Game Loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB - Red, Green, Blue
    screen.fill((0,0,0))
    pygame.display.update()
    