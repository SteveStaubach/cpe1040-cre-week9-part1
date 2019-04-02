from microbit import *
import random
import utime
pause = 1200
start = 0
active = False
screen = 0

x = 0
y = 0
bits = []
while True:
    #Blinking Cursor
    cursor = display.set_pixel(x,y,7)
    sleep(100)
    if active:
        cursor = display.set_pixel(x,y,1)
        sleep(100)
    else:
        cursor = display.set_pixel(x,y,0)
        sleep(100)

    if button_b.is_pressed():
        start = utime.ticks_ms()
        while True:
            if not button_b.is_pressed():
                break

        if utime.ticks_diff(utime.ticks_ms(), start) < pause:
            if screen == 0:

                #Bit pattern
                if active:
                    bits.append('1')
                else:
                    bits.append('0')

                #Move Cursor
                if x + y == 8:
                    display.clear()
                    screen = 1
                    x = 0
                    y = 0
                    active = False
                elif x < 4:
                    x = x + 1
                    active = False
                else:
                    x = 0
                    y = y + 1
                    active = False

            else:

                #Bit pattern
                if active:
                    bits.append('1')
                else:
                    bits.append('0')

                #Move Cursor
                if x and y == 1:
                    display.clear()
                    bitstring = ''.join(bits)
                    display.scroll(bitstring, delay=100)
                elif x < 4:
                    x = x + 1
                    active = False
                else:
                    x = 0
                    y = y + 1
                    active = False

        else:
            if screen == 0:
                screen = (screen + 1) % 2
                display.clear()
                x = 0
                y = 0

    elif button_a.is_pressed():

        if display.get_pixel(x,y) == 0:
            active = True
        else:
            active = False