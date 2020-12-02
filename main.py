from pprint import pprint
import pygame as pg

from class.car import Car

pg.init()

# Define game colors
PINK = (0, 0.54, 0.226, 0.063)
WHITE = ( 255, 255, 255)
BLUE = (0,255,255)
BLACK = ( 255, 0, 0)

# Open a new window
size = (700, 500)
screen = pg.display.set_mode(size)
pg.display.set_caption("My First Game")


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()
  	
playerCar = Car(BLUE, 20, 30)

playerCar.rect.x = 200
playerCar.rect.y = 300
	
player1Car = Car(BLACK, 20, 30)
player1Car.rect.x = 200
player1Car.rect.y = 300


player2Car = Car(WHITE, 20, 30)
player2Car.rect.x = 400
player2Car.rect.y = 400

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
 
    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    pg.draw.rect(screen, RED, [55, 200, 100, 70],0)
    pg.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pg.draw.ellipse(screen, BLACK, [20,20,250,100], 2)


    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pg.quit()