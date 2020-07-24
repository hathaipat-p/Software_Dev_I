
#####################################
###  Name : Hathaipat Chumninoul  
###  Student ID : 6201012620244                
###  Date : 24/07/2020            
#####################################

import threading
import time
import pygame

def mandelbrot(c, max_iters=10):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

#create function thread
def thread_func(start,stop):
    scale = 0.006
    offset = complex(-0.55,0.0)
    for x in range(start,stop,10):
        for y in range(scr_h):
            re = scale*(x-w2) + offset.real
            im = scale*(y-h2) + offset.imag
            c = complex( re, im )
            color = mandelbrot(c, 63)
            r = (color << 6) & 0xc0
            g = (color << 4) & 0xc0
            b = (color << 2) & 0xc0
            sur = surface.set_at( (x,y), (255-r,255-g,255-b) )
        screen.blit( surface, (0,0) )
        pygame.display.update()

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 600,600
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

running = True

w2, h2 = scr_w/2, scr_h/2 # half width, half screen

while running:

    clock.tick(1)

    for n in range(10):
        tr = threading.Thread(target=thread_func, args=(n,scr_w-n))
        tr.start()
        tr.join()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
print( 'PyGame done...')