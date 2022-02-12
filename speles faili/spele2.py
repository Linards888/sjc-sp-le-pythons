from tkinter import *
import random
import keyboard
canvas_width = 600
canvas_height = 600
master = Tk()
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)

x1=300
y1=300
x2=150
y2=250
e=5
f="blue"

def salidzinam():
    global x2, y2, e, f, p11, p12, p21, p22, pl1, pl2, b2, b1, b3, pl3, p31, p32
    print(x2)
    print(y2)
    if x2==p11 and y2==p12 and pl1:
        e=10
        print("palielinam")
        w.delete(b1)
        p11 = random.randrange(50, 550, 10)
        p12 = random.randrange(50, 550, 10)
        pl1 = p12 + 7
        b1=w.create_line(p11, p12, p11, pl1, width=5, fill="blue" )

    if x2==p31 and y2==p32 and pl3:
        w.delete(b3)
        p31 = random.randrange(50, 550, 10)
        p32 = random.randrange(50, 550, 10)
        pl3 = p32 + 7
        b1=w.create_line(p31, p32, p31, pl3, width=5, fill="blue" )

    if x2==p21 and y2==p22 and pl2:
        w.delete(b2)
        p21 = random.randrange(50, 550, 10)
        p22 = random.randrange(50, 550, 10)
        pl2 = p22 + 7
        b2=w.create_line(p21, p22, p21, pl2, width=5, fill="red" )

    Start()

# W variant (uz augšu)
def uzaugsu():
    global x1, y1, x2, y2, e, f, pl3, p31, p32
    x2=x1+0
    y2=y1-10
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    x1=x2
    y1=y2
    print(x1)
    print(y1)
    salidzinam()

# D variants (pa labi)
def palabi():
    global x1, y1, x2, y2, e, f, pl3, p31, p32
    x2=x1 + 10
    y2 = y1 + 0
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    x1=x2
    y1=y2
    print(x1)
    print(y1)
    salidzinam()

# S variants (uz leju)
def uzleju():
    global x1, y1, x2, y2, e, f, pl3, p31, p32
    x2=x1+0
    y2=y1+10
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    x1=x2
    y1=y2
    print(x1)
    print(y1)
    salidzinam()

# A variants (pa kreisi)
def pakreisi():
    global x1, y1, x2, y2, e, f, pl3, p31, p32
    x2=x1 - 10
    y2 = y1 + 0
    w.create_line(x1, y1, x2, y2, width=e, fill=f )
    x1=x2
    y1=y2
    print(x1)
    print(y1)
    salidzinam()




def Start():
    global p11, p12, p21, p22, pl1, pl2, b1, b2, x1, y1, x2, y2, e, f, pl3, p31, p32
    w.pack()
    g = 259
    while g>0:
       k = input("virziens")
       if keyboard.is_pressed("w"):
           g = g - 1
           uzaugsu()
    
       if keyboard.is_pressed('s'):
           g = g - 1
           uzleju()
     
       if keyboard.is_pressed('d'):
           g = g - 1
           palabi()
    
       if keyboard.is_pressed('a'):
           g = g - 1
           pakreisi()
    
    mainloop()

def StartpaPusei():
    global p11, p12, p21, p22, pl1, pl2, b1, b2, b3, x1, y1, x2, y2, e, f, pl3, p31, p32
    w.pack()
    
    p11 = random.randrange(50, 550, 10)
    p12 = random.randrange(50, 550, 10)
    p21 = random.randrange(50, 550, 10)
    p22 = random.randrange(50, 550, 10)
    p31 = random.randrange(50, 550, 10)
    p32 = random.randrange(50, 550, 10)

    pl1 = p12 + 7
    pl2 = p22 + 7
    pl3 = p32 + 7

    b1=w.create_line(p11, p12, p11, pl1, width=5, fill="blue" )
    b3=w.create_line(p31, p32, p31, pl3, width=5, fill="blue" )
    b2=w.create_line(p21, p22, p21, pl2, width=5, fill="red" )
    Start()

def clicked1(event):
    global pStartRec, pStartTex, pSettingsRec, pSettingsTex
    w.delete(pStartRec, pStartTex, pSettingsRec, pSettingsTex)
    StartpaPusei()

def clicked2():
    print("Tagat esi settingos")

def jaj():
    global pStartRec, pStartTex, pSettingsRec, pSettingsTex
    w.pack()
    pStartRec = w.create_rectangle(0, 0, 600, 300, fill="grey40", outline="grey60")
    pStartTex = w.create_text(300, 100, text="Start", )
    w.tag_bind(pStartRec, "<Button-1>", clicked1) ## when the square is clicked runs function "clicked".
    w.tag_bind(pStartTex, "<Button-1>", clicked1) ## same, but for the text.
    pSettingsRec = w.create_rectangle(0, 300, 600, 600, fill="grey40", outline="grey60")
    pSettingsTex = w.create_text(50, 15, text="Settings")
    w.tag_bind(pSettingsRec, "<Button-1>", clicked2)
    w.tag_bind(pSettingsTex, "<Button-1>", clicked2)
    
    mainloop()
jaj()




