# ---------------- ส่วน game ยังไม่เสร็จ -----------------#
import cv2
import numpy as np
import PySimpleGUI as sg 
from ball_pysim import *
from time import time

#color in hex
bt1 = {'size':(13,4), 'font':('Franklin Gothic Book', 20), 'button_color':("white",'#df6b77')}
bt2 = {'size':(13,2), 'font':('Franklin Gothic Book', 20), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')


def main_menu() :

    layout =[ 
            
            [sg.Text('ONE-TOUCH', size=(30,1), justification='center', text_color='White', font=('Franklin Gothic Book', 80, 'bold'))],
            [sg.Text('--------', size=(22, 8), font=('Segoe UI', 14), text_color='Black')],
            [sg.Text('--------', size=(45, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('START',**bt1),sg.Text('--------', size=(12, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('HOW TO PLAY ?',**bt1)] ,  
            [sg.Text('--------', size=(22, 2), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False, resizable=False).Finalize()
    window.Maximize()

    while True:
        button , values = window.read()
        if button == "START" :
            game()
            window.Close()

        if button == "HOW TO PLAY ?" :
            sg.popup('Touch/Click the ball through the camera , When you tap it there will show your score with coundown timer :P')

        if button == sg.WIN_CLOSED :
            break
            window.Close()


def game():

    #----------------open cv------------------#
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(r'C:\Users\User\workspace-software\Game\OpenCV\haarcascade_frontalface_default.xml')
    cap.set(3, 1280)
    cap.set(4, 720)
    #-----------------------------------------#

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('OpenCV Demo', size=(100, 1), justification='center', font='Helvetica 20')],
              [sg.T('                       ') , sg.Graph(canvas_size=(1280,720), graph_bottom_left=(0,0), 
                        graph_top_right=(400,400),key="canvas")],
              [sg.Button('Ball', size=(10, 1), font='Helvetica 14'),
               sg.Button('Exit', size=(10, 1), font='Helvetica 14') ]]

    # create the window and show it without the plot
    window = sg.Window('Demo Game PysimpleGUI', layout).Finalize() 
    window.maximize()  

    canvas = window['canvas']

    ball = ball_pysim(canvas)        

    while True:
        
        circle = canvas.DrawCircle((ball.x, ball.y), ball.r, fill_color=ball.color, line_color='black')

        event, values = window.read(timeout=60)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'Ball':
            canvas.DeleteFigure(circle)
            ball = ball_pysim(canvas)

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
       
        canvas.DrawImage(data=imgbytes, location=(0, 400))


def score() :

    layout =[

            [sg.Text('ONE-TOUCH', size=(30,2), justification='center', text_color='White', font=('Franklin Gothic Book', 80, 'bold'))],
            [sg.Text('--------', size=(30, 2), font=('Segoe UI', 14), text_color='Black'),sg.Text('SCORE : ', size=(10, 2), font=('Segoe UI', 30), text_color='White'),sg.Text('', size=(15, 1), font=('Segoe UI', 30), text_color='White', key='score')],   
            [sg.Text('--------', size=(60, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('RESTART',**bt2),sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False, resizable=False).Finalize()
    window.Maximize()

    while True:
        button , values = window.read()
        if button == "RESTART" :
            main_menu()
            window.Close()

        if button == sg.WIN_CLOSED :
            break
            window.Close()

main_menu()
