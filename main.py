import machine
import time
from utime import sleep

LED_COUNT = 9
BUTTON_START_ID = 16
BUTTON_COUNT = 3
INPUT_COUNT = 4
LED_GPIO_START = 7
last_button_time_stamp = 0
key_presses = []

def PinId(pin):
    return int(str(pin)[8:11].rstrip(","))

def interrupt_callback(pin):
    global last_button_time_stamp
    cur_button_timestamp = time.ticks_ms()
    button_press_delta = cur_button_timestamp - last_button_time_stamp
    if button_press_delta > 200:
        last_button_time_stamp = cur_button_timestamp
        key_presses.append(pin)
        print(f'Button pressed: {PinId(pin) - BUTTON_START_ID}')

def main():
    sleep(0.01)
    global key_presses
    global last_button_time_stamp

    s0 = machine.Pin(27, machine.Pin.OUT)
    s1 = machine.Pin(28, machine.Pin.OUT)
    mux_in = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)

    buttons = []
    for button_id in range(BUTTON_COUNT):
        buttons.append(machine.Pin(BUTTON_START_ID + button_id, machine.Pin.IN, machine.Pin.PULL_DOWN))
        buttons[-1].irq(trigger=machine.Pin.IRQ_FALLING, handler=interrupt_callback)

    PASS_CODE = [buttons[0], buttons[2], buttons[1]]
    PASSCODE_LENGTH = len(PASS_CODE)

    output_pins = []
    for output_id in range(LED_COUNT):
        output_pins.append(machine.Pin(LED_GPIO_START + output_id, machine.Pin.OUT))

    prev_val = -1
    while True:
        binary_code = 0
        for sel_val in range(INPUT_COUNT):
            s0.value(sel_val % 2)
            sleep(0.02)
            s1.value(sel_val // 2)
            sleep(0.02)
            binary_code += (pow(2, sel_val) * mux_in.value())

        if prev_val != binary_code:
            prev_val = binary_code
            print(f'selected output: {prev_val}')
            sleep(0.2)

        if len(key_presses) >= PASSCODE_LENGTH:
            if key_presses[:PASSCODE_LENGTH] == PASS_CODE:
                print('RIGHT PASS!')
                if  binary_code < LED_COUNT:
                    print(f'toggling: {binary_code}')
                    output_pins[binary_code].toggle() 
                else:  
                    print('Selected output is out of range. Valid range: 0-8')
            else:
                print('WRONG PASS TRY AGAIN')
            print(' ')
            key_presses = key_presses[PASSCODE_LENGTH:]

if __name__ == "__main__":
    main()
