"""
When I cut a LED strip, I don't often know exactly how many pixels it has.  This utility was written
to help with that predicament. Basically, its guessing script.  You set the estimated length of your
strip and then try to light ONE pixel to verify it.  Rinse, repeat until you have the correct values.

There are probably better ways to do this, but it works for me.

NOTE: You have to run this with sudo.

Example:
    sudo python3 ./measure-strip.py --max-pixels 110 --test-pixel 103
"""
import board
import neopixel
import RPi.GPIO as GPIO
import argparse

# Colors
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
BRIGHTNESS = 1.0


def restricted_int(x):
    """
    Restricts the value to be and integer
    :param x: The value to be restricted
    :return: The value if it is an integer
    """
    try:
        x = int(x)
    except ValueError:
        raise argparse.ArgumentTypeError("%r not an integer" % (x,))
    return x


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--max-pixels",
                        type=restricted_int,
                        action="store",
                        required=False,
                        default=100,
                        dest="max_pixels",
                        help="The maximum number of pixels in the strip")

    parser.add_argument("--test-pixel",
                        type=restricted_int,
                        action="store",
                        required=True,
                        dest="test_pixel",
                        help="Turn on test pixel")

    args = parser.parse_args()

    if args.test_pixel > args.max_pixels:
        raise ValueError("Test pixel cannot be greater than the maximum number of pixels in the strip")

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
