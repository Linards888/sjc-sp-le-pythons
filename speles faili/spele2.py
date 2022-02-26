from tkinter import *
import random
import keyboard
import time

t=310
z=300
e=5
f="blue"
g = 200
x = 310
y = 310
a = 305
b = 305
direction = None

def move():
    global x_vel
    global y_vel
    global direction
    if direction is not None:
        w.move(rect, x_vel,y_vel)
    salidzinam()

def salidzinam():
    global e, f, p11, p12, p21, p22, pl1, pl2, b2, b1, b3, pl3, p31, p32, w
    if z==p11 and t==p12 and pl1:
        e=10
        print("palielinam")
        w.delete(b1)
        p11 = random.randrange(50, 550, 10)
        p12 = random.randrange(50, 550, 10)
        pl1 = p12 + 5
        b1=w.create_line(p11, p12, p11, pl1, width=5, fill="blue" )

    if z==p31 and t==p32 and pl3:
        w.delete(b3)
        p31 = random.randrange(50, 550, 10)
        p32 = random.randrange(50, 550, 10)
        pl3 = p32 + 5
        b1=w.create_line(p31, p32, p31, pl3, width=5, fill="blue" )

    if z==p21 and t==p22 and pl2:
        w.delete(b2)
        p21 = random.randrange(50, 550, 10)
        p22 = random.randrange(50, 550, 10)
        pl2 = p22 + 5
        b2=w.create_line(p21, p22, p21, pl2, width=5, fill="red" )

    on_keypress()


def on_keypress(event):
    global direction, z, t, x_vel, y_vel
    if event.keysym == "Left":
        direction = "left"
        x_vel = -10
        y_vel = 0
        z = z - 10
        print(z)
        move()
    if event.keysym == "Right":
        direction = "right"
        x_vel = 10
        y_vel = 0
        z = z + 10
        print(z)
        move()
    if event.keysym == "Down":
        direction = "down"
        x_vel = 0
        y_vel = 10
        t = t + 10
        print(t)
        move()
    if event.keysym == "Up":
        direction = "up"
        x_vel = 0
        y_vel = -10
        t = t - 10
        print(t)
        move()

    mainloop()
    

def on_keyrelease(event):
    global direction
    direction = None



def StartpaPusei():
    global p11, p12, p21, p22, pl1, pl2, b1, b2, b3, e, f, pl3, p31, p32, coord, rect
    w.pack()
    
    window.bind_all('<KeyPress>', on_keypress)
    window.bind_all('<KeyRelease>', on_keyrelease)

    p11 = random.randrange(50, 550, 10)
    p12 = random.randrange(50, 550, 10)
    p21 = random.randrange(50, 550, 10)
    p22 = random.randrange(50, 550, 10)
    p31 = random.randrange(50, 550, 10)
    p32 = random.randrange(50, 550, 10)

    pl1 = p12 + 5
    pl2 = p22 + 5
    pl3 = p32 + 5

    b1=w.create_line(p11, p12, p11, pl1, width=5, fill="blue" )
    b3=w.create_line(p31, p32, p31, pl3, width=5, fill="blue" )
    b2=w.create_line(p21, p22, p21, pl2, width=5, fill="red" )

    coord = [305, 305, 300, 300]
    rect = w.create_rectangle(*coord, outline="#000000", fill="#00ff00")
    
    window.mainloop()
    on_keypress()

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


window = Tk()

canvas_width = 600
canvas_height = 600

#canvas and drawing
w=Canvas(window, height = canvas_height, width = canvas_width)
w.grid(row=0, column=0, sticky=W)

#capturing keyboard inputs and assigning to function


jaj()




