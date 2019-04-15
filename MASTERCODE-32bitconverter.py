from microbit import *
from array import *
import random,utime
active,bits,counter,pause,start,screen,cordx,cordy = False,[],0,850,0,0,0,0
def bitstatesave():
    if active:
        bits.append('1')
    else:
        bits.append('0')
def bitstatetoggle():
    global active
    if display.get_pixel(cordx,cordy) == 0:
        active = True
    else:
        active = False
def cursor():
    cursor = display.set_pixel(cordx,cordy,6)
    sleep(50)
    if active:
        cursor = display.set_pixel(cordx,cordy,3)
    else:
        cursor = display.set_pixel(cordx,cordy,0)
    sleep(50)
def defaultmovement():
    global cordx,cordy
    if cordx < 4:
        cordx = cordx+1
    else:
        cordx,cordy = 0,cordy+1
def complexmovement():
    global cordx,cordy,active,bitstring,bitvalue,bituint,bitsint,bitfloat,screen
    if screen == 0:
        bitstatesave()
        if cordx == 4 and cordy == 4:
            cordx,cordy,screen = 0,0,1
            display.clear()
        else:
            defaultmovement()
    elif screen == 1:
        bitstatesave()
        if cordx == 1 and cordy == 1:
            cordx,cordy,screen = 0,0,2
            display.clear()
# Def bit values
            bitstring = ''.join(bits)
            bituint = int(bitstring,2)
            if (bits[0]) == '1':
                bits[:] = ['0' if x=='1' else '1' for x in bits]
                sbits = ''.join(bits)
                bitsint = (int(sbits,2)*(-1))-1
            else:
                bitsint = bituint
            bitfloat = array("i",bits)
            display.scroll("SELECTION MENU", delay=45)
            sleep(600)
        else:
            defaultmovement()
    elif screen == 2:
        if cordy < 4:
            cordy = cordy+1
        else:
            cordy = 0
    active = False
while True:
    cursor()
    if screen <= 1:
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
    if screen == 2:
        if cordy == 0:
            if counter == 0:
                display.scroll("USIGN", delay=45)
                counter = 1
            display.show(Image('05105:05105:05105:05105:00550'))
            if button_a.is_pressed():
                display.scroll(bituint, delay=100)
        elif cordy == 1:
            if counter == 0:
                display.scroll("INTGR", delay=45)
                counter = 1
            display.show(Image('05555:00510:00510:00510:05555'))
            if button_a.is_pressed():
                display.scroll(bitsint, delay=100)
        elif cordy == 2:
            if counter == 0:
                display.scroll("FLOAT", delay=45)
                counter = 1
            display.show(Image('05555:05100:05550:05100:05100'))
            if button_a.is_pressed():
                display.scroll(bitfloat, delay=100)
        elif cordy == 3:
            if counter == 0:
                display.scroll("ASCII", delay=45)
                counter = 1
            display.show(Image('00550:05101:05100:05101:00550'))
        elif cordy == 4:
            if counter == 0:
                display.scroll("RESET", delay=45)
                counter = 1
            display.show(Image('05550:05105:05550:05150:05105'))
        if button_b.is_pressed():
            while True:
                if not button_b.is_pressed():
                    break
            complexmovement()
            counter = 0