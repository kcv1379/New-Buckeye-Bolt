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

# displaying window that is 640 x 700
WIDTH = 640
HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

# game images
GRAY_SQUARE = pygame.image.load(os.path.join('assets','gray.png'))
SCARLET_SQUARE = pygame.image.load(os.path.join('assets','scarlet.png'))
SMALL_BUCKEYE = pygame.image.load(os.path.join('assets','smallbuckeye.png'))
BIG_BUCKEYE = pygame.image.load(os.path.join('assets','bigbuckeye.png'))
FOODBOT_LEFT = pygame.image.load(os.path.join('assets','foodbot.png'))
#ENEMY_1 = pygame.image.load(os.path.join('assets','enemy1.png'))
#ENEMY_2 = pygame.image.load(os.path.join('assets','enemy2.png'))
#ENEMY_3 = pygame.image.load(os.path.join('assets','enemy3.png'))
#ENEMY_4 = pygame.image.load(os.path.join('assets','enemy4.png'))
ENEMY_DOOR = pygame.image.load(os.path.join('assets','enemydoor.png'))

# colors
GRAY = (167, 177, 183)
SCARLET = (187, 0, 0)

# display game name at top of window
pygame.display.set_caption("Buckeye Bolt")

# initial game settings
foodbot_x = 288
foodbot_y = 320
direction = 0
direction_c = 0
flicker = False
counter = 0
turns = [False, False, False, False]   
score = 0 

# display window with main aspects
def window_display():
     WINDOW.fill(GRAY)

     for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                pygame.draw.rect(WINDOW,SCARLET,pygame.Rect(j * 32, i * 32, 32, 32))
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
            elif map[i][j] == 0:
                WINDOW.blit(GRAY_SQUARE,(j * 32, i * 32))


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
def position_check(x,y):
    # 0 = left, 1 = right, 2 = up, 3 = down
    # if square ahead of foodbot is red,stop them from moving 
    #32, 15?
    turns = [False, False, False, False]
    
    # x and y are already centerd, no need to adjust
    center_x = x 
    center_y = y 

    if center_x // 32 < 19:
       # down
       if map[round((center_y + 18) / 32)][round((center_x + 5) / 32)] == 0 and 0 <= center_x % 32 <= 5:
           turns[3] = True
       elif map[round((center_y + 18) / 32)][round((center_x + 5) / 32)] == 2 and 0 <= center_x % 32 <= 5:
           turns[3] = True
       elif map[round((center_y + 18) / 32)][round((center_x + 5) / 32)] == 3 and 0 <= center_x % 32 <= 5:
           turns[3] = True

      # up
       if map[round((center_y - 18) / 32)][round((center_x - 5) / 32)] == 0 and 0 <= center_x % 32 <= 5:
           turns[2] = True
       elif map[round((center_y - 18) / 32)][round((center_x - 5) / 32)] == 2 and 0 <= center_x % 32 <= 5:
           turns[2] = True
       elif map[round((center_y - 18) / 32)][round((center_x - 5) / 32)] == 3 and 0 <= center_x % 32 <= 5:
           turns[2] = True

       # right
       if map[round((center_y + 5) / 32)][round((center_x + 18) / 32)] == 0 and 0 <= center_y % 32 <= 5:
           turns[1] = True
       elif map[round((center_y + 5) / 32)][round((center_x + 18) / 32)] == 2 and 0 <= center_y % 32 <= 5:
          turns[1] = True
       elif map[round((center_y + 5) / 32)][round((center_x + 18) / 32)] == 3 and 0 <= center_y % 32 <= 5:
           turns[1] = True

       # left 
       if map[round((center_y - 5) / 32)][round((center_x - 16) / 32)] == 0 and 0 <= center_y % 32 <= 5:
           turns[0] = True
       elif map[round((center_y - 5) / 32)][round((center_x - 16) / 32)] == 2 and 0 <= center_y % 32 <= 5:
           turns[0] = True
       elif map[round((center_y - 5) / 32)][round((center_x - 16) / 32)] == 3 and 0 <= center_y % 32 <= 5:
           turns[0] = True
    
    else: 
        turns[0] = True
        turns[1] = True
    return turns

# move foodbot based on where its at and if its able to turn
def move_foodbot(foodbot_x,foodbot_y,turns):
    # 0 = left, 1 = right, 2 = up, 3 = down
    # if foodbot is in direction and is allowed to keep moving in that direction, 
    # change position by increasing or decreasing x and y values
    if direction == 0 and turns[0]:
        foodbot_x -= 2
    elif direction == 1 and turns [1]:
        foodbot_x += 2
    elif direction == 2 and turns [2]:
        foodbot_y -= 2
    elif direction == 3 and turns [3]:
        foodbot_y += 2
    return foodbot_x,foodbot_y

# change score based on what's eaten
def score_change(x, y, score):
    if map[y // 32][x // 32] == 2:
        map[y // 32][x // 32] == 0
        score += 10
    if map[y // 32][x // 32] == 3:
        map[y // 32][x // 32] == 0
        score += 50
    
    score += 10
    return score
    
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
    score = score_change(foodbot_x,foodbot_y,score)

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
        
        if (foodbot_x) > 600:
            foodbot_x = 0
            direction = 1

        elif (foodbot_x) < 0:
            foodbot_x = 600
            direction = 0

        print("x: ")
        print(foodbot_x)
        print("y: ")
        print(foodbot_y)

    pygame.display.update()
        

pygame.quit()

# only run this game if this file is ran
#if __name__ == "__main__":
    #main()
    #print("main")