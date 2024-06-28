import pygame
import os

pygame.init()

# map of maze
# 0 = gray square, 1 = red square, 2 = small buckeye, 3 = big buckeye, 
# 4 = foodbot, 5 = enemy 1, 6 = enemy 2, 7 = enemy 3, 8 = enemy 4
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
       [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
       [1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0, 1, 1, 2, 1, 2, 1],
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
direction = 0
flicker = False
counter = 0

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


#change foodbot direction facing based on movement
# 0 = left, 1 = right, 2 = up, 3 = down
def foodbot_display():
    if direction == 0:
        WINDOW.blit(FOODBOT_LEFT,(foodbot_x,foodbot_y))
    elif direction == 1:
        WINDOW.blit(pygame.transform.flip(FOODBOT_LEFT,True, False), (foodbot_x,foodbot_y))
        print ("direction right working")
    elif direction == 2:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 270), (foodbot_x,foodbot_y))
        print ("direction up working")
    elif direction == 3:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 90), (foodbot_x,foodbot_y))
        print ("direction down working")
    

FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    counter = 0
    while run:
        clock.tick(FPS)
        if counter < 19:
            counter += 1
            if counter > 3:
                flicker = False
        else:
            counter = 0
            flicker = True

        window_display()
        foodbot_display()
        for event in pygame.event.get():
            # quit game if user exits window
            if event.type == pygame.QUIT:
                run = False
            # change direction depending on key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = 2
                    print ("W pressed")
                elif event.key == pygame.K_a:
                    direction = 0
                    print ("A pressed")
                elif event.key == pygame.K_s:
                    direction = 3
                    print ("S pressed")
                elif event.key == pygame.K_d:
                    direction = 1
                    print ("D pressed")
                print(direction)
        
        pygame.display.update()


    pygame.quit()

# only run this game if this file is ran
if __name__ == "__main__":
    main()
    print("main")