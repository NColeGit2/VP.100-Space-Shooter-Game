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
  
  #bullet functions
  def drawBullet(self):
    pygame.draw.circle(screen, GREEN, [self._x, self._y], self._radius)

#other variable initializers (fonts, text, images, etc)

canShoot=True
flag2=0
bulletID=0

#alterable variables
reloadTime=30
bulletRadius=10

plrSpaceShip=SpaceShip(20, 50)
shipX=screen_width/2

bullets=[]

#functions for game
def drawPlayer(x):
  pygame.draw.rect(screen, GREY, [x, screen_height-plrSpaceShip.getHeight(), plrSpaceShip.getWidth(), plrSpaceShip.getHeight()])

def movePlayer(direction, currentX):
  speed=5
  if currentX < screen_width-plrSpaceShip.getWidth():
    if direction == 'r':
      currentX+=speed
  if currentX > 0:
    if direction == 'l':
      currentX-=speed 
  return(currentX)

def createBullets(currentX):
  print('circle')
  newBullet=Bullet(bulletRadius, currentX, screen_height-plrSpaceShip.getHeight()-bulletRadius)
  bullets.append(newBullet)
  print('circle2')

def updateBullets():
  for bullet in bullets:
    if bullet.getY() > 0-bulletRadius:
      bullet.setY(bullet.getY()-10)
    else:
      print('bullet dead')
      bullets.remove(bullet)
    bullet.drawBullet()

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
    if flag2 < reloadTime:
      print(flag2)
      flag2+=1
    else:
      print("Can shoot")
      flag2=0
      canShoot=True

    
  #add your mouse controls here

  #all items drawn to the screen go here
  screen.fill((0, 0, 0))
  pygame.draw.line(screen, GREEN, [0, 0], [100,100], 5)
  drawPlayer(shipX)


  
  updateBullets()
  #This function call updates the screen
  pygame.display.update()

  #sets the frame rate
  clock.tick(60)
#quits the pygame module 
pygame.quit() 
quit() 