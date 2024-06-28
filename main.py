import pygame
import os

# map of maze
# 0 = gray square, 1 = red square, 2 = small buckeye, 3 = big buckeye, 
# 4 = foodbot, 5 = enemy 1, 6 = enemy 2, 7 = enemy 3, 8 = enemy 4
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 1],
       [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1],
       [1, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [0, 2, 1, 2, 1, 2, 1, 1, 1, 4, 1, 2, 1, 1, 1, 1, 2, 1, 2, 0],
       [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1],
       [1, 2, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 2, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],
       [1, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# game images
SCARLET_SQUARE = pygame.image.load(os.path.join('assets','scarlet.png'))
SMALL_BUCKEYE = pygame.image.load(os.path.join('assets','smallbuckeye.png'))
BIG_BUCKEYE = pygame.image.load(os.path.join('assets','bigbuckeye.png'))
FOODBOT = pygame.image.load(os.path.join('assets','foodbot.png'))
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

# display window with main aspects
def window_main():
     WINDOW.fill(GRAY)

     for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                WINDOW.blit(SCARLET_SQUARE,(j * 32, i * 32))
            elif map[i][j] == 2:
                WINDOW.blit(SMALL_BUCKEYE,(j * 32, i * 32))
            elif map[i][j] == 3:
                WINDOW.blit(BIG_BUCKEYE,(j * 32, i * 32))
            elif map[i][j] == 4:
                WINDOW.blit(FOODBOT,(j * 32, i * 32))

     pygame.display.update()

FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # quit game if user exits window
            if event.type == pygame.QUIT:
                run = False

        window_main()
    

   
    

    pygame.quit()

# only run this game if this file is ran
if __name__ == "__main__":
    main()