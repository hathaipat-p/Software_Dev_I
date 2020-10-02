# ---------------------------------------------------------- using OpenCV with pygame ------------------------------------------------------- #
# --------------- pygame กับ opencv ยังเป็นคนละหน้าต่างกัน ยังรวมกันไม่ได้ ใช้กล่องพร้อมกันไม่ได้ ถ้าใช้กล้องใน OpenCV กล้องใน pygame จะนิ่งไม่ทำงาน ---------------#
# -------------------- สามารถเล่นได้โดยดูตำแหน่งบอลจากหน้าต่าง pygame แล้วมาดูกล้องของ opencv ขยับให้ตรงตำแหน่งบอล บอลหาย ขึ้นลูกใหม่  ------------------- #

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
screen = pygame.display.set_mode((1280, 720) , pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1280, 720))
surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )


def open_camera( frame_size=(1280,720),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 


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


#--------------------------------------------------MAIN MENU------------------------------------------------------------#   

def main_menu():

    screen.fill(black)

    screen.blit(image, (350, 400))
    text_show('ONE TOUCH')
    text_howto('** HOW TO PLAY ? : Touch/Click the ball through the camera ',640,400)
    text_howto('when you tap it, there will show your score with coundown timer :P **',640,450)

    button_1 =  pygame.Rect(550,230,200,100)

    pygame.draw.rect(screen, red , button_1)

    create_text('START !',650,280)

    while True:

        mx1, my1 = pygame.mouse.get_pos()
        
        if button_1.collidepoint((mx1, my1)):
            if click:
                game()
    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def game():

    global count_score, cap

    #------- part opencv -----#
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(r'C:\Users\User\workspace-software\Game\OpenCV\haarcascade_frontalface_default.xml')
    #-------------------------#

    surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

    camera = open_camera()

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
        
        camera.start()
        img_non_flip = camera.get_image()
        img = pygame.transform.flip(img_non_flip,True,False)
        screen.blit( img , (0,0) )  

        pygame.draw.rect(screen, black , (0,0,1280,60))
        
        create_text('TIME : ' ,80,30)

        screen.blit(text, text_rect.center)
        
        create_text('SCORE :    ' + str(count_score) ,1150,30)

        mx2, my2 = pygame.mouse.get_pos()
        button_2 = pygame.Rect(1180,670,100,50) #(left,top,width,hight)

        pygame.draw.rect(screen, red , button_2)
        create_text('EXIT',1230,700)
        
        
        #------------------- part openCV ----------------#
        # Read the frame
        _, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720))
        frame = cv2.flip(frame, 1)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            if obj_ball.is_collided(x, y):
                surface1 = pygame.Surface( screen.get_size(), pygame.SRCALPHA )          #เหมือนการรีหน้า surface ใหม่เพื่อลบบอลออก
                count_score += 1
                pygame.time.wait(50)                                                #รอเวลาสักครู้เพื่อขึ้นลูกใหม่
                obj_ball = ball(surface1)
            print((x,y))

        #cv2.imshow('frame', frame)
        #cv2.waitKey(1)
        if counter == 0:
            break
            #cap.release()
            #cv2.destroyAllWindows()
        #------------------------------------------------#
    

        if button_2.collidepoint((mx2, my2)):
            if click:
                score()
                camera.stop()

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
                    time_up()
                    camera.stop()
                    cap.release()
                    cv2.destroyAllWindows()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    camera.stop()
                    cap.release()
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
    
        
def time_up():
    cap.release()
    cv2.destroyAllWindows()
    is_running = True  
    while is_running :

        screen.fill(black)
        screen.blit(image, (350, 400))
        text_show('ONE TOUCH')
        
        create_text('TIMES UP!',650,300)

        pygame.display.update()
        pygame.time.wait(3000)
        score()


def score():
    cap.release()
    cv2.destroyAllWindows()

    is_running = True  
    while is_running :

        screen.fill(black)
        screen.blit(image, (350, 400))
        text_show('ONE TOUCH')
        
        mx3,my3 = pygame.mouse.get_pos()
        button_3 = pygame.Rect(550,350,200,100)

        if button_3.collidepoint((mx3, my3)):
            if click:
                main_menu()
        
        pygame.draw.rect(screen, red , button_3)
        create_text('RESTART !',650,400)
        create_text('SCORE :    ' + str(count_score),650,280)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


main_menu()
