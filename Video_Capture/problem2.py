
###################################################################
# problem 2
# Name : Hathaipat Chumninoul
# Student ID : 6201012620244
# File: pygame_camera_demo-1.py
# Date: 2020-07-31
###################################################################
# กดช่องหนึ่งลากไปหาช่องหนึ่งแล้วปล่อย สองช่องนั้นภาพสลับกัน

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
rect_img = []

M,N = 5,5
rw, rh = scr_w//M, scr_h//N

for i in range(M):
    for j in range(N):
        rect = (i*rw, j*rh, rw, rh)
        rect_list.append(rect)
        rect_img.append(rect)
        
while is_running:

    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h

    # วาดกรอบสีเขียวและภาพ
    for i in range(len(rect_list)):
        pygame.draw.rect( img, (0,255,0), rect_list[i], 1)
        surface1.blit( img , rect_list[i], rect_img[i] ) 

    #click to appear the image
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            is_running = False

        global rect1 , rect2
        if ( event.type == pygame.MOUSEBUTTONDOWN ):     
            mouse_x1 , mouse_y1 = pygame.mouse.get_pos() 
            for i in range(M):
                for j in range(N):
                    if ( i*rw <= mouse_x1 <= (i+1)*rw  ):
                        if ( j*rh <= mouse_y1 <= (j+1)*rh ) :
                            rect1 = rect_list.index((i*rw, j*rh, rw, rh))  # เช็คว่า mouse กดที่ภาพไหน (หา index ของภาพใน rect_list)
                            
        elif ( event.type == pygame.MOUSEBUTTONUP ):        
            mouse_x2 , mouse_y2 = pygame.mouse.get_pos() 
            for i in range(M):
                for j in range(N):
                    if ( i*rw <= mouse_x2 <= (i+1)*rw  ):
                        if ( j*rh <= mouse_y2 <= (j+1)*rh ) :
                            rect2 = rect_list.index((i*rw, j*rh, rw, rh))  # เช็คว่า mouse กดที่ภาพไหน (หา index ของภาพใน rect_list)
                            #สลับภาพ 2 ตำแหน่ง
                            temp = rect_img[rect1]
                            rect_img[rect1] = rect_img[rect2]
                            rect_img[rect2] = temp

    # write the surface to the screen and update the display
    screen.blit( surface1, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################