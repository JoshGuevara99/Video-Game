import pygame
import random
import math
#Initialize the pygame
pygame.init()
#Create screen X,Y
screen = pygame.display.set_mode((800,650))
#Background
background = pygame.image.load('Screen Shot 2020-06-19 at 5.44.52 PM.png')
#Title
pygame.display.set_caption("Space Defense")
#Player 
playerImage = pygame.image.load('spaceship.png')
spawnX = 370 
spawnY = 480
CurrentPlayerX = spawnX
CurrentPlayerY = spawnY
playerX_Change = 0
playerY_Change = 0
def player(x,y):
    #Param image, coordinates
    screen.blit(playerImage, (x,y))
#Enemy
enemyImage = pygame.image.load('ufo.png')
enemyX = random.randint(0,800)
enemyY = 0
enemyX_Change = 0
def enemy(j,k):
    screen.blit(enemyImage, (j,k))

#Bullets
bulletImage = pygame.image.load('bullet.png')   
bulletY = CurrentPlayerY
def shoot(w,z):
    screen.blit(bulletImage,(w,z)) 
explosionImage = pygame.image.load('explosion.png')
def explode(x,y):
    screen.blit(explosionImage,(x,y))


    


#Anything we want to persistently be in the game window has to go in the loop
#Keeping Game Loop running 
shotX = 0
shotY = 0
fire = False
cantShoot = False
running = True
clearedWall = True
shot = False
while running:
    
    #Param red green and blue 255 max
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        #QUIT refers to the quitting button
        if event.type == pygame.QUIT:
            running = False
    
        #If keystroke is pressed/ a key pressed down, check if left or right
        if event.type == pygame.KEYDOWN:
            #Check and restrict movement boundaries
            if CurrentPlayerX >= 735:
                CurrentPlayerX = 735
            if CurrentPlayerY >=635:
                CurrentPlayerY = 635
            if CurrentPlayerX <= 0:
                CurrentPlayerX = 0
            if CurrentPlayerY <= 0: 
                CurrentPlayerY = 0

            #Movement, adjust coordinates according to keys pressed
            if event.key == pygame.K_a:
                playerX_Change = -4
            if event.key == pygame.K_d:
                playerX_Change = 4
            if event.key == pygame.K_w:
                playerY_Change =-4
            if event.key == pygame.K_s:
                playerY_Change = 4
            
            #Firing 
            if event.key == pygame.K_SPACE and cantShoot == False:
                fire = True
                shotX = CurrentPlayerX+19
                shotY = CurrentPlayerY-15
                
            
        #Movement stops when keys go up
        if event.type == pygame.KEYUP:
            #Prevents movement stopping when keyup event occurs
            if event.key == pygame.K_a:
                if pygame.key.get_pressed()[pygame.K_d] == True:
                    playerX_Change = 4
            
                else:
                    playerX_Change = 0
            if event.key == pygame.K_d:
                if pygame.key.get_pressed()[pygame.K_a] == True:
                    playerX_Change = -4
            
                else:
                    playerX_Change = 0
                
            if event.key == pygame.K_s:
                if pygame.key.get_pressed()[pygame.K_w] == True:
                    playerY_Change = -4
            
                else:
                    playerY_Change = 0
            if event.key == pygame.K_w:
                if pygame.key.get_pressed()[pygame.K_s] == True:
                    playerY_Change = 4
            
                else:
                    playerY_Change = 0
                
       
        

    #Enemy movemement and boundaries
    
    if(clearedWall):
        enemyX_Change = 6
    if enemyX >= 735:
        clearedWall = False
        enemyY = enemyY+20
        enemyX_Change= -6
        
    if enemyX <= 0:
        enemyX_Change = 6
        enemyY = enemyY +20
    
    
    #Spawn coords playerX playerY
    CurrentPlayerX +=playerX_Change
    CurrentPlayerY +=playerY_Change
    player(CurrentPlayerX, CurrentPlayerY)  
    
    if fire == True:
        shoot(shotX,shotY)
        shotY -= 20
        cantShoot = True
        if (shotY <= 0):
            cantShoot = False
    #Implementing collision with distance formula
    delta_x = (enemyX+30)-shotX
    delta_y = (enemyY-20)-shotY
    distance = 0
   
    if bulletY>0 :
        distance = math.sqrt(pow(delta_x,2)+(pow(delta_y,2)))
        #If there is a collision
        if distance <=30 and shot == False:
            shot = True
            explode(enemyX,enemyY)
        

            
    enemyX += enemyX_Change
    if shot == False:
        enemy(enemyX,enemyY)
    pygame.display.update()
    
    




