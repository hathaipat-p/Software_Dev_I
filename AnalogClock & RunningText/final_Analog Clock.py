
#Ref. ในการหา position ของเข็มนาฬิกา https://zhuanlan.zhihu.com/p/127254433

import pygame
import time
import math

pygame.init()

radius = 300
x = 300
y = 300
angle = 0

red = 225,0,0
white = 210,210,210
green = 0,255,0
blue = 0,0,255
gray = 200,255,255
black = 0,0,0

screen = pygame.display.set_mode([800,800])

pygame.display.set_caption("Analog Clock")

background = pygame.image.load('D:\Me.jpg')

pygame.font.init()
text_font = pygame.font.SysFont('FreesiaUPC',30)

#สร้างฟังก์ชั่นหามุมของเข็มนาฬิกา
def get_sec():
    sec = time.strftime("%S")
    angle = (math.pi/30) * int(sec) - math.pi/2
    return angle
    
def get_min():
    mins = time.strftime("%M")
    angle = (math.pi/30) * int(mins) - math.pi/2
    return angle

def get_hour():
    hr = time.strftime("%I")
    angle =  (math.pi/6) * int(hr) - math.pi/2
    return angle

running = True

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    pygame.draw.circle(screen,white,(300,300),300,0)

    #แถบบอกช่วงของนาฬิกา เลข 3 6 9 12
    pygame.draw.line(screen, black, (300,590), (300,600), 12)
    pygame.draw.line(screen, black, (590,300), (600,300), 12)
    pygame.draw.line(screen, black, (300,0), (300,10), 12)
    pygame.draw.line(screen, black, (0,300), (10,300), 12)
    
    #แสดงตัวเลขเวลามุมซ้ายบน
    showtime = time.strftime("%I : %M : %S")
    text_surface =  text_font.render(showtime, False, gray)
    screen.blit(text_surface,(20,20))

    #การหา position ของปลายเข็มนาฬิกา
    hour_angle = get_hour()
    hour_x = math.cos(hour_angle) * (radius - 100)
    hour_y = math.sin(hour_angle) * (radius - 100)
    target = ( x+hour_x, y+hour_y )
    pygame.draw.line(screen, blue, (300,300), target, 25)

    min_angle = get_min()
    min_x = math.cos(min_angle) * (radius-50)
    min_y = math.sin(min_angle) * (radius-50)
    target = ( x+min_x, y+min_y )
    pygame.draw.line(screen, green, (300,300), target, 10)

    sec_angle = get_sec()
    sec_x = math.cos(sec_angle) * (radius-10)
    sec_y = math.sin(sec_angle) * (radius-10)
    target = ( x+sec_x, y+sec_y )
    pygame.draw.line(screen, red, (300,300), target, 4)


    pygame.display.update()

pygame.quit()