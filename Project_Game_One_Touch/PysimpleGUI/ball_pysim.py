import PySimpleGUI as sg     
import random
from colors import *

class ball_pysim():

    def __init__(self, canvas ):
        position_ball = [ (50,50) , (200,50) , (350,50) , 
                            (50,200) , (350,200) , 
                            (50,350) , (200,350) , (350,350)]
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        self.r = 20
        self.color = random.choice(COLORS)
        self.x, self.y = random.choice(position_ball) 
        self.canvas = canvas
