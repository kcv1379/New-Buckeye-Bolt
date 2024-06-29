import pygame
import os

pygame.init()

# need to figure out how to add main function

# map of maze
# 0 = gray square, 1 = red square, 2 = small buckeye, 3 = big buckeye, 
# 4 = foodbot, 5 = enemy 1, 6 = enemy 2, 7 = enemy 3, 8 = enemy 4 9 = enemy door
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
       [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
       [1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 9, 1, 1, 2, 1, 2, 1],
       [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 1, 2, 1, 2, 1],
       [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 5, 6, 1, 2, 1, 2, 1],
       [0, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 7, 8, 1, 2, 1, 2, 0],
       [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# game images
SCARLET_SQUARE = pygame.image.load(os.path.join('assets','scarlet.png'))
SMALL_BUCKEYE = pygame.image.load(os.path.join('assets','smallbuckeye.png'))
BIG_BUCKEYE = pygame.image.load(os.path.join('assets','bigbuckeye.png'))
FOODBOT_LEFT = pygame.image.load(os.path.join('assets','foodbot.png'))
#ENEMY_1 = pygame.image.load(os.path.join('assets','enemy1.png'))
#ENEMY_2 = pygame.image.load(os.path.join('assets','enemy2.png'))
#ENEMY_3 = pygame.image.load(os.path.join('assets','enemy3.png'))
#ENEMY_4 = pygame.image.load(os.path.join('assets','enemy4.png'))
ENEMY_DOOR = pygame.image.load(os.path.join('assets','enemydoor.png'))

# displaying window that is 640 x 700
WIDTH = 640
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

# colors
GRAY = (167, 177, 183)

# display game name at top of window
pygame.display.set_caption("Buckeye Bolt")

# initial game settings
foodbot_x = 288
foodbot_y = 320
center_x = foodbot_x + 16
center_y = foodbot_y + 16
direction = 0
direction_c = 0
flicker = False
counter = 0
turns = [False, False, False, False]   
foodbot_speed = 2

# display window with main aspects
def window_display():
     WINDOW.fill(GRAY)

     for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                WINDOW.blit(SCARLET_SQUARE,(j * 32, i * 32))
            elif map[i][j] == 2:
                WINDOW.blit(SMALL_BUCKEYE,(j * 32, i * 32))
            elif map[i][j] == 3 and not flicker:
                WINDOW.blit(BIG_BUCKEYE,(j * 32, i * 32))
            elif map[i][j] == 4:
                WINDOW.blit(FOODBOT_LEFT,(j * 32, i * 32))
            #elif map[i][j] == 5:
                #WINDOW.blit(ENEMY_1,(j * 32, i * 32))
            #elif map[i][j] == 6:
                #WINDOW.blit(ENEMY_2,(j * 32, i * 32))
            #elif map[i][j] == 7:
                #WINDOW.blit(ENEMY_3,(j * 32, i * 32))
            #elif map[i][j] == 8:
                #WINDOW.blit(ENEMY_4,(j * 32, i * 32))
            elif map[i][j] == 9:
                WINDOW.blit(ENEMY_DOOR,(j * 32, i * 32))


#change foodbot direction facing based on movement
# 0 = left, 1 = right, 2 = up, 3 = down
def foodbot_display():
    if direction == 0:
        WINDOW.blit(FOODBOT_LEFT,(foodbot_x,foodbot_y))
    elif direction == 1:
        WINDOW.blit(pygame.transform.flip(FOODBOT_LEFT,True, False), (foodbot_x,foodbot_y))
    elif direction == 2:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 270), (foodbot_x,foodbot_y))
    elif direction == 3:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 90), (foodbot_x,foodbot_y))
    

# checking which directions foodbot is allowed to move based on position
def position_check(center_x,center_y):
    # 0 = left, 1 = right, 2 = up, 3 = down
    # if square ahead of foodbot is red,stop them from moving 
    #32, 15?
    turns = [False, False, False, False]
    if center_x // 32 < 19:
        # if i am moving right and 
        if direction == 1:
            if map[center_y // 20][(center_x) // 20] == 0:
                turns[0] = True  
            elif map[center_y // 20][(center_x) // 20] == 2:
                turns[0] = True  
            elif map[center_y // 20][(center_x) // 20] == 3:
                turns[0] = True  
        if direction == 0:
            if map[center_y // 20][(center_x) // 20] == 0:
                turns[1] = True  
            elif map[center_y // 20][(center_x) // 20] == 2:
                turns[1] = True  
            elif map[center_y // 20][(center_x) // 20] == 3:
                turns[1] = True  
        if direction == 2:
            if map[(center_y) // 32][center_x // 20] == 0:
                turns[3] = True  
            elif map[(center_y) // 32][center_x // 20] == 2:
                turns[3] = True  
            elif map[(center_y) // 32][center_x // 20] == 3:
                turns[3] = True  
        if direction == 3:
            if map[(center_y) // 32][center_x // 20] == 0:
                turns[2] = True  
            elif map[(center_y) // 32][center_x // 20] == 2:
                turns[2] = True  
            elif map[(center_y) // 32][center_x // 20] == 3:
                turns[2] = True  
        if direction == 2 or direction == 3:
            # if the x value is approximately at the midpoint of a square 
            if 7 <= center_x % 20 <= 13:
                if map[(center_y) // 32][center_x // 32] == 0:
                   turns[3] = True  
                elif map[(center_y) // 32][center_x // 32] == 2:
                   turns[3] = True  
                elif map[(center_y) // 32][center_x // 32] == 3:
                   turns[3] = True  
                if map[(center_y) // 32][center_x // 32] == 0:
                   turns[2] = True  
                elif map[(center_y) // 32][center_x // 32] == 2:
                   turns[2] = True  
                elif map[(center_y) // 32][center_x // 32] == 3:
                   turns[2] = True  
            if 7 <= center_y % 20 <= 13:
                if map[(center_y) // 32][(center_x - 32) // 32] == 0:
                   turns[0] = True  
                elif map[(center_y) // 32][(center_x - 32) // 32] == 2:
                   turns[0] = True  
                elif map[(center_y) // 32][(center_x - 32) // 32] == 3:
                   turns[0] = True  
                if map[(center_y) // 32][(center_x + 32) // 32] == 0:
                   turns[1] = True  
                elif map[(center_y) // 32][(center_x + 32) // 32] == 2:
                   turns[1] = True  
                elif map[(center_y) // 32][(center_x + 32) // 32] == 3:
                   turns[1] = True  
        
        if direction == 0 or direction == 1:
            # if the x value is approximately at the midpoint of a square 
            if 7 <= center_x % 20 <= 13:
                if map[(center_y + 32) // 32][center_x // 32] == 0:
                   turns[3] = True  
                elif map[(center_y + 32) // 32][center_x // 32] == 2:
                   turns[3] = True  
                elif map[(center_y + 32) // 32][center_x // 32] == 3:
                   turns[3] = True  
                if map[(center_y - 32) // 32][center_x // 32] == 0:
                   turns[2] = True  
                elif map[(center_y - 32) // 32][center_x // 32] == 2:
                   turns[2] = True  
                elif map[(center_y - 32) // 32][center_x // 32] == 3:
                   turns[2] = True  
            if 7 <= center_y % 20 <= 13:
                if map[(center_y) // 32][(center_x - 10) // 32] == 0:
                   turns[0] = True  
                elif map[(center_y) // 32][(center_x - 10) // 32] == 2:
                   turns[0] = True  
                elif map[(center_y) // 32][(center_x - 10) // 32] == 3:
                   turns[0] = True  
                if map[(center_y) // 32][(center_x + 32) // 32] == 0:
                   turns[1] = True  
                elif map[(center_y) // 32][(center_x + 32) // 32] == 2:
                   turns[1] = True  
                elif map[(center_y) // 32][(center_x + 32) // 32] == 3:
                   turns[1] = True  
        
        
                
    else:
        turns[1] = True
        turns[0] = True
    return turns

def move_foodbot(foodbot_x,foodbot_y,turns):
    # 0 = left, 1 = right, 2 = up, 3 = down
    # if foodbot is in direction and is allowed to keep moving in that direction, 
    # change position by increasing or decreasing x and y values
    if direction == 0 and turns[0]:
        foodbot_x -= foodbot_speed
    elif direction == 1 and turns [1]:
        foodbot_x += foodbot_speed
    elif direction == 2 and turns [2]:
        foodbot_y -= foodbot_speed
    elif direction == 3 and turns [3]:
        foodbot_y += foodbot_speed
    return foodbot_x,foodbot_y


FPS = 60

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    if counter < 60:
        counter += 1
        if counter > 30:
            flicker = True
    else:
        counter = 0
        flicker = False
    
    window_display()
    foodbot_display()
    turns = position_check(foodbot_x,foodbot_y)
    foodbot_x,foodbot_y = move_foodbot(foodbot_x,foodbot_y,turns)

    for event in pygame.event.get():
        # quit game if user exits window
        if event.type == pygame.QUIT:
            run = False
        # change direction depending on key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction_c = 2
            elif event.key == pygame.K_a:
                direction_c = 0
            elif event.key == pygame.K_s:
                direction_c = 3
            elif event.key == pygame.K_d:
                direction_c = 1
        # keep foodbot moving in direction even if key pressed is lifted
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and direction_c == 2:
                direction_c = direction
            elif event.key == pygame.K_a and direction_c == 0:
                direction_c = direction
            elif event.key == pygame.K_s and direction_c == 3:
                direction_c = direction
            elif event.key == pygame.K_d and direction_c == 1:
                direction_c = direction
        for i in range(4):
            if direction_c == i and turns[i]:
                direction = i
        
        if foodbot_x > 672:
            foodbot_x = -32
        elif foodbot_x < -32:
            foodbot_x = 672


        pygame.display.update()


pygame.quit()

# only run this game if this file is ran
#if __name__ == "__main__":
    #main()
    #print("main")