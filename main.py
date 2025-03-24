from lib import satz_bauen
import os
import RPi.GPIO as GPIO
import time

pin_grn = 6
pin_ylw = 13
pin_red = 19
pin_blk = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup([pin_grn, pin_ylw, pin_red, pin_blk], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def print_text(text):

    with open("/dev/usb/lp0", "w") as printer:
        printer.write("**************" + "\n")
        printer.write("\f" + "\n")
        printer.write(text + "\n")
        printer.write("\f" + "\n") 
        printer.write("**************" + "\n")
        printer.write("\f" + "\n")
        printer.write("\f" + "\n")
        printer.flush()

def replace_umlauts(text):
    replacements = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "ß": "ss",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue"
    }
    for umlaut, replacement in replacements.items():
        text = text.replace(umlaut, replacement)
    return text

def handle_green():
    weisheit = satz_bauen.weisheiten()
    print("red")
    clean_text = replace_umlauts(weisheit)
    print(clean_text)
    print_text(clean_text)
    time.sleep(1)

def handle_yellow():
    schnupfe = satz_bauen.schnupfspruch()
    print("ylw")
    clean_text = replace_umlauts(schnupfe)
    print(clean_text)
    print_text(clean_text)
    time.sleep(1)

def handle_red():
    flueche = satz_bauen.form_sentence()
    print("grn")
    clean_text = replace_umlauts(flueche)
    print(clean_text)
    print_text(clean_text)
    time.sleep(1)

def handle_black():
    gespraech = satz_bauen.frage_stellen()
    print("ylw")
    clean_text = replace_umlauts(gespraech)
    print(clean_text)
    print_text(clean_text)
    time.sleep(1)


button_actions = {
    pin_grn: handle_green,
    pin_ylw: handle_yellow,
    pin_red: handle_red,
    pin_blk: handle_black
}

try:
    while True:
        for pin, action in button_actions.items():
            if GPIO.input(pin) == GPIO.LOW:
                action()
                time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting program")

