from microbit import *
import random,utime
active,bits,pause,start,screen,x,y = False,[],1000,0,0,0,0
def bitstatesave():
    if active:
        bits.append('1')
    else:
        bits.append('0')
def bitstatetoggle():
    global active
    if display.get_pixel(x,y) == 0:
        active = True
    else:
        active = False
def cursor():
    cursor = display.set_pixel(x,y,6)
    sleep(50)
    if active:
        cursor = display.set_pixel(x,y,3)
    else:
        cursor = display.set_pixel(x,y,0)
    sleep(50)
def defaultmovement():
    global x,y
    if x < 4:
        x = x+1
    else:
        x,y = 0,y+1
def complexmovement():
    global x,y,active,screen
    if screen == 0:
        bitstatesave()
        if x == 4 and y == 4:
            x,y,screen = 0,0,1
            display.clear()
        else:
            defaultmovement()
    elif screen == 1:
        bitstatesave()
        if x == 1 and y == 1:
            x,y,screen = 0,0,2
            display.clear()
            bitstring = ''.join(bits)
            display.scroll(bitstring, delay=100)
        else:
            defaultmovement()
    elif screen == 2:
        if y < 4:
            y = y+1
        else:
            y = 0
    active = False
while True:
    if screen <= 1:
        cursor()
        while button_a.is_pressed():
            bitstatetoggle()
        if button_b.is_pressed():
            start = utime.ticks_ms()
            while True:
                if not button_b.is_pressed():
                    break
            if utime.ticks_diff(utime.ticks_ms(), start) < pause:
                complexmovement()
            else:
                while screen == 1:
                    complexmovement()
                while screen == 0:
                    complexmovement()
    else:
        if y == 0:
            display.show(Image('05105:05105:05105:05105:00550'))
        if y == 1:
            display.show(Image('05555:00510:00510:00510:05555'))
        if y == 2:
            display.show(Image('05555:05100:05550:05100:05100'))
        if y == 3:
            display.show(Image('05550:05105:05100:05105:05550'))
        if y == 4:
            display.show(Image('05550:05105:05550:05150:05105'))
        if button_b.is_pressed():
            while True:
                if not button_b.is_pressed():
                    break
            complexmovement()
