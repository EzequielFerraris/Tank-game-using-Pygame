import pygame
import random as rd
pygame.init()


win = pygame.display.set_mode((1000, 700)) #creates the window
pygame.display.set_caption('First game') 

tank1Up= pygame.image.load('Tanke_arr.png')
tank1Down= pygame.image.load('Tanke_abajo.png')
tank1Right= pygame.image.load('Tanke_der.png')
tank1Left= pygame.image.load('Tanke_izq.png')
enemyUp= pygame.image.load('Enemy1up.png')
enemyDown= pygame.image.load('Enemy1down.png')
enemyRight= pygame.image.load('Enemy1right.png')
enemyLeft= pygame.image.load('Enemy1left.png')



class ship(object): #PLAYER'S TANK
    def __init__(self, x, y, width, height):
        self.x= x
        self.y= y
        self.width= width
        self.height= height
        self.vel= 10
        self.down = False
        self.left = False
        self.right = False
        self.up = True
        self.hitbox = (self.x + 10, self.y, 44, 62)
        self.score = 0
        self.lives = 3
        self.visible = 1

    def direction(self, dir):
        if dir == 'right':
            self.left = False
            self.up = False
            self.down = False
            self.right = True
        if dir == 'left':
            self.up = False
            self.down = False
            self.right = False
            self.left = True
        if dir == 'up':
            self.down = False
            self.right = False
            self.left = False
            self.up = True
        if dir == 'down':
            self.left = False
            self.right = False
            self.up = False
            self.down = True

    def hit(self):
        self.lives -=1
        self.x = 480
        self.y= 600
        if self.lives == 0:

            i1 = 0
            while i1 < 50:
                pygame.time.delay(10)
                i1 += 1
                win.fill((0, 0, 0))
                pygame.display.update()
                
            font1 = pygame.font.SysFont('Arial', 100)
            text = font1.render('Game Over', 1, (255,255,0))
            win.blit(text, (500 - (text.get_width()/2),300))
            pygame.display.update()
            i = 0
            while i < 200:
                
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
            pygame.quit()

        
    def draw(self, win):
        if self.visible > 0:
            if self.up:
                win.blit(tank1Up, (self.x,self.y))
            if self.down:
                win.blit(tank1Down, (self.x,self.y))
            if self.right:
                win.blit(tank1Right, (self.x,self.y))
            if self.left:
                win.blit(tank1Left, (self.x,self.y))
                
            if self.up or self.down:
                self.hitbox = (self.x + 10, self.y, 44, 62) 
                #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            else:
                self.hitbox = (self.x, self.y + 10, 62, 44) 
                #pygame.draw.rect(win, (255,0,0), self.hitbox,2) -> UNCOMMENT TO SEE THE HITBOX AS A RED RECTANGLE-> UNCOMMENT TO SEE THE HITBOX AS A RED RECTANGLE


class enemy(object): #ENEMIES
    
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.width= 64
        self.height= 64
        self.vel= 11
        self.changedir = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = True
        self.hitbox = (self.x + 10, self.y, 44, 62)
        self.lives = 3
        self.visible = 1
        self.shootCountdown = 0 #WHEN IT ADDS A CERTAIN NUMBER OF STEPS, FIRES A BULLET
        
        
    def direction(self, dir):
        if dir == 'right':
            self.left = False
            self.up = False
            self.down = False
            self.right = True
        if dir == 'left':
            self.up = False
            self.down = False
            self.right = False
            self.left = True
        if dir == 'up':
            self.down = False
            self.right = False
            self.left = False
            self.up = True
        if dir == 'down':
            self.left = False
            self.right = False
            self.up = False
            self.down = True
        
        
    def draw(self, win):
        if self.visible > 0:
            if self.up:
                win.blit(enemyUp, (self.x,self.y))
            if self.down:
                win.blit(enemyDown, (self.x,self.y))
            if self.right:
                win.blit(enemyRight, (self.x,self.y))
            if self.left:
                win.blit(enemyLeft, (self.x,self.y))
                
            if self.up or self.down:
                self.hitbox = (self.x + 10, self.y, 44, 62) 
                    #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            else:
                self.hitbox = (self.x, self.y + 10, 62, 44) 
                    #pygame.draw.rect(win, (255,0,0), self.hitbox,2) -> UNCOMMENT TO SEE THE HITBOX AS A RED RECTANGLE

    def hit(self):
        ship1.score += 1
        self.lives -= 1
        if self.lives == 0:
            i1 = 0
            while i1 < 50:
                pygame.time.delay(10)
                i1 += 1
                win.fill((0, 0, 0))
                pygame.display.update()
    
            font1 = pygame.font.SysFont('Arial', 100)
            text = font1.render('You win!', 1, (255,255,0))
            win.blit(text, (500 - (text.get_width()/2),300))
            pygame.display.update()
            i = 0
            while i < 200:
                
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
            pygame.quit()
        
            
            
class projectile(object): #BULLETS
    def __init__(self,x,y,radius,color,facing,axis):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing
        self.axis = axis
        self.visible = 1

    def draw(self,win):
        if self.visible > 0:
            pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) 


#DRAWING FUNCTION
def drawing():
    win.fill((0, 0, 0))
    scoretext = scoreFont.render('Life: ' + str(ship1.lives) + '   Score: ' + str(ship1.score), 1, (255,255,0))
    win.blit(scoretext, (850, 10))
    ship1.draw(win)
    enemy01.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for bullet in enemyBullets:
        bullet.draw(win)
    pygame.display.update()
    

#DECLARING LOOP VARIABLES
    
run = True
ship1 = ship(480, 600, 64, 64)
enemy01 = enemy((rd.randint(10, 900)), (rd.randint(40, 600)))
bullets = []
bulletcooldown = 0
enemybulletcd = 0
enemyBullets = []

scoreFont = pygame.font.SysFont("Arial", 17, True)


#RULES AND INTRODUCTION
intro= 0
while intro < 300:
    pygame.time.delay(10)
    win.fill((0, 0, 0))
    font1 = pygame.font.SysFont('Arial', 20, True)
    text = font1.render('Welcome to Tanky wars!', 1, (255,255,0))
    font2 = pygame.font.SysFont('Arial', 18, True)
    text2 = font2.render('In this game you have to defeat your opponent. In order to attain this, you must land 5 shoots.', 1, (255,255,0))
    text3 = font2.render('But beware! You only have 3 lives. Receiveing a bullet or colliding with your opponent will make you lose one life.', 1, (255,255,0))
    text4 = font2.render('You can move using the direction keys and shoot using the spacebar. Good luck!', 1, (255,255,0))
    win.blit(text, (500 - (text.get_width()/2),300))
    win.blit(text2, (500 - (text2.get_width()/2),330))
    win.blit(text3, (500 - (text3.get_width()/2),360))
    win.blit(text4, (500 - (text4.get_width()/2),400))
    pygame.display.update()

    intro += 1
            
#MAIN RUN

while run:
    pygame.time.delay(100) #MAKES THE GAME RUN IN A SLOWER PACE

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #allows to close the window and end the game
            run = False
    
    #PLAYER BULLETS ANIMATIONS
    #COOLDOWN
    if bulletcooldown > 0:
         bulletcooldown +=1
    if bulletcooldown > 3:
         bulletcooldown =0

    #PLAYER SHOOT
    
            
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy01.hitbox[1] + enemy01.hitbox[3] and bullet.y + bullet.radius > enemy01.hitbox[1]:
            if bullet.x + bullet.radius > enemy01.hitbox[0] and bullet.x - bullet.radius < enemy01.hitbox[0] + enemy01.hitbox[2]:
                enemy01.hit()
                bullets.pop(bullets.index(bullet))
                
        if bullet.axis == 'x':
            if bullet.x < 1000 and bullet.x > 0:
                bullet.x += bullet.vel  # Moves the bullet by its vel
            else:
                bullets.pop(bullets.index(bullet))  # This will remove the bullet if it is off the screen
        else:
            if bullet.y < 700 and bullet.y > 0:
                bullet.y += bullet.vel  # Moves the bullet by its vel
            else:
                bullets.pop(bullets.index(bullet))  # This will remove the bullet if it is off the screen

    #CHECKING FOR COLITION
    if ship1.hitbox[1] < enemy01.hitbox[1] + enemy01.hitbox[3] and ship1.hitbox[1] + ship1.hitbox[3] > enemy01.hitbox[1]:
        if ship1.hitbox[0] + ship1.hitbox[2] > enemy01.hitbox[0] and ship1.hitbox[0] < enemy01.hitbox[0] + enemy01.hitbox[2]:
            ship1.hit()
            
   

    #ENEMY BULLETS ANIMATIONS
    #COOLDOWN
    if enemybulletcd > 0:
         enemybulletcd +=1
    if enemybulletcd > 3:
         enemybulletcd =0

    #ENEMY SHOOT

    for bullet in enemyBullets:
        if bullet.y - bullet.radius < ship1.hitbox[1] + ship1.hitbox[3] and bullet.y + bullet.radius > ship1.hitbox[1]:
            if bullet.x + bullet.radius > ship1.hitbox[0] and bullet.x - bullet.radius < ship1.hitbox[0] + ship1.hitbox[2]:
                ship1.hit()
                enemyBullets.pop(enemyBullets.index(bullet))
                
        if bullet.axis == 'x':
            if bullet.x < 1000 and bullet.x > 0:
                bullet.x += bullet.vel  # Moves the bullet by its vel
            else:
                enemyBullets.pop(enemyBullets.index(bullet))  # This will remove the bullet if it is off the screen
        else:
            if bullet.y < 700 and bullet.y > 0:
                bullet.y += bullet.vel  # Moves the bullet by its vel
            else:
                enemyBullets.pop(enemyBullets.index(bullet))  # This will remove the bullet if it is off the screen
                
    if enemy01.shootCountdown == 10:
        if enemy01.left: 
            facing = -1
            or_ax = 'x'
        elif enemy01.right:
            facing = 1
            or_ax = 'x'
        elif enemy01.up:
            facing = -1
            or_ax = 'y'
        elif enemy01.down:
            facing = 1
            or_ax = 'y'
            
        if len(enemyBullets) < 15:  # This will make sure enemy cannot exceed 5 bullets on the screen at once
            if enemy01.up:
                enemyBullets.append(projectile(round(enemy01.x + enemy01.width//2), enemy01.y, 6, (255,0,0), facing, or_ax))
            elif enemy01.left:
                enemyBullets.append(projectile(round(enemy01.x), round(enemy01.y + enemy01.height//2), 6, (255,0,0), facing, or_ax))
            elif enemy01.right:
                enemyBullets.append(projectile((enemy01.x + enemy01.width), round(enemy01.y + enemy01.height//2), 6, (255,0,0), facing, or_ax))
            else:
                enemyBullets.append(projectile(round(enemy01.x + enemy01.width//2), round(enemy01.y + enemy01.height), 6, (255,0,0), facing, or_ax))
        enemybulletcdenemybulletcd = 1
        enemy01.shootCountdown = 0
    
    #ENEMY RANDOM MOVEMENT 
    if enemy01.changedir >= 6:

        rvalue = rd.randint(1, 4)
	    
        if rvalue == 1:
            enemy01.direction('down')
            
        if rvalue == 2:
            enemy01.direction('up')  
            
        if rvalue == 3:
            enemy01.direction('right')
            
        if rvalue == 4:
            enemy01.direction('left')
            
        enemy01.changedir = 0
        rvalue = 0

    if enemy01.down and (enemy01.y + enemy01.height) < 700:
        enemy01.y += enemy01.vel
        enemy01.shootCountdown += 2
        enemy01.changedir += 1
    if enemy01.down and (enemy01.y + enemy01.height) >= 700:
        enemy01.changedir += 1
        
    if enemy01.up and enemy01.y > 30:
        enemy01.y -= enemy01.vel
        enemy01.shootCountdown += 2
        enemy01.changedir += 1
    if enemy01.up and enemy01.y <= 30:
        enemy01.changedir += 1
        
    if enemy01.right and (enemy01.x + enemy01.width) < 1000:
        enemy01.x += enemy01.vel
        enemy01.shootCountdown += 2
        enemy01.changedir += 1
    if enemy01.right and (enemy01.x + enemy01.width) >= 1000:
        enemy01.changedir += 1
        
    if enemy01.left and enemy01.x > 0:
        enemy01.x -= enemy01.vel
        enemy01.shootCountdown += 2
        enemy01.changedir += 1
    if enemy01.left and enemy01.x <= 0:
        enemy01.changedir += 1
        
                
    #KEYS
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ship1.x > ship1.vel:
        ship1.direction('left')
        ship1.x -= ship1.vel
        
    if keys[pygame.K_RIGHT] and ship1.x < 1000 - ship1.width - ship1.vel:
        ship1.direction('right')
        ship1.x += ship1.vel
        
    if keys[pygame.K_UP] and ship1.y > ship1.vel + 25:
        ship1.direction('up')
        ship1.y -= ship1.vel
        
    if keys[pygame.K_DOWN] and ship1.y < 700 - ship1.height - ship1.vel:
        ship1.direction('down')
        ship1.y += ship1.vel
        
    if keys[pygame.K_SPACE] and bulletcooldown == 0:
        if ship1.left: 
            facing = -1
            or_ax = 'x'
        elif ship1.right:
            facing = 1
            or_ax = 'x'
        elif ship1.up:
            facing = -1
            or_ax = 'y'
        elif ship1.down:
            facing = 1
            or_ax = 'y'
        if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
            if ship1.up:
                bullets.append(projectile(round(ship1.x + ship1.width//2), ship1.y, 6, (255,255,0), facing, or_ax))
            elif ship1.left:
                bullets.append(projectile(round(ship1.x), round(ship1.y + ship1.height//2), 6, (255,255,0), facing, or_ax))
            elif ship1.right:
                bullets.append(projectile((ship1.x + ship1.width), round(ship1.y + ship1.height//2), 6, (255,255,0), facing, or_ax))
            else:
                bullets.append(projectile(round(ship1.x + ship1.width//2), round(ship1.y + ship1.height), 6, (255,255,0), facing, or_ax))
        bulletcooldown = 1
    
    drawing() #CALLS THE DRAWING FUNCTION
    
pygame.quit()
        
