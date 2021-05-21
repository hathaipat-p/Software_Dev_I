import pygame
import datetime
 
GREEN = (0, 255, 0) 
BLUE  = (0, 0, 255) 

# initialize pygame
pygame.init()


# create a screen of width=600 and height=400
scr_w, scr_h = 600, 400
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Running Text') 

pygame.font.init() 
text_font = pygame.font.SysFont('FreesiaUPC', 40)


# create a clock
clock = pygame.time.Clock()

# set the initial value for x-position
x = scr_w

running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick(15) 

    # check four QUIT button event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('exit')


    dtime = datetime.datetime.now()
    time = dtime.time()

    date1 = "Fri, 10 Jul 2020 {}     " .format(time)
    date2 = "วันศุกร์ 10 กรกฎาคม 2563 {} " .format(time)

    
    text_surface1 = text_font.render( date1, False, BLUE )
    text_width, text_height = text_surface1.get_rect()[2:]

    text_surface2 = text_font.render( date2, False, GREEN )
    text_width, text_height = text_surface2.get_rect()[2:]    

    # fill the screen with white color
    screen.fill( (0,0,0) )

    # set the y position for text drawing
    y = scr_h//2 - text_height

    # show text on the screen
    screen.blit( text_surface1,(x,y) )
    screen.blit( text_surface2,(x+500,y-7) )

    # decrease the x position for the next text drawing
    x -= 4
    if x < -text_width:
        x = scr_w

    # update the entire display.
    pygame.display.flip()

pygame.quit()
