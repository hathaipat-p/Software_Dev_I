# --------------- เหลือปรับตำแหน่งให้ตรงกับหน้าในภาพ ----------------#

import PySimpleGUI as sg     
import random
from colors import *

class ball_pysim():

    def __init__(self, canvas ):
        position_ball = [   (50,60) , (200,60) , (350,60) , 
                            (50,200) , (350,200) , 
                            (50,350) , (200,350) , (350,350)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 50
        self.color = random.choice(COLORS)
        self.x, self.y = random.choice(position_ball) 
        self.canvas = canvas

    def delete_ball(self):
        self.canvas.DeleteFigure(self.circle)
    
    # ลองปรับตำแหน่ง
    def is_collided(self, facex, facey ):
        #if self.x-self.r < facex and facex < self.x+self.r and self.y-self.r < facey and facey < self.y+self.r:
        #    return True
        #else : return False

        if self.x == 50 and self.y == 60 :
            if 0 <= facex and facex <= 100 and 0 <= facey and facey <= 100:
                return True
        
        else : return False

        


