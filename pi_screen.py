from PIL import Image, ImageDraw, ImageFont
import os
import logging
from waveshare_epd import epd2in7
from gpiozero import Button

logging.basicConfig(level=logging.DEBUG)

CUR_IMAGE = 1
MAX_IMAGE = 3


def cycle_up():
    global CUR_IMAGE
    global MAX_IMAGE
    if CUR_IMAGE < MAX_IMAGE:
        CUR_IMAGE += 1
    else:
        CUR_IMAGE = 1
    logging.info(f"Image No. {CUR_IMAGE} selected")
    refresh()


def cycle_down():
    global CUR_IMAGE
    global MAX_IMAGE
    if CUR_IMAGE > 1:
        CUR_IMAGE -= 1
    else:
        CUR_IMAGE = MAX_IMAGE
    logging.info(f"Image No. {CUR_IMAGE} selected")
    refresh()


def clear():
    global CUR_IMAGE
    global MAX_IMAGE
    logging.info("Clearing Screen")
    CUR_IMAGE = 0
    refresh()


def refresh():
    epd.Clear(0xFF)
    draw_img(CUR_IMAGE)


def draw_img(img_number):
    base_img = Image.new("1", (epd.height, epd.width), 255)
    img = Image.open(os.path.join("pics", str(CUR_IMAGE) + ".png"))
    base_img.paste(img, (0, 0))
    epd.display(epd.getbuffer(base_img))


# initialize display
epd = epd2in7.EPD()
epd.init()

btn1 = Button(5)
btn2 = Button(6)
btn3 = Button(13)
btn4 = Button(19)

btn1.when_pressed = clear
btn2.when_pressed = cycle_up
btn3.when_pressed = cycle_down
btn4.when_pressed = refresh

while True:
    pass
