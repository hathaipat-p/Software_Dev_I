import pygame, sys
from pygame.locals import *
from ball import ball  
import pygame.camera
import cv2


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#rgb color
black = (0,0,0)
red = (161, 0, 0)
white = (250,250,250)

#font
text_font1 = pygame.font.Font('freesansbold.ttf', 80)
text_font2 = pygame.font.Font('freesansbold.ttf', 36)
text_font3 = pygame.font.Font('freesansbold.ttf', 20)

pygame.display.set_caption('One Touch')
#screen = pygame.display.set_mode((1280, 720) , pygame.FULLSCREEN)
screen = pygame.display.set_mode((1280, 720))
surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#picture bg
image = pygame.image.load(r'C:\Users\User\workspace-software\Game\ball.jpg') 

#draw button
def draw_rect(color,rect):
    pygame.draw.rect(screen, color , rect)

#show text ONE TOUCH
def text_show(text):
    text_surface = text_font1.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = (640,150)
    screen.blit( text_surface , text_rect )
    return 0

#draw text
def create_text(text,x,y):
    text_surface = text_font2.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = ( x,y )
    screen.blit( text_surface , text_rect )
    return 0

#show text how to play
def text_howto(text,x,y):
    text_surface = text_font3.render( text, False, white )
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit( text_surface , text_rect )
    return 0

#-------------- part opencv --------------#
camera = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(r'C:\Users\User\workspace-software\Game\OpenCV\haarcascade_frontalface_default.xml')
camera.set(3, 1280)
camera.set(4, 720)
#-----------------------------------------#

surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

obj_ball = ball(surface1)             #สร้างบอลลูกแรก

count_score = 0

#Timer
font = pygame.font.SysFont(None, 45)
counter = 60
text = font.render(str(counter), True, white)
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
text_rect = text.get_rect()
text_rect.center = (150,15)

running= True
while running:

    #------------------- part openCV ----------------#
    ret, frame = camera.read()
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame,1)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.transpose(frame)
    img = pygame.surfarray.make_surface(frame)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        pygame.draw.rect(img, (0,255,0), (x,y,x+w, y+h), 3)
        print((x,y))
        if obj_ball.is_collided(x, y):
            surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
            count_score += 1
            pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
            obj_ball = ball(surface1)
        
    #cv2.waitKey(1)

    #------------------------------------------------#

    screen.blit( img , (0,0) ) 

    pygame.draw.rect(screen, black , (0,0,1280,60))
    
    create_text('TIME : ' ,80,30)

    screen.blit(text, text_rect.center)
    
    create_text('SCORE :    ' + str(count_score) ,1150,30)

    mx2, my2 = pygame.mouse.get_pos()
    button_2 = pygame.Rect(1180,670,100,50) #(left,top,width,hight)

    pygame.draw.rect(screen, red , button_2)
    create_text('EXIT',1230,700)
    

    if button_2.collidepoint((mx2, my2)):
        if click:
            score()

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            counter -= 1
            text = font.render(str(counter), True, white)
            if counter == 0:
                pygame.time.set_timer(timer_event, 0)
                #time_up()
                camera.release()
                cv2.destroyAllWindows()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit() 
                sys.exit()
                camera.release()
                cv2.destroyAllWindows()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if obj_ball.is_collided(mx2, my2):
                surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
                count_score += 1
                pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                obj_ball = ball(surface1)
        
    
    screen.blit( surface1 , (0,0) )

    pygame.display.update()
    clock.tick(60) 
    
