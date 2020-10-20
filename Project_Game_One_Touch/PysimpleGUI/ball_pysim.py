
import PySimpleGUI as sg     
import random
from colors import *

class ball_pysim():

    def __init__(self, canvas ):
        position_ball = [   (50,70) , (200,70) , (350,70) , 
                            (50,175) , (350,175) , 
                            (50,350) , (200,350) , (350,350)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 30
        self.color = random.choice(COLORS)
        self.x, self.y = random.choice(position_ball) 
        self.canvas = canvas

    def delete_ball(self):
        self.canvas.DeleteFigure(self.circle)

    def is_collided(self, face_x, face_y ):

        if self.x == 50 and self.y == 350 :
            if 0 < face_x  and face_x < 100 and 0 < face_y and face_y < 100:
                return True

        if self.x == 200 and self.y == 350 :
            if 500 <= face_x and face_x <= 600 and 0 <= face_y and face_y <= 100:
                return True

        if self.x == 350 and self.y == 350 :
            if 900 <= face_x and face_x <= 1100 and 0 <= face_y and face_y <= 100:
                return True

        if self.x == 50 and self.y == 175 :
            if 0 <= face_x and face_x <= 100 and 200 <= face_y and face_y <= 300:
                return True

        if self.x == 350 and self.y == 175 :
            if 900 <= face_x and face_x <= 1100 and 200 <= face_y and face_y <= 300:
                return True

        if self.x == 50 and self.y == 70 :
            if 0 <= face_x and face_x <= 100 and 500 <= face_y and face_y <= 600:
                return True

        if self.x == 200 and self.y == 70 :
            if 500 <= face_x and face_x <= 600 and 500 <= face_y and face_y <= 600:
                return True

        if self.x == 350 and self.y == 70 :
            if 900 <= face_x and face_x <= 1100 and 500 <= face_y and face_y <= 600:
                return True

        else : return False

