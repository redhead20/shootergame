import utime
import machine

B1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)  #C to 3.3v, NO to GPIO 14

B1_clicks = 0

def round_counter():
    global B1_clicks
    if B1.value():  #Was the B1 button pushed?
        B1_clicks += 1
    if B1_clicks > 4:
        print('Rnds: {}'.format(B1_clicks))
        utime.sleep(0.25)  #Pause
    else:
        print('Rnds: -{}'.format(B1_clicks))
        utime.sleep(0.25)  #Pause 
