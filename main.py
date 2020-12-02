from pprint import pprint
import pygame as pg
import random

from coisas.car import Car

pg.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        
SCREENWIDTH=400
SCREENHEIGHT=500
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption("Car Racing")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pg.sprite.Group()
 
playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)
 
#Allowing the user to close the window...
carryOn = True
clock=pg.time.Clock()
 
while carryOn:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                carryOn=False
                
        #Game Logic
        all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(GREEN)
        #Draw The Road
        pg.draw.rect(screen, GREY, [40,0, 200,300])
        #Draw Line painting on the road
        pg.draw.line(screen, WHITE, [140,0],[140,300],5)
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pg.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pg.quit()