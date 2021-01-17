import pygame
import speech_recognition as spr
import webbrowser
from PIL import ImageTk,Image
import win32com.client as wincom
from datetime import datetime
from tkhtmlview import HTMLLabel
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import keyboard
import sys
import json
import htmldisplayer
speaking=False
mbd=False
speak = wincom.Dispatch("SAPI.SpVoice")
r=spr.Recognizer()
val=''
pygame.init()
win= pygame.display.set_mode((900,500))
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mbd=True
        if event.type==pygame.MOUSEBUTTONUP:
            mbd=False
    mouseposx,mouseposy=pygame.mouse.get_pos()
    buttonpresser=pygame.Rect(mouseposx,mouseposy,10,10)
    pygame.draw.rect(win,(0,0,255), buttonpresser)
    win.fill((16,16,16))
    speakbutton=pygame.Rect(300,450, 50,50)
    pygame.draw.rect(win,(16,16,16), speakbutton)
    noteframemain=pygame.Rect(650,0, 250,500)
    surface = pygame.image.load(BytesIO(htmldisplayer.displayhtml.htmldisplay(1, '<h1>hi</h1>'))).subsurface(0,0,30,30)
    pygame.draw.rect(win,(0,122,204), noteframemain)

    def fornow():
        speaking=True
        with spr.Microphone() as source:
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                jsonfile=json.load(open('repliesdata.json'))
                try:
                    jsonstr=(savedfile[f'{text}'])
                    speak.Speak(jsonstr)
                except:
                    speak.Speak("here's what i found")
                    if text=="quiz me anything":
                        print('for now')
            except:
                speak.Speak('i did not understand')
            speaking=False
    if  buttonpresser.colliderect(speakbutton):
        print('hover')
        if mbd:
            fornow()
    pygame.font.init()
    myfont = pygame.font.SysFont('Verdana', 30)
    notestitle = myfont.render('Notes', False, (0, 0, 0))
    win.blit(notestitle,(660,10))
    win.blit(surface,(50,100))
    with open('notes\\note1.txt', 'r')as f:
        fileread1=f.read()
        pygame.font.init()
        myfont = pygame.font.SysFont('Verdana', 20)
        note1 = myfont.render(f'{fileread1}', False, (0, 0, 0))
        print(fileread1)
        win.blit(note1,(660,70))
    with open('notes\\note2.txt', 'r')as f:
        fileread2=f.read()
        pygame.font.init()
        myfont = pygame.font.SysFont('Verdana', 20)
        note2 = myfont.render(f'{fileread2}', False, (0, 0, 0))
        win.blit(note2,(660,140))
    with open('notes\\note3.txt', 'r')as f:
        fileread3=f.read()
        pygame.font.init()
        myfont = pygame.font.SysFont('Verdana', 20)
        note3 = myfont.render(f'{fileread3}', False, (0, 0, 0))
        win.blit(note3,(660,210))
    
    pygame.display.flip()
sys.exit()
