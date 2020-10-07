
import pygame
import random

pygame.init()

class ball():

    def __init__(self,surface):
        position_ball = [ (100,150) , (100,590) , (1190,150) , (1190,590) ,
                        (100,350) , (1190,350) , (600,150) , (600,590)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 50
        self.color = (r,g,b)
        self.pos = random.choice(position_ball) 
        self.surface = surface
        self.draw = pygame.draw.circle( self.surface, self.color, self.pos, self.r ,0)
        self.circle = pygame.draw.circle( self.surface, (0,0,0), self.pos, self.r ,1)
        self.surface_size = surface.get_size()

    def is_collided(self,mx, my):
        if self.draw.collidepoint((mx, my)):
            return True
        else : return False
        
