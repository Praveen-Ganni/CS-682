#PYTHON SCRIPT

from datetime import datetime,timezone
import time
from dateutil.relativedelta import relativedelta
from PIL import Image,ImageDraw,ImageFont

def format_and_show_message(ccinfo,display,image1,draw):
    CD1 = [datetime.fromisoformat(ccinfo[0]["timestamp"]),ccinfo[0]["labels"][1]]
    NH1 = [ccinfo[2]]
    R1 = [ccinfo[1]["initial"],datetime.fromisoformat(ccinfo[1]["timestamp"]),ccinfo[1]["rate"],ccinfo[1]["labels"][0]]
    NH2 = [ccinfo[3]]
    while True:
        le = 0
        news_headline1 = NH1[0]+".  "
        while le != 60:
            now = datetime.now(timezone.utc)
            deadline_delta = relativedelta(CD1[0], now)
            years = deadline_delta.years
            rdays = relativedelta(months=deadline_delta.months, days=deadline_delta.days)
            days = ((rdays + now) - now).days
            hours = deadline_delta.hours
            minutes = deadline_delta.minutes
            seconds = deadline_delta.seconds
            message_list=[[years,days,str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)],news_headline1]
            show(message_list,display,image1,draw)
            time.sleep(1)
            news_headline1_list = list(news_headline1)
            news_headline1_list.append(news_headline1_list.pop(0))
            news_headline1 = "".join(news_headline1_list)
            le += 1
        le = 0
        news_headline2 = NH2[0]+".  "
        while le != 60:
            t = (datetime.now(timezone.utc) - R1[1]).total_seconds()
            percent = R1[2] * t + R1[0]
            message_list = ["{}%".format(format(percent,".2f")),
                            news_headline2]
            show(message_list,display,image1,draw,message1=False)
            time.sleep(1)
            news_headline2_list = list(news_headline2)
            news_headline2_list.append(news_headline2_list.pop(0))
            news_headline2 = "".join(news_headline2_list)
            le += 1
    return 0

def show(message_list,display,image1,draw,message1=True):
    # Alternatively you can change the I2C address of the device with an addr parameter:
    #display = adafruit_ssd1305.SSD1305_I2C(128, 32, i2c, addr=0x31)

    # Clear the display.  Always call show after changing pixels to make the display
    # update visible!
    #display.fill(0)
    image1 = Image.new('1', (display.width, display.height))
    draw = ImageDraw.Draw(image1)
    draw.rectangle((0,0,display.width,display.height), outline=0, fill=0)
    #display.show()
    padding = -2
    top = padding
    bottom = display.height-padding
    font = ImageFont.truetype("arial.ttf",16)
    font2 = ImageFont.truetype("arial.ttf",7)
    font3 = ImageFont.truetype("arial.ttf",12)
    for index,value in enumerate(message_list):
        if index == 0:
            if message1:
                draw.text((0, top),str(value[0]) ,font=font,fill=255)
                draw.text((10, top+8),"YRS" ,font=font2,fill=255)
                draw.text((23, top),str(value[1]).zfill(3) ,font=font,fill=255)
                draw.text((48, top+8),"DAYS" ,font=font2,fill=255)
                draw.text((67, top),value[2] ,font=font,fill=255)
            else:
                draw.text((0,top),value,font=font3,fill=225)
        else:
            draw.text((0, top+14),value ,font=font,fill=255)
    display.image(image1)
    display.show()

    return 0
