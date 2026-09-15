#import the pygame library a
import pygame 

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

#other variable initializers (fonts, text, images, etc)
plrSpaceShip=SpaceShip(20, 50)
shipX=screen_width/2
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
  if pressed[pygame.K_LEFT]:
    #print('Going left')
    shipX=movePlayer('l', shipX)
  if pressed[pygame.K_RIGHT]:
    #print('Going right')
    shipX=movePlayer('r', shipX)
    
  #add your mouse controls here

  #all items drawn to the screen go here
  screen.fill((0, 0, 0))
  pygame.draw.line(screen, GREEN, [0, 0], [100,100], 5)
  drawPlayer(shipX)

  #This function call updates the screen
  pygame.display.update()

  #sets the frame rate
  clock.tick(60)

#quits the pygame module 
pygame.quit() 
quit() 