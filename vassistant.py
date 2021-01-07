import tkinter as tk
import speech_recognition as spr
import webbrowser
from PIL import ImageTk,Image
import win32com.client as wincom
from datetime import datetime
from tkhtmlview import HTMLLabel
import requests
from bs4 import BeautifulSoup
import keyboard
speaking=False
speak = wincom.Dispatch("SAPI.SpVoice")
r=spr.Recognizer()
win=tk.Tk()
val=''
win.geometry('900x500')
win['background']='#101010'
def buttonpressed():
    speaking=True
    with spr.Microphone() as source:
       audio=r.listen(source)
       try:
           text=r.recognize_google(audio)
           if text=="hello":
               speak.Speak('hi')
           else:
               speak.Speak('now opening google')
               webbrowser.open(f'https://www.google.com/search?q={text}')
               
       except:
           speak.Speak('i did not understand')
       speaking=False
mah_image=Image.open("micicon.png")
my_image=ImageTk.PhotoImage(mah_image)
frame=tk.Frame(win, width=640, height=30)
frame.place(x=0, y=0)
e=tk.Entry(frame)
e.insert(0,'search about anything')
e.place(x=29, y=0, height=30, width=571)
def callback_e_focus(event):
    e.delete(first=0,last=21)
e.bind("<FocusIn>", callback_e_focus)
def btn2cmd ():
    webbrowser.open(f'https://www.google.com/search?q={e.get()}')
btn2=tk.Button(frame, text='search',command=btn2cmd)
noteframe=tk.Frame(win, width=261, height=500)
noteframe.place(x=641, y=0)
noteframe['bg']="#007acc"
btn2.place(x=600, y=0, height=30, width=40)
btn=tk.Button(win, text="press me",image=my_image,command=buttonpressed)
btn.place(x=300, y=460, height=30, width=29)
notetext=tk.Label(noteframe, text='notes', bg="#007acc")
notetext.place(x=70,y=0)
notetext.config(font=("Arial", 20))
noteholder1=tk.Frame(noteframe, width=261, height=60)
noteholder1.place(x=0, y=70)
noteholder1['bg']="#007acc"
with open('notes\\note1.txt', 'r') as f:
    note1=f.read()
e1=tk.Entry(noteholder1)
e1.place(x=0, y=47, height=13, width=231)
note11=tk.Label(noteholder1, text=f"{note1}",bg="#007acc")
note11.place(x=0, y=0)
def refresh():
    with open('notes\\note1.txt', 'r') as f:
       note1=f.read()
    noteremover=tk.Label(noteholder1, text=f"                                               ",bg="#007acc")
    noteremover.place(x=0, y=0)
def edit():
    with open('notes\\note1.txt', 'w') as f:
        f.write(e1.get())
        e1.delete(first=0,last=len(e1.get()))
    with open('notes\\note1.txt', 'r') as f:
        note1=f.read()
    refresh()
    note11=tk.Label(noteholder1, text=f"{note1}",bg="#007acc")
    note11.place(x=0, y=0)   
b1=tk.Button(noteholder1, text="done",command=edit)
b1.place(x=232, y=47, width=30, height=13)
noteholder2=tk.Frame(noteframe, width=261, height=60)
noteholder2.place(x=0, y=140)
noteholder2['bg']="#007acc"
with open('notes\\note2.txt', 'r') as f:
    note2=f.read()
e2=tk.Entry(noteholder2)
e2.place(x=0, y=47, height=13, width=231)
note21=tk.Label(noteholder2, text=f"{note2}",bg="#007acc")
note21.place(x=0, y=0)
def refresh2():
    with open('notes\\note2.txt', 'r') as f:
       note2=f.read()
    noteremover2=tk.Label(noteholder2, text=f"                                               ",bg="#007acc")
    noteremover2.place(x=0, y=0)
def edit2():
    with open('notes\\note2.txt', 'w') as f:
        f.write(e2.get())
        e2.delete(first=0,last=len(e2.get()))
    with open('notes\\note2.txt', 'r') as f:
        note2=f.read()
    refresh2()
    note21=tk.Label(noteholder2, text=f"{note2}",bg="#007acc")
    note21.place(x=0, y=0)   
b2=tk.Button(noteholder2, text="done",command=edit2)
b2.place(x=232, y=47, width=30, height=13)
noteholder3=tk.Frame(noteframe, width=261, height=60)
noteholder3.place(x=0, y=210)
noteholder3['bg']="#007acc"
with open('notes\\note3.txt', 'r') as f:
    note3=f.read()
e3=tk.Entry(noteholder3)
e3.place(x=0, y=47, height=13, width=231)
note31=tk.Label(noteholder3, text=f"{note3}",bg="#007acc")
note31.place(x=0, y=0)
def refresh3():
    with open('notes\\note3.txt', 'r') as f:
       note3=f.read()
    noteremover3=tk.Label(noteholder3, text=f"                                               ",bg="#007acc")
    noteremover3.place(x=0, y=0)
def edit3():
    with open('notes\\note3.txt', 'w') as f:
        f.write(e3.get())
        e3.delete(first=0,last=len(e3.get()))
    with open('notes\\note3.txt', 'r') as f:
        note3=f.read()
    refresh3()
    note31=tk.Label(noteholder3, text=f"{note3}",bg="#007acc")
    note31.place(x=0, y=0)   
b3=tk.Button(noteholder3, text="done",command=edit3)
b3.place(x=232, y=47, width=30, height=13)
calc=tk.Frame(noteframe,width=261,height=250)
calc.place(x=0, y=270)
calc['bg']='#323232'
result=tk.Label(calc,text=f'{val}', bg='#323232')
result.place(x=10, y=3, width=200, height=90)
def refreshcalc():
    hider=tk.Label(calc,text='                                  ', bg='#ffffff')
    hider.place(x=75,y=3)
    result=tk.Label(calc,text=f'{val}', bg='#ffffff')
    result.place(x=75, y=3, width=100, height=20)
def on_1_pressed():
    global val
    val1=val+'1'
    val=val1
    refreshcalc()
def on_2_pressed():
    global val
    val1=val+'2'
    val=val1
    refreshcalc()
def on_3_pressed():
    global val
    val1=val+'3'
    val=val1
    refreshcalc()
def on_4_pressed():
    global val
    val1=val+'4'
    val=val1
    refreshcalc()
def on_5_pressed():
    global val
    val1=val+'5'
    val=val1
    refreshcalc()
def on_6_pressed():
    global val
    val1=val+'6'
    val=val1
    refreshcalc()
def on_7_pressed():
    global val
    val1=val+'7'
    val=val1
    refreshcalc()
def on_8_pressed():
    global val
    val1=val+'8'
    val=val1
    refreshcalc()
def on_9_pressed():
    global val
    val1=val+'9'
    val=val1
    refreshcalc()
def on_0_pressed():
    global val
    val1=val+'0'
    val=val1
    refreshcalc()

def on_divide_pressed():
    global val
    val1=val+'/'
    val=val1
    refreshcalc()
def on_multiply_pressed():
    global val
    val1=val+'*'
    val=val1
    refreshcalc()
def on_plus_pressed():
    global val
    val1=val+'+'
    val=val1
    refreshcalc()
def on_minus_pressed():
    global val
    val1=val+'-'
    val=val1
    refreshcalc()
def on_C_pressed():
    global val
    val=''
    refreshcalc()
btnc1=tk.Button(calc,text='1',command=on_1_pressed, border=0)
btnc1.place(x=30, y=30, width=50, height=50)
btnc1=tk.Button(calc,text='2',command=on_2_pressed,border=0)
btnc1.place(x=80, y=30, width=50, height=50)
btnc1=tk.Button(calc,text='3',command=on_3_pressed, border=0)
btnc1.place(x=125, y=30, width=50, height=50)
btnc1=tk.Button(calc,text='4',command=on_4_pressed, border=0)
btnc1.place(x=175, y=30, width=50, height=50)
btnc1=tk.Button(calc,text='5',command=on_5_pressed, border=0)
btnc1.place(x=30, y=80, width=50, height=50)
btnc1=tk.Button(calc,text='6',command=on_6_pressed,border=0)
btnc1.place(x=80, y=80, width=50, height=50)
btnc1=tk.Button(calc,text='7',command=on_7_pressed, border=0)
btnc1.place(x=125, y=80, width=50, height=50)
btnc1=tk.Button(calc,text='8',command=on_8_pressed, border=0)
btnc1.place(x=175, y=80, width=50, height=50)
btnc1=tk.Button(calc,text='0',command=on_0_pressed, border=0)
btnc1.place(x=80, y=130, width=50, height=50)
btnc1=tk.Button(calc,text='+',command=on_plus_pressed,border=0)
btnc1.place(x=30, y=180, width=50, height=50)
btnc1=tk.Button(calc,text='C',command=on_C_pressed, border=0)
btnc1.place(x=175, y=130, width=50, height=50)
btnc1=tk.Button(calc,text='9',command=on_9_pressed, border=0)
btnc1.place(x=175, y=130, width=50, height=50)
btnc1.place(x=30, y=130, width=50, height=50)
btnc1=tk.Button(calc,text='-',command=on_minus_pressed,border=0)
btnc1.place(x=80, y=180, width=50, height=50)
btnc1=tk.Button(calc,text='/',command=on_divide_pressed, border=0)
btnc1.place(x=125, y=130, width=50, height=50)
btnc1=tk.Button(calc,text='*',command=on_multiply_pressed, border=0)
btnc1.place(x=125, y=180, width=50, height=50)
dateandtime=str(datetime.now())
win.mainloop()