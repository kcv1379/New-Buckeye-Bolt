import pygame
import os

pygame.init()

# need to figure out how to add main function
# CHANGE ENEMIES TO CARS THAT HIT FOODBOT 

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
       [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0, 0, 1, 2, 1, 2, 1],
       [0, 2, 1, 2, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 1, 2, 1, 2, 0],
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
ENEMY1_IMAGE = pygame.image.load(os.path.join('assets','enemy1.png'))
ENEMY2_IMAGE = pygame.image.load(os.path.join('assets','enemy2.png'))
ENEMY3_IMAGE = pygame.image.load(os.path.join('assets','enemy3.png'))
ENEMY4_IMAGE = pygame.image.load(os.path.join('assets','enemy4.png'))
ENEMY_EYES = pygame.image.load(os.path.join('assets','enemyeyes.png'))
ENEMY_POWERUP = pygame.image.load(os.path.join('assets','powerupenemy.png'))
ENEMY_DOOR = pygame.image.load(os.path.join('assets','enemydoor.png'))

# colors and font
GRAY = (167, 177, 183)
SCARLET = (187, 0, 0)
font = pygame.font.Font(None, 32)

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
powerup = False
powerup_count = 0
enemy_eaten = [False, False, False, False]
start_count = 0
start_game = False
lives_left = 3
ENEMY_1_x = 416
ENEMY_1_y = 288
ENEMY_1_direction = 0
ENEMY_2_x = 448
ENEMY_2_y = 288
ENEMY_2_direction = 0
ENEMY_3_x = 416
ENEMY_3_y = 256
ENEMY_3_direction = 0
ENEMY_4_x = 448
ENEMY_4_y = 256
ENEMY_4_direction = 0
enemy_targets = [(foodbot_x,foodbot_y), (foodbot_x,foodbot_y), (foodbot_x,foodbot_y), (foodbot_x,foodbot_y)]
ENEMY_1_eaten = False
ENEMY_2_eaten = False
ENEMY_3_eaten = False
ENEMY_4_eaten = False
ENEMY_1_box = True
ENEMY_2_box = True
ENEMY_3_box = True
ENEMY_4_box = True
enemy_speed = [2, 2, 2, 2]
game_over = False
buckeyes_collected = 0

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
            elif map[i][j] == 9:
                WINDOW.blit(ENEMY_DOOR,(j * 32, i * 32))
            elif map[i][j] == 0:
                WINDOW.blit(GRAY_SQUARE,(j * 32, i * 32))

# change foodbot direction facing based on movement
# 0 = left, 1 = right, 2 = up, 3 = down
def foodbot_display():
    if direction == 0:
        WINDOW.blit(FOODBOT_LEFT,(foodbot_x, (foodbot_y - 2)))
    elif direction == 1:
        WINDOW.blit(pygame.transform.flip(FOODBOT_LEFT,True, False), (foodbot_x, (foodbot_y - 2)))
    elif direction == 2:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 270), (foodbot_x,foodbot_y))
    elif direction == 3:
        WINDOW.blit(pygame.transform.rotate(FOODBOT_LEFT, 90), ((foodbot_x - 2),foodbot_y))
    
# miscellaneous stuff to be put on window 
def misc_display():
    score_text = font.render(f'SCORE: {score}', True, 'black')
    WINDOW.blit(score_text, (20, 660))

    for i in range(lives_left):
        WINDOW.blit(FOODBOT_LEFT, (470 + (50 * i), 650))
        
# checking which directions foodbot is allowed to move based on position
def position_check():
    # 0 = left, 1 = right, 2 = up, 3 = down
    # if square ahead of foodbot is red,stop them from moving 
    #32, 15?
    turns = [False, False, False, False]
    
    # x and y are already centerd, no need to adjust
    center_x = foodbot_x 
    center_y = foodbot_y

    if round(center_x / 32) < 19:
       # down
       if map[round((center_y + 18) / 32)][round((center_x + 0) / 32)] == 0 and 0 <= center_x % 32 <= 8:
           turns[3] = True
       elif map[round((center_y + 18) / 32)][round((center_x + 0) / 32)] == 2 and 0 <= center_x % 32 <= 8:
           turns[3] = True
       elif map[round((center_y + 18) / 32)][round((center_x + 0) / 32)] == 3 and 0 <= center_x % 32 <= 8:
           turns[3] = True

      # up
       if map[round((center_y - 18) / 32)][round((center_x - 0) / 32)] == 0 and 0 <= center_x % 32 <= 8:
           turns[2] = True
       elif map[round((center_y - 18) / 32)][round((center_x - 0) / 32)] == 2 and 0 <= center_x % 32 <= 8:
           turns[2] = True
       elif map[round((center_y - 18) / 32)][round((center_x - 0) / 32)] == 3 and 0 <= center_x % 32 <= 8:
           turns[2] = True

       # right
       if map[round((center_y + 0) / 32)][round((center_x + 16) / 32)] == 0 and 0 <= center_y % 32 <= 8:
           turns[1] = True
       elif map[round((center_y + 0) / 32)][round((center_x + 16) / 32)] == 2 and 0 <= center_y % 32 <= 8:
          turns[1] = True
       elif map[round((center_y + 0) / 32)][round((center_x + 16) / 32)] == 3 and 0 <= center_y % 32 <= 8:
           turns[1] = True

       # left 
       if map[round((center_y - 0) / 32)][round((center_x - 18) / 32)] == 0 and 0 <= center_y % 32 <= 8:
           turns[0] = True
       elif map[round((center_y - 0) / 32)][round((center_x - 18) / 32)] == 2 and 0 <= center_y % 32 <= 8:
           turns[0] = True
       elif map[round((center_y - 0) / 32)][round((center_x - 18) / 32)] == 3 and 0 <= center_y % 32 <= 8:
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

# change score based on what's eaten and activate powerup abilities if big buckeye eaten
def score_change(score, powerup, powerup_count, enemy_eaten, buckeyes_collected):
    if 0 < foodbot_x < 608:
        if map[foodbot_y // 32][foodbot_x // 32] == 2:
           map[foodbot_y // 32][foodbot_x // 32] = 0
           score += 10
           buckeyes_collected += 1
        if map[foodbot_y // 32][foodbot_x // 32] == 3:
           map[foodbot_y // 32][foodbot_x // 32] = 0
           score += 50
           powerup = True
           powerup_count = 0
           enemy_eaten = [False, False, False, False]
           buckeyes_collected +=1
    return score, powerup, powerup_count, enemy_eaten, buckeyes_collected
    
class Enemies:
    def __init__(self, x, y, target, speed, image, enemy_direction, eaten, box, id):
       self.x_coord = x
       self.y_coord = y
       self.target = target
       self.speed = speed
       self.image = image
       self.enemy_direction = enemy_direction
       self.eaten = eaten
       self.in_box = box 
       self.id = id 
       self.turns, self.in_box = self.collision_check()
       self.rect = self.draw()

    def draw(self): 
        if (not powerup and not self.eaten) or (enemy_eaten[self.id] and powerup and not self.eaten) or self.in_box:
            WINDOW.blit(self.image, (self.x_coord, self.y_coord))
        elif (powerup and not self.eaten and not enemy_eaten[self.id]):
            WINDOW.blit(ENEMY_POWERUP, (self.x_coord, self.y_coord))
        else:
            WINDOW.blit(ENEMY_EYES, (self.x_coord, self.y_coord))
        enemy_rect = pygame.rect.Rect((self.x_coord, self.y_coord), (32, 32))
        return enemy_rect
    
    def collision_check(self):
        self.turns = [False, False, False, False]

        if 415 < self.x_coord < 450 and 220 < self.y_coord < 330:
           self.in_box = True
           self.eaten = False
           enemy_eaten[self.id] = False
        else:
           self.in_box = False
    
        if round(self.x_coord / 32) < 19:
          # down
          if ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 0) \
            or ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[3] = True
          elif ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 2) \
          or ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[3] = True
          elif ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 3) \
            or ((map[round((self.y_coord + 18) / 32)][round((self.x_coord + 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[3] = True

         # up
          if ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 0) \
            or ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[2] = True
          elif ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 2) \
            or ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[2] = True
          elif ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 3) \
            or ((map[round((self.y_coord - 18) / 32)][round((self.x_coord - 0) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.x_coord % 32 <= 8:
              self.turns[2] = True

          # right
          if ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 0) \
            or ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.y_coord % 32 <= 8:
              self.turns[1] = True
          elif ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 2) \
            or ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.y_coord % 32 <= 8:
             self.turns[1] = True
          elif ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 3) \
            or ((map[round((self.y_coord + 0) / 32)][round((self.x_coord + 16) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.y_coord % 32 <= 8:
              self.turns[1] = True

          # left 
          if ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 0) \
            or ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.y_coord % 32 <= 8:
              self.turns[0] = True
          elif ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 2) \
          or ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 9) and (self.in_box or self.eaten))) \
          and 0 <= self.y_coord % 32 <= 8:
              self.turns[0] = True
          elif ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 3) \
            or ((map[round((self.y_coord - 0) / 32)][round((self.x_coord - 18) / 32)] == 9) and (self.in_box or self.eaten))) \
            and 0 <= self.y_coord % 32 <= 8:
              self.turns[0] = True
    
        else: 
           self.turns[0] = True
           self.turns[1] = True

        return self.turns, self.in_box

    def move_enemies(self):
        # 0 = left, 1 = right, 2 = up, 3 = down
        if self.enemy_direction == 1:
            # if target is to the right and enemy is able to move right, continue moving right
            if self.target[0] > self.x_coord and self.turns[1]:
                self.x_coord += self.speed
            # if unable to move right
            elif not self.turns[1]:
                # if target is below enemy and enemy is able to move down, move down
                if self.target[1] > self.y_coord and self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.target[1] < self.y_coord and self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                elif self.target[0] < self.x_coord and self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                elif self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                elif self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
            elif self.turns[1]:
                if self.target[1] > self.y_coord and self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                if self.target[1] < self.y_coord and self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                else:
                    self.x_coord += self.speed
        elif self.enemy_direction == 0:
            if self.target[1] > self.y_coord and self.turns[3]:
                self.enemy_direction = 3
            elif self.target[0] < self.x_coord and self.turns[0]:
                self.x_coord -= self.speed
            elif not self.turns[0]:
                if self.target[1] > self.y_coord and self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.target[1] < self.y_coord and self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                elif self.target[0] > self.x_coord and self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                elif self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                elif self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                
            elif self.turns[0]:
                if self.target[1] > self.y_coord and self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                if self.target[1] < self.y_coord and self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                else:
                    self.x_coord -= self.speed
        elif self.enemy_direction == 2:
            if self.target[0] < self.x_coord and self.turns[0]:
                self.enemy_direction = 0
                self.x_coord -= self.speed
            elif self.target[1] < self.y_coord and self.turns[2]:
                self.y_coord -= self.speed
            elif not self.turns[2]:
                if self.target[0] > self.x_coord and self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                elif self.target[0] < self.x_coord and self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                elif self.target[1] > self.y_coord and self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.turns[3]:
                    self.enemy_direction = 3
                    self.y_coord += self.speed
                elif self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                elif self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                
            elif self.turns[2]:
                if self.target[0] > self.x_coord and self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                if self.target[0] < self.x_coord and self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                else:
                    self.y_coord -= self.speed
        elif self.enemy_direction == 3:
            if self.target[1] > self.y_coord and self.turns[3]:
                self.y_coord += self.speed
            elif not self.turns[3]:
                if self.target[0] > self.x_coord and self.turns[1]:
                   self.enemy_direction = 1
                   self.x_coord += self.speed
                elif self.target[0] < self.x_coord and self.turns[0]:
                   self.enemy_direction = 0
                   self.x_coord -= self.speed
                elif self.target[1] < self.y_coord and self.turns[2]:
                   self.enemy_direction = 2
                   self.y_coord -= self.speed
                elif self.turns[2]:
                    self.enemy_direction = 2
                    self.y_coord -= self.speed
                elif self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                elif self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed              
            elif self.turns[3]:
                if self.target[0] > self.x_coord and self.turns[1]:
                    self.enemy_direction = 1
                    self.x_coord += self.speed
                if self.target[0] < self.x_coord and self.turns[0]:
                    self.enemy_direction = 0
                    self.x_coord -= self.speed
                else:
                    self.y_coord += self.speed
        if (self.x_coord) > 600:
            self.x_coord = 0
            self.enemy_direction = 1

        elif (self.x_coord) < 0:
            self.x_coord = 600
            self.enemy_direction = 0
        return self.x_coord, self.y_coord, self.enemy_direction

def get_targets(ENEMY_1_x, ENEMY_1_y, ENEMY_2_x, ENEMY_2_y, ENEMY_3_x, ENEMY_3_y, ENEMY_4_x, ENEMY_4_y):
    if foodbot_x < 320:
        escape_x = 640
    else:
        escape_x = 0
    if foodbot_y < 320:
        escape_y = 640
    else:
        escape_y = 0
    return_target = (416,320)
    if powerup:
        if not ENEMY_1_eaten and not enemy_eaten[0]:
            ENEMY_1_TARGET = (escape_x, escape_y)
        elif not ENEMY_1_eaten and enemy_eaten[0]:
            if 416 < ENEMY_1_x < 448 and 256 < ENEMY_1_y < 320:
                ENEMY_1_TARGET = (224,416)
            else: 
                ENEMY_1_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_1_TARGET = return_target

        if not ENEMY_2_eaten and not enemy_eaten[1]:
            ENEMY_2_TARGET = (escape_x, foodbot_y)
        elif not ENEMY_2_eaten and enemy_eaten[1]:
            if 416 < ENEMY_2_x < 448 and 256 < ENEMY_2_y < 320:
                ENEMY_2_TARGET = (224,416)
            else: 
                ENEMY_2_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_2_TARGET = return_target

        if not ENEMY_3_eaten and not enemy_eaten[2]:
            ENEMY_3_TARGET = (foodbot_x, escape_y)
        elif not ENEMY_3_eaten and enemy_eaten[2]:
            if 416 < ENEMY_3_x < 448 and 256 < ENEMY_3_y < 320:
                ENEMY_3_TARGET = (224,416)
            else: 
                ENEMY_3_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_3_TARGET = return_target

        if not ENEMY_4_eaten and not enemy_eaten[3]:
            ENEMY_4_TARGET = (320, 320)
        elif not ENEMY_4_eaten and enemy_eaten[3]:
            if 416 < ENEMY_4_x < 448 and 256 < ENEMY_4_y < 320:
                ENEMY_4_TARGET = (224,416)
            else: 
                ENEMY_4_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_4_TARGET = return_target

    else:
        if not ENEMY_1_eaten:
            if 416 < ENEMY_1_x < 448 and 256 < ENEMY_1_y < 320:
                ENEMY_1_TARGET = (224,416)
            else: 
                ENEMY_1_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_1_TARGET = return_target
        if not ENEMY_2_eaten:
            if 416 < ENEMY_2_x < 448 and 256 < ENEMY_2_y < 320:
                ENEMY_2_TARGET = (224,416)
            else: 
                ENEMY_2_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_2_TARGET = return_target
        if not ENEMY_3_eaten:
            if 416 < ENEMY_3_x < 448 and 256 < ENEMY_3_y < 320:
                ENEMY_3_TARGET = (224,416)
            else: ENEMY_3_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_3_TARGET = return_target
        if not ENEMY_4_eaten:
            if 416 < ENEMY_4_x < 448 and 256 < ENEMY_4_y < 320:
                ENEMY_4_TARGET = (224,416)
            else: ENEMY_4_TARGET = (foodbot_x, foodbot_y)
        else: 
            ENEMY_4_TARGET = return_target

    return [ENEMY_1_TARGET, ENEMY_2_TARGET, ENEMY_3_TARGET, ENEMY_4_TARGET]

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

    # if powerup activated for less than 10 seconds
    if powerup and powerup_count < 600:
        powerup_count += 1
    elif powerup and powerup_count >= 600:
        powerup = False
        powerup_count = 0
        enemy_eaten = [False, False, False, False]

    if 0 <= start_count < 90:
        start_game = False
        start_count += 1
        ready_text = font.render(f'READY!', True, 'black')
        WINDOW.blit(ready_text, (280, 660))
    elif 89 < start_count < 180:
        start_game = False
        start_count += 1
        ready_text = font.render(f'SET!', True, 'black')
        WINDOW.blit(ready_text, (300, 660))
    elif start_count == 180 and lives_left > 0 and buckeyes_collected < 177: 
        start_game = True
        go_text = font.render(f'GO!', True, 'black')
        WINDOW.blit(go_text, (300, 660))

    if lives_left == 0:
        start_count = -999
        start_game = False
        start_count -= 1
        WINDOW.blit(font.render(f'GAME OVER', True, 'black'), (300, 660))
    
    if buckeyes_collected == 177:
        start_count = -999
        start_game = False
        start_count -= 1
        WINDOW.blit(font.render(f'GAME WON', True, 'black'), (300, 660))

    
    
    foodbot_display()

    ENEMY_1 = Enemies(ENEMY_1_x, ENEMY_1_y, enemy_targets[0], enemy_speed[0], ENEMY1_IMAGE, ENEMY_1_direction, ENEMY_1_eaten, ENEMY_1_box, 0)
    ENEMY_2 = Enemies(ENEMY_2_x, ENEMY_2_y, enemy_targets[1], enemy_speed[1], ENEMY2_IMAGE, ENEMY_2_direction, ENEMY_2_eaten, ENEMY_2_box, 1)
    ENEMY_3 = Enemies(ENEMY_3_x, ENEMY_3_y, enemy_targets[2], enemy_speed[2], ENEMY3_IMAGE, ENEMY_3_direction, ENEMY_3_eaten, ENEMY_3_box, 2)
    ENEMY_4 = Enemies(ENEMY_4_x, ENEMY_4_y, enemy_targets[3], enemy_speed[3], ENEMY4_IMAGE, ENEMY_4_direction, ENEMY_4_eaten, ENEMY_4_box, 3)

    if powerup:
        enemy_speed = [1, 1, 1, 1]
    else: 
        enemy_speed = [2, 2, 2, 2]
    if ENEMY_1_eaten and not ENEMY_1.in_box:
        enemy_speed[0] = 4
    if ENEMY_2_eaten and not ENEMY_2.in_box:
        enemy_speed[1] = 4
    if ENEMY_3_eaten and not ENEMY_3.in_box:
        enemy_speed[2] = 4
    if ENEMY_4_eaten and not ENEMY_4.in_box:
        enemy_speed[3] = 4


    turns = position_check()
    if start_game:
        foodbot_x,foodbot_y = move_foodbot(foodbot_x,foodbot_y,turns)
        ENEMY_1_x, ENEMY_1_y, ENEMY_1_direction = ENEMY_1.move_enemies()
        ENEMY_2_x, ENEMY_2_y, ENEMY_2_direction = ENEMY_2.move_enemies()
        ENEMY_3_x, ENEMY_3_y, ENEMY_3_direction = ENEMY_3.move_enemies()
        ENEMY_4_x, ENEMY_4_y, ENEMY_4_direction = ENEMY_4.move_enemies()
    score, powerup, powerup_count, enemy_eaten, buckeyes_collected = score_change(score, powerup, powerup_count, enemy_eaten, buckeyes_collected)
    misc_display()
    foodbot_hitbox = pygame.draw.circle(WINDOW, 'white', ((foodbot_x + 16), (foodbot_y + 14)), 1, 1)
    enemy_targets = get_targets(ENEMY_1_x, ENEMY_1_y, ENEMY_2_x, ENEMY_2_y, ENEMY_3_x, ENEMY_3_y, ENEMY_4_x, ENEMY_4_y)

    if not powerup:
        if (foodbot_hitbox.colliderect(ENEMY_1.rect) and not ENEMY_1.eaten) \
            or (foodbot_hitbox.colliderect(ENEMY_2.rect) and not ENEMY_2.eaten) \
                or (foodbot_hitbox.colliderect(ENEMY_3.rect) and not ENEMY_3.eaten) \
                    or (foodbot_hitbox.colliderect(ENEMY_4.rect) and not ENEMY_4.eaten):
            if lives_left > 0:
                foodbot_x = 288
                foodbot_y = 320
                direction = 0
                direction_c = 0
                powerup = False
                powerup_count = 0
                lives_left -= 1
                start_count = 0
                ENEMY_1_x = 416
                ENEMY_1_y = 288
                ENEMY_1_direction = 0
                ENEMY_2_x = 448
                ENEMY_2_y = 288
                ENEMY_2_direction = 0
                ENEMY_3_x = 416
                ENEMY_3_y = 256
                ENEMY_3_direction = 0
                ENEMY_4_x = 448
                ENEMY_4_y = 256
                ENEMY_4_direction = 0
                enemy_eaten = [False, False, False, False]
                ENEMY_1_eaten = False
                ENEMY_2_eaten = False
                ENEMY_3_eaten = False
                ENEMY_4_eaten = False
  
    if powerup and foodbot_hitbox.colliderect(ENEMY_1.rect) and enemy_eaten[0] and not ENEMY_1.eaten:
        if lives_left > 0:
                ENEMY_1_x = 416
                ENEMY_1_y = 288
                ENEMY_1_direction = 0
                ENEMY_2_x = 448
                ENEMY_2_y = 288
                ENEMY_2_direction = 0
                ENEMY_3_x = 416
                ENEMY_3_y = 256
                ENEMY_3_direction = 0
                ENEMY_4_x = 448
                ENEMY_4_y = 256
                ENEMY_4_direction = 0
                enemy_eaten = [False, False, False, False]
                ENEMY_1_eaten = False
                ENEMY_2_eaten = False
                ENEMY_3_eaten = False
                ENEMY_4_eaten = False
    if powerup and foodbot_hitbox.colliderect(ENEMY_2.rect) and enemy_eaten[1] and not ENEMY_2.eaten:
        if lives_left > 0:
                foodbot_x = 288
                foodbot_y = 320
                direction = 0
                direction_c = 0
                powerup = False
                powerup_count = 0
                lives_left -= 1
                start_count = 0
                ENEMY_1_x = 416
                ENEMY_1_y = 288
                ENEMY_1_direction = 0
                ENEMY_2_x = 448
                ENEMY_2_y = 288
                ENEMY_2_direction = 0
                ENEMY_3_x = 416
                ENEMY_3_y = 256
                ENEMY_3_direction = 0
                ENEMY_4_x = 448
                ENEMY_4_y = 256
                ENEMY_4_direction = 0
                enemy_eaten = [False, False, False, False]
                ENEMY_1_eaten = False
                ENEMY_2_eaten = False
                ENEMY_3_eaten = False
                ENEMY_4_eaten = False
    if powerup and foodbot_hitbox.colliderect(ENEMY_3.rect) and enemy_eaten[2] and not ENEMY_3.eaten:
        if lives_left > 0:
                foodbot_x = 288
                foodbot_y = 320
                direction = 0
                direction_c = 0
                powerup = False
                powerup_count = 0
                lives_left -= 1
                start_count = 0
                ENEMY_1_x = 416
                ENEMY_1_y = 288
                ENEMY_1_direction = 0
                ENEMY_2_x = 448
                ENEMY_2_y = 288
                ENEMY_2_direction = 0
                ENEMY_3_x = 416
                ENEMY_3_y = 256
                ENEMY_3_direction = 0
                ENEMY_4_x = 448
                ENEMY_4_y = 256
                ENEMY_4_direction = 0
                enemy_eaten = [False, False, False, False]
                ENEMY_1_eaten = False
                ENEMY_2_eaten = False
                ENEMY_3_eaten = False
                ENEMY_4_eaten = False
    if powerup and foodbot_hitbox.colliderect(ENEMY_4.rect) and enemy_eaten[3] and not ENEMY_4.eaten:
        if lives_left > 0:
                foodbot_x = 288
                foodbot_y = 320
                direction = 0
                direction_c = 0
                powerup = False
                powerup_count = 0
                lives_left -= 1
                start_count = 0
                ENEMY_1_x = 416
                ENEMY_1_y = 288
                ENEMY_1_direction = 0
                ENEMY_2_x = 448
                ENEMY_2_y = 288
                ENEMY_2_direction = 0
                ENEMY_3_x = 416
                ENEMY_3_y = 256
                ENEMY_3_direction = 0
                ENEMY_4_x = 448
                ENEMY_4_y = 256
                ENEMY_4_direction = 0
                enemy_eaten = [False, False, False, False]
                ENEMY_1_eaten = False
                ENEMY_2_eaten = False
                ENEMY_3_eaten = False
                ENEMY_4_eaten = False

    if powerup and foodbot_hitbox.colliderect(ENEMY_1.rect) and not ENEMY_1.eaten and not enemy_eaten[0]:
        ENEMY_1_eaten = True
        enemy_eaten[0] = True
        score += 200
    if powerup and foodbot_hitbox.colliderect(ENEMY_2.rect) and not ENEMY_2.eaten and not enemy_eaten[1]:
        ENEMY_2_eaten = True
        enemy_eaten[1] = True
        score += 200
    if powerup and foodbot_hitbox.colliderect(ENEMY_3.rect) and not ENEMY_3.eaten and not enemy_eaten[2]:
        ENEMY_3_eaten = True
        enemy_eaten[2] = True
        score += 200
    if powerup and foodbot_hitbox.colliderect(ENEMY_4.rect) and not ENEMY_4.eaten and not enemy_eaten[3]:
        ENEMY_4_eaten = True
        enemy_eaten[3] = True
        score += 200

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

        if ENEMY_1.in_box and ENEMY_1_eaten:
            ENEMY_1_eaten = False
        elif ENEMY_2.in_box and ENEMY_2_eaten:
            ENEMY_2_eaten = False
        elif ENEMY_3.in_box and ENEMY_3_eaten:
            ENEMY_2_eaten = False
        elif ENEMY_4.in_box and ENEMY_4_eaten:
            ENEMY_4_eaten = False

    pygame.display.update()

pygame.quit()
