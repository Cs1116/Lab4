import time

from hal import hal_input_switch as switch
from hal import hal_led as led


def led_blink(delay):
    led.init()
    led.set_output(0,1)
    time.sleep(delay)
    led.set_output(0,0)
    time.sleep(delay)

def led_off():
    led.init()
    led.set_output(0,0)

def main():
    while True:
        switch.init()
        x = switch.read_slide_switch()
        if x == 1:
            led_blink(0.1)
            i = 0
        elif x == 0:
            if i == 50:
                led_off()
            elif i < 50:
                led_blink(0.05)
                i = i + 1


if __name__ == "__main__":
    main()

