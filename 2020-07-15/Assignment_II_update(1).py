#  6201012620244
#########  Assignment II (2020-07-15)  ########

###  update  ####
#  bouncing at frame and can delete circle  #

import pygame , math
from random import *

pygame.init()


width = 800
heigth = 600
screen = pygame.display.set_mode([width,heigth])
pygame.display.set_caption('bouncing circles')

clock = pygame.time.Clock()

black = 0,0,0
white = 255,255,255

        
radius = []       # for radius

obj_cir = []

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b
    

class Circle():
    def __init__(self):
        self.x = randint(20,780)
        self.y = randint(20,580)
        self.r = randint(10,20)
        self.color = random_color()
        self.move_x = randrange(-2, 3)
        self.move_y = randrange(-2, 3)
        radius.append(self.r)
    
    def Draw(self):
        self.draw = pygame.draw.circle(screen, self.color, (self.x,self.y), self.r ,0)

    def Del(self):
        pygame.draw.circle(screen, black, (self.x,self.y), self.r ,0)


def get_cir_rm():
    max_r = max(radius)                      # find the most radius
    for r in radius :
        if r == max_r: 
            index = radius.index(r)          # find index of circle with the most radius
            circle = obj_cir[index]          # Let circle = val of  circle 
            return circle


def  del_data():
    circle = get_cir_rm()                    # circle = rm_cir.draw
    index = obj_cir.index(circle)            # find index of circle in list
    obj_cir.remove(circle)                   # Remove odject from obj_cir
    radius.remove(radius[index])             # Remove radius from radius
    return 0    


# check is curso inisde circle
def is_inside_cir(cir_x,cir_y,cir_r,mouse_x,mouse_y):                   
    if (cir_x - mouse_x)**2 + (cir_y - mouse_y)**2 <= cir_r**2 :
        return True
    else: return False


# bouncing at frame
# fill screen with background , find new position and redraw
def move_circle_frame():
    screen.fill(black)
    for n in range(len(obj_cir)):
        if len(obj_cir) >= 0 :
            if obj_cir[n].y > (heigth - obj_cir[n].r) or obj_cir[n].y < obj_cir[n].r:
                obj_cir[n].move_y *= -1
            if obj_cir[n].x > (width - obj_cir[n].r) or obj_cir[n].x < obj_cir[n].r:
                obj_cir[n].move_x *= -1

            obj_cir[n].x += obj_cir[n].move_x
            obj_cir[n].y += obj_cir[n].move_y

            obj_cir[n].draw = pygame.draw.circle(screen, obj_cir[n].color, (obj_cir[n].x,obj_cir[n].y), obj_cir[n].r ,0)
    return 0


# Draw
for i in range(10):
    obj_cir.append('c'+str(i))
    obj_cir[i] = Circle()
    for j in range(len(obj_cir)):
        if i != j:
            dist = int(math.hypot(obj_cir[i].x - obj_cir[j].x, obj_cir[i].y - obj_cir[j].y))
            if dist < int(obj_cir[i].r*2):
                continue
    obj_cir[i].Draw()

running = True

while running :

    clock.tick(80)
    
    ev = pygame.event.get()
    
    move_circle_frame()

    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        
        if len(obj_cir) == 0:           # if delete all circle close the screen
            running = False

        if ( event.type == pygame.MOUSEBUTTONUP ):         # When click mouse 
            mouse_pos = pygame.mouse.get_pos()             # Location of the mouse-click
            rm_cir = get_cir_rm()

            if is_inside_cir(rm_cir.x,rm_cir.y,rm_cir.r,mouse_pos[0],mouse_pos[1]):
                rm_cir.Del()            # make circle's color is black (make circle disappear)
                del_data()              # delete data about removed circle in everylist
                

    pygame.display.update()

pygame.quit()