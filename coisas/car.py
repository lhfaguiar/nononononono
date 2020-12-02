import pygame as pg


WHITE = (255, 255, 255)
 
class Car(pg.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in pg.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pg.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        pg.draw.rect(self.image, color, [0, 0, width, height])
        
        # Instead we could load a proper pciture of a car...
        # self.image = pg.image.load("car.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    
    def moveUp(self, pixels):
        self.rect.y -= pixels
    
    def moveDown(self, pixels):
        self.rect.y += pixels