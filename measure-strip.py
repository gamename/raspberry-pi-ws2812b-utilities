"""
When I cut a LED strip, I don't often know exactly how many pixels it has.  This utility was written
to help with that predicament. Basically, its guessing script.  You set the estimated length of your
strip and then try to light ONE pixel to verify it.  Rinse, repeat until you have the correct values.

There are probably better ways to do this, but it works for me.

NOTE: You have to run this with sudo.

Example:
    sudo python3 ./measure-strip.py --max_pixels 110 --test_pixel 103
"""
import board
import neopixel
import RPi.GPIO as GPIO
import argparse

# Colors
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
BRIGHTNESS = 1.0


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--max_pixels",
                        type=int,
                        action="store",
                        required=True,
                        dest="max_pixels",
                        help="The maximum number of pixels in the strip")

    parser.add_argument("--test_pixel",
                        type=int,
                        action="store",
                        required=True,
                        dest="test_pixel",
                        help="Turn on test pixel")

    args = parser.parse_args()

    pixels = neopixel.NeoPixel(board.D18, args.max_pixels, brightness=BRIGHTNESS)

    GPIO.setwarnings(False)

    # Refer pins by their sequence number on the board
    GPIO.setmode(GPIO.BCM)

    while True:
        try:
            pixels[args.test_pixel] = WHITE
        except KeyboardInterrupt:
            pixels.fill(OFF)
            exit()


if __name__ == '__main__':
    main()
