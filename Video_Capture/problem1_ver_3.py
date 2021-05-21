
###################################################################
# Name : Hathaipat Chumninoul
# File: pygame_camera_demo-1.py
# Date: 2020-07-25
###################################################################
# Update : ลบได้ทีละช่อง ทีละแถว เรียงจากบนลงล่าง

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

img = None
is_running = True 

rect_list = []
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
        surface1.blit( img, rect, rect )   

    # draw black rect and green frame on the images
    for i in range(len(black_rect_list)):
        pygame.draw.rect( img, (0,0,0), black_rect_list[i] , 0)
        pygame.draw.rect( img, (0,255,0), black_rect_list[i], 1)
        surface1.blit( img, rect_list[i], black_rect_list[i])

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )

        #click to appear the image
        if ( event.type == pygame.MOUSEBUTTONDOWN ):     
            mouse_x , mouse_y = pygame.mouse.get_pos() 
            for i in range(M):
                for j in range(N):
                    if ( i*rw <= mouse_x <= (i+1)*rw  ):
                        if ( j*rh <= mouse_y <= (j+1)*rh ) :
                            index_del = rect_list.index((i*rw, j*rh, rw, rh))
                            black_rect_list.pop(index_del)
                            print(black_rect_list)

    # write the surface to the screen and update the display
    screen.blit( surface1, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################