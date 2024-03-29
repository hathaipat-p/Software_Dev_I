#  6201012620244
#########  Assignment II (2020-07-15)  ########

import pygame
from random import *

pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('non-overlapping circles')

clock = pygame.time.Clock()

black = 0,0,0
white = 255,255,255

cir_place = []    # for position (x,y)
Name = []         
radius = []       # for radius

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b

# make 10 circles
def make_Circle():
    for i in range(10):
        r = randint(10,20)
        x = randrange(20,780,20)
        y = randrange(20,580,20) 
        color = random_color()
        
        val = pygame.draw.circle(screen, color, (x,y), r ,0)
        Name.append(val)
        cir_place.append((x,y))
        radius.append(r)
    return 0

# find circle to remove that choose from the circle with the most radius
def get_cir_rm():
    max_r = max(radius)
    for r in radius :
        if r == max_r: 
            c = radius[radius.index((r))]   # Let c = circle with the most radius
            index = radius.index((r))          # find index of circle with the most radius
            circle = Name[index]                      # Let circle = val of  circle 
            print("The largest circle is ", circle)
            return circle

# get the most radius
def get_r_rm():
    max_r = max(radius)
    for r in radius :
        if r == max_r: 
            return r 


def  del_data():
    circle = get_cir_rm()                     # circle = วงกลมที่จะลบ
    index = Name.index(circle)                # fin dindex of data about circle
    Name.remove(Name[index])                  # Remove val from Name
    cir_place.remove(cir_place[index])        # Remove position from cir_place
    radius.remove(radius[index])              # Remove radius from radius
    return 0    

# Draw
make_Circle()

running = True

while running :

    clock.tick(100)
    
    ev = pygame.event.get()

    #for x,y in cir_place :
    #    x += 5
    #    y += 5
    #    screen.fill((0,0,0))
    #   dot = pygame.draw.circle(screen, (250,0,0), (x,y),0)

    for event in ev:
        if event.type == pygame.QUIT:
            running = False

    for event in ev:
        if ( event.type == pygame.MOUSEBUTTONUP ):         # When click mouse 
            mouse_pos = pygame.mouse.get_pos()             # Location of the mouse-click
            circle_remove = get_cir_rm()                   # Select circle to remove 
            r = get_r_rm()
            if ( circle_remove.collidepoint( mouse_pos ) ):   # click inside circle 
                pygame.draw.circle(screen, black, mouse_pos, r*2 ,0)    # Draw another circle over selected circle (color is same background)
                del_data()                                  # delete data about removed circle from every list
   
    pygame.display.update()

pygame.quit()
