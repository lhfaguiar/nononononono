from pprint import pprint
import pygame as pg
import random

from coisas.car import Car
from utils.color import *

pg.init()
 
colorList = (colors)
 
 
SCREENWIDTH=800
SCREENHEIGHT=600
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pg.display.set_mode(size)
pg.display.set_caption("Cartas")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pg.sprite.Group()
 
# playerCar = Car(RED, 60, 80, 70)
# playerCar.rect.x = 160
# playerCar.rect.y = SCREENHEIGHT - 100

# Add the car to the list of objects
# all_sprites_list.add(playerCar)
# all_sprites_list.add(car1)
# all_sprites_list.add(car2)
# all_sprites_list.add(car3)
# all_sprites_list.add(car4)
 
# all_coming_cars = pg.sprite.Group()
# all_coming_cars.add(car1)
# all_coming_cars.add(car2)
# all_coming_cars.add(car3)
# all_coming_cars.add(car4)
 
 
#Allowing the user to close the window...
carryOn = True
clock=pg.time.Clock()
 
# while carryOn:
#         for event in pg.event.get():
#             if event.type==pg.QUIT:
#                 carryOn=False
#             elif event.type==pg.KEYDOWN:
#                 if event.key==pg.K_x:
#                      playerCar.moveRight(10)
 
#         keys = pg.key.get_pressed()
#         if keys[pg.K_LEFT]:
#             playerCar.moveLeft(5)
#         if keys[pg.K_RIGHT]:
#             playerCar.moveRight(5)
#         if keys[pg.K_UP]:
#             speed += 0.05
#         if keys[pg.K_DOWN]:
#             speed -= 0.05
 
 
        #Game Logic
        # for car in all_coming_cars:
        #     car.moveForward(speed)
        #     if car.rect.y > SCREENHEIGHT:
        #         car.changeSpeed(random.randint(50,100))
        #         car.repaint(random.choice(colorList))
        #         car.rect.y = -200
	
        # #Check if there is a car collision
        # car_collision_list = pg.sprite.spritecollide(playerCar,all_coming_cars,False)
        # for car in car_collision_list:
        #     print("Car crash!")
        #     #End Of Game
        #     carryOn=False
 
        # all_sprites_list.update()
 
        # #Drawing on Screen
        # screen.fill(GREEN)
        # #Draw The Road
        # pg.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
        # #Draw Line painting on the road
        # pg.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        # #Draw Line painting on the road
        # pg.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
        # #Draw Line painting on the road
        # pg.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)
 
 
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        # all_sprites_list.draw(screen)
 
        #Refresh Screen
        # pg.display.flip()
 
        #Number of frames per secong e.g. 60
        # clock.tick(60)
 
pg.quit()
