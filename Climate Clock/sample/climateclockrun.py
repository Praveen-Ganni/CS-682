#PYTHON SCRIPT

from src.climate_clock_api import climateclock
from src.adafruit_oled_api import format_and_show_message
from PIL import ImageDraw
from PIL import Image
def main():
    try:
        from board import SCL, SDA
        import busio
        # Import the SSD1305 module.
        import adafruit_ssd1305

        # Create the I2C interface.
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1305 OLED class.
        # The first two parameters are the pixel width and pixel height.  Change these
        # to the right size for your display!
        display = adafruit_ssd1305.SSD1305_I2C(128, 32, i2c,addr=0x3C)
        image1 = Image.new('1', (display.width, display.height))
        draw = ImageDraw.Draw(image1)
        draw.rectangle((0,0,display.width,display.height), outline=0, fill=0)

        ccinfo=climateclock()
        format_and_show_message(ccinfo,display,image1,draw)
    except Exception as e:
        raise e
        print("Error : \n{}".format(e))
        return 1

    return 0

if __name__ == "__main__":
    main()