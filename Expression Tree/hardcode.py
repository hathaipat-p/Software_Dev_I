###################################################################
# Name : Hathaipat Chumninoul
# Student ID : 6201012620244
# Date: 2020-08-06
# Expression Tree
# hardcode
###################################################################

import pygame

pygame.init()
pygame.font.init()

scr_w , scr_h = 400,400
screen = pygame.display.set_mode((scr_w,scr_h))
pygame.display.set_caption('Expression Tree')
text_font = pygame.font.SysFont('FreesiaUPC', 30)


white = 255,255,255
black = 0,0,0

def create_text(text,x,y):
    text_surface = text_font.render( text, False, black )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    screen.blit( text_surface , text_rect )
    #text_rect = [x,y,text_w,text_h]
    return 0

class node():
    def __init__(self,value,x,y):
        self.value = value
        self.r = 20
        self.x = x
        self.y = y
        self.draw = pygame.draw.circle(screen, white, (self.x,self.y), self.r ,0)
        self.draw_ = pygame.draw.circle(screen, black, (self.x,self.y), self.r ,1)
        self.text = create_text(self.value, self.x, self.y)
        self.left_node = None
        self.right_node = None
  
w , h = scr_w//8 , scr_h//5

w_list = []
h_list = []

for i in range(1,8):
    w_list.append(i*w)
for i in range(1,5):
    h_list.append(i*h)

running = True

while running:

    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.image.save( screen, 'image.jpg' )

    
    pygame.draw.line(screen, black, (w_list[3],h_list[0]) , (w_list[1],h_list[1]), 1)
    pygame.draw.line(screen, black, (w_list[3],h_list[0]) , (w_list[5],h_list[1]), 1)
    r1 = node('+',w_list[3],h_list[0])
    
    pygame.draw.line(screen, black, (w_list[1], h_list[1]) , (w_list[0], h_list[2]), 1)
    pygame.draw.line(screen, black, (w_list[1],h_list[1]) , (w_list[2],h_list[2]), 1)
    r2 = node('&',w_list[1],h_list[1])
    node('I0',w_list[0],h_list[2])
    node('I1',w_list[2],h_list[2])

    pygame.draw.line(screen, black, (w_list[5],h_list[1]) , (w_list[5],h_list[2]), 1)
    pygame.draw.line(screen, black, (w_list[5],h_list[2]) , (w_list[4],h_list[3]), 1)
    pygame.draw.line(screen, black, (w_list[5],h_list[2]) , (w_list[6],h_list[3]), 1)
    
    r3 = node('!',w_list[5],h_list[1])
    r4 = node('&',w_list[5],h_list[2])
    node('I1',w_list[4],h_list[3])
    node('I2',w_list[6],h_list[3])
    
    pygame.display.update()

pygame.quit()

print('...Exit...')
