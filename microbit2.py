from microbit import *
import random
import utime
x = 0
y = 0
active = False
screen = 0
pause = 1200
bits = []
a0 = a1 = a2 = a3 = a4 = b0 = b1 = b2 = 0
b3 = b4 = c0 = c1 = c2 = c3 = c4 = d0 = 0
d1 = d2 = d3 = d4 = e0 = e1 = e2 = e3 = 0
e4 = f0 = f1 = f2 = f3 = f4 = g0 = g1 = 0
if display.get_pixel(0,0) == 1:
    a0 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(1,0) == 1:
    a1 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(2,0) == 1:
    a2 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(3,0) == 1:
    a3 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(4,0) == 1:
    a4 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(0,1) == 1:
    b0 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(1,1) == 1:
    b1 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(2,1) == 1:
    b2 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(3,1) == 1:
    b3 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(4,1) == 1:
    b4 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(0,2) == 1:
    c0 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(1,2) == 1:
    c1 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(2,2) == 1:
    c2 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(3,2) == 1:
    c3 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(4,2) == 1:
    c4 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(0,3) == 1:
    d0 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(1,3) == 1:
    d1 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(2,3) == 1:
    d2 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(3,3) == 1:
    d3 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(4,3) == 1:
    d4 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(0,4) == 1:
    e0 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(1,4) == 1:
    e1 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(2,4) == 1:
    e2 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(3,4) == 1:
    e3 = 1
    bits.append('1')
else:
    bits.append('0')
if display.get_pixel(4,4) == 1:
    e4 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(0,0) == 1:
    f0 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(1,0) == 1:
    f1 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(2,0) == 1:
    f2 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(3,0) == 1:
    f3 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(4,0) == 1:
    f4 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(0,1) == 1:
    g0 = 1
    bits.append('1')
else:
    bits.append('0')
if screen == 1 and display.get_pixel(1,1) == 1:
    g1 = 1
    bits.append('1')
else:
    bits.append('0')
bitstring = ''.join(bits)
display.scroll(bitstring, delay=100)
while True:
    cursor = display.set_pixel(x,y,7)
    sleep(186)
    while True:
        if not button_b.is_pressed():
            break
        elif screen == 0 and button_b.is_pressed():
            start = utime.ticks_ms()
            if utime.ticks_diff(utime.ticks_ms(), start) < pause:
                if x + y == 8:
                    display.clear()
                    screen = 1
                    x = 0
                    y = 0
                    break
                elif x < 4:
                    x = x + 1
                    break
                else:
                    x = 0
                    y = y + 1
                    break
            else:
                display.clear()
                screen = 1
                x = 0
                y = 0
        elif screen == 1 and button_b.is_pressed():
            start = utime.ticks_ms()
            if utime.ticks_diff(utime.ticks_ms(), start) < pause:
                if x == 1 and y ==1:
                    bitstring = ''.join(bits)
                    display.scroll(bitstring, delay=100)
                    break
                elif x < 4:
                    x = x + 1
                    break
                else:
                    x = 0
                    y = y + 1
                    break
            else:
                bitstring = ''.join(bits)
                display.scroll(bitstring, delay=100)
                break
    while True:
        if not button_a.is_pressed():
            break
        elif button_a.is_pressed():
            if x == 0 and y == 0:
                if display.get_pixel(x,y) == 0:
                    a0 = display.set_pixel(x,y,1)
                    break
                else:
                    a0 = display.set_pixel(x,y,0)
                    break
    if display.get_pixel(x,y) == 1:
        cursor = display.set_pixel(x,y,1)
        sleep(186)
    else:
        cursor = display.set_pixel(x,y,0)
        sleep(186)