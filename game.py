import pygame 
import random

#anchor the pygame screen so you see it in codio.
#Click on the arrow in the upper left corner to display in a new browser tab.
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

#start the pygame module 
pygame.init() 

#variables for screen size: 
screen_width=1000
screen_height=750

#color code constants 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)

#classes
class SpaceShip:
  def __init__(self, width, height):
    """init vars"""
    self._height=height
    self._width=width

  #getters & setters
  def setHeight(self, height):
    self._height=height
  def getHeight(self):
    return(self._height)
  
  def setWidth(self, width):
    self._width=width
  def getWidth(self):
    return(self._width)
  
class Bullet:
  def __init__(self, radius, x, y):
    """init vars"""
    self._radius=radius
    self._x=x
    self._y=y
    self._hitbox=pygame.Rect(self._x, self._y, self._radius*2, self._radius*2)

  #getters & setters
  def setRadius(self, radius):
    self._radius=radius
  def getRadius(self):
    return(self._radius)
  
  def setX(self, x):
    self._x=x
  def getX(self):
    return(self._x)
  
  def setY(self, y):
    self._y=y
  def getY(self):
    return(self._y)
  
  def setHitbox(self, hitbox):
    self._hitbox=hitbox
  def getHitbox(self):
    return(self._hitbox)
  #bullet functions
  def updateHitbox(self):
    self._hitbox=pygame.Rect(self._x, self._y, self._radius*2, self._radius*2)

  def drawBullet(self):
    return(pygame.draw.circle(screen, GREEN, [self._x, self._y], self._radius))

class Enemy:
  def __init__(self, y):
    self._startPos=random.randint(0, screen_width-enemySize)
    self._x=self._startPos
    self._y=y
    self._canMove=False
    self._moveCD=10
    self._hitbox=pygame.Rect(self._x, self._y, enemySize, enemySize)

  
  def setX(self, x):
    self._x=x
  def setY(self, y):
    self._y=y
  def getX(self):
    return(self._x)
  def getY(self):
    return(self._y)
  
  def setCanMove(self, data):
    self._canMove=data
  def getCanMove(self):
    return(self._canMove)
  
  def setMoveCD(self, data):
    self._moveCD=data
  def getMoveCD(self):
    return(self._moveCD)
  
  def setHitbox(self, hitbox):
    self._hitbox=hitbox
  def getHitbox(self):
    return(self._hitbox)
  #
  def updateHitbox(self):
    self._hitbox=pygame.Rect(self._x, self._y, enemySize, enemySize)

  def countdown(self):
    if self._moveCD > 0:
      self._moveCD-=1
    else:
      self._canMove=True

  def drawEnemy(self):
    return(pygame.draw.rect(screen, RED, [self._x, self._y, enemySize, enemySize]))
      

#other variable initializers (fonts, text, images, etc)



#alterable variables
reloadTime=20
bulletRadius=10
bulletSpeed=10
enemySize=40
randomSpawnTime=True
enemySpawnCooldown=300
enemyMoveCooldown=15
speed=5
enemySpeed=5
enemyXRange=15

plrSpaceShip=SpaceShip(20, 50)
shipX=screen_width/2

bullets=[]
enemies=[]

canShoot=True
flag=0
enemyFlag=enemySpawnCooldown

#functions for game
def drawPlayer(x):
  pygame.draw.rect(screen, GREY, [x, screen_height-plrSpaceShip.getHeight(), plrSpaceShip.getWidth(), plrSpaceShip.getHeight()])

def movePlayer(direction, currentX):
  
  if currentX < screen_width-plrSpaceShip.getWidth():
    if direction == 'r':
      currentX+=speed
  if currentX > 0:
    if direction == 'l':
      currentX-=speed 
  return(currentX)

def checkCollision():
  for bullet in bullets:
    for enemy in enemies:
      if(pygame.Rect.colliderect(enemy.drawEnemy(), bullet.drawBullet())):
        print('hit!')
        try:
          bullets.remove(bullet)
          enemies.remove(enemy)
        except ValueError:
          print('error, one bullet hit two targets')

def createBullets(currentX):
  newBullet=Bullet(bulletRadius, currentX, screen_height-plrSpaceShip.getHeight()-bulletRadius)
  bullets.append(newBullet)

def updateBullets():
  for bullet in bullets:
    if bullet.getY() > 0-bulletRadius:
      bullet.setY(bullet.getY()-bulletSpeed)
    else:
      #print('bullet dead')
      bullets.remove(bullet)

    checkCollision()
    bullet.drawBullet()

def spawnEnemy():
  newEnemy=Enemy(0)
  enemies.append(newEnemy)

def updateEnemies():
  for enemy in enemies:
    enemy.countdown()
    if enemy.getY() > screen_height+enemySize:
      enemies.remove(enemy)
    elif enemy.getCanMove():
        enemy.setCanMove(False)
        enemy.setMoveCD(enemyMoveCooldown)
        
        xMovement=random.randint(-enemyXRange, enemyXRange)
        if enemy.getX()+xMovement > 0 and enemy.getX()+xMovement < screen_width-enemySize:
          enemy.setX(enemy.getX()+xMovement)
        enemy.setY(enemy.getY()+enemySpeed)

    enemy.drawEnemy()
    #print(enemy.getY())

#create a screen with dimensions 
screen = pygame.display.set_mode((screen_width, screen_height)) 

#set the screen caption 
pygame.display.set_caption("My First Pygame") 
#fills the screen initially with black
screen.fill((0, 0, 0))

 

#the clock will be used to regulate the frame rate 
clock = pygame.time.Clock() 

#variable to control the game loop 
keep_playing=True 



#OTHER STUFF ABOOOVE
#GAME LOOP BELOOOW


#Game Loop - needed to keep updating and redrawing the screen 
while keep_playing==True: 
  #iterates over the current list of events(checks for events)  
  for event in pygame.event.get(): 
    #will stop the game loop if escape is pressed (doesn't work in Codio)
    if event.type == pygame.QUIT: 
      keep_playing = False

  #add your key press code here
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_x]:
    print("close")
    keep_playing=False
  ##movement
  if pressed[pygame.K_LEFT]:
    #print('Going left')
    shipX=movePlayer('l', shipX)
  if pressed[pygame.K_RIGHT]:
    #print('Going right')
    shipX=movePlayer('r', shipX)
  ##shoot
  if canShoot:
    if pressed[pygame.K_SPACE]:
      canShoot=False
      createBullets(shipX+(plrSpaceShip.getWidth()/2))  #gets the bullet centered on the ship
  else:
    #waits countdown, 60 frames is a second
    if flag < reloadTime:
      #print(flag)
      flag+=1
    else:
      print("Can shoot")
      flag=0
      canShoot=True

    
  #add your mouse controls here


  #spawn enemy loop
  if enemyFlag > 0:
    enemyFlag-=1
    #print(enemySpawnCooldown)
    #print(enemyFlag)
  else: 
    spawnEnemy()
    if randomSpawnTime:
      enemyFlag=random.randint(0,enemySpawnCooldown)
      #print(enemyFlag)
    else:
      enemyFlag=enemySpawnCooldown
  
  #all items drawn to the screen go here
  screen.fill((0, 0, 0))
  pygame.draw.line(screen, GREEN, [0, 0], [100,100], 5)
  drawPlayer(shipX)


  #enemy stuff


  updateBullets()
  updateEnemies()
  #This function call updates the screen
  pygame.display.update()

  #sets the frame rate
  clock.tick(60)
#quits the pygame module 
pygame.quit() 
quit() 