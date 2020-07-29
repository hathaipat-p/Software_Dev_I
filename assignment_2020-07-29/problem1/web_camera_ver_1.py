
###################################################################
# Name : Hathaipat Chumninoul
# File: pygame_camera_demo-1.py
# Date: 2020-07-25
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

scr_w, scr_h = 1280 , 720
pygame.init()
camera = open_camera()

if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

screen = pygame.display.set_mode((scr_w, scr_h))

surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
surface2 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

img = None
is_running = True 

rect_list = []
draw_list = []
black_draw_list = []
black_rect_list = []

M,N = 10,8
rw, rh = scr_w//M, scr_h//N

for i in range(M):
    for j in range(N):
        rect = (i*rw, j*rh, rw, rh)
        rect_list.append(rect)
        black_rect_list.append(rect)

while is_running:

    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

    # draw (MxN) tiles of the images
    for rect in rect_list:
        pygame.draw.rect( img, (0,255,0), rect, 1)
        surface1.blit( img, rect, rect )   

    # draw black rect on the images
    for rect in black_rect_list:
        black = pygame.draw.rect( img, (0,0,0), rect , 1000)
        pygame.draw.rect( img, (0,255,0), rect, 1)
        black_draw_list.append(black)
        surface1.blit( img, rect, rect)


    #click to appear the image
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )

        if ( event.type == pygame.MOUSEBUTTONUP ):        
            mouse_pos = pygame.mouse.get_pos() 
            for i in range(len(black_draw_list)):
                black_draw_rect = black_draw_list[i]       
                if ( black_draw_rect.collidepoint( mouse_pos ) ):
                    black_rect_list.pop(0)


    # write the surface to the screen and update the display
    
    screen.blit( surface1, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################