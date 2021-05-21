
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

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

img = None
is_running = True 
while is_running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
                
    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

    # draw (MxN) tiles of the images
    M,N = 10,8
    rw, rh = scr_w//M, scr_h//N
    for i in range(M):
        for j in range(N):
            # draw a green frame (tile)
            rect = (i*rw, j*rh, rw, rh)
            pygame.draw.rect( img, (0,255,0), rect, 1)
            surface.blit( img, rect, rect )

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################
                  