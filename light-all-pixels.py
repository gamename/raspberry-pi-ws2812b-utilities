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


    args = parser.parse_args()

    pixels = neopixel.NeoPixel(board.D18, args.max_pixels, brightness=BRIGHTNESS)

    GPIO.setwarnings(False)

    # Refer pins by their sequence number on the board
    GPIO.setmode(GPIO.BCM)

    while True:
        try:
            pixels.fill(WHITE)
        except KeyboardInterrupt:
            pixels.fill(OFF)
            exit()


if __name__ == '__main__':
    main()
