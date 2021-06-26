from digitalio import DigitalInOut, Direction, Pull
import time
import board
import displayio
import adafruit_il0373
import terminalio
from adafruit_display_text import label
import random

print("Imports Done! Let's get started")

# button
door_button = DigitalInOut(board.A4)
door_button.direction = Direction.INPUT
door_button.pull = Pull.UP

BLACK = 0x000000
WHITE = 0xFFFFFF
RED = 0xFF0000
# Used to ensure the display is free in CircuitPython
displayio.release_displays()
# Define the pins needed for display use
spi = board.SPI()
epd_cs = board.D9
epd_dc = board.D10
epd_reset = board.D5
epd_busy = board.D6

# Create the displayio connection to the display pins
display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset, baudrate=1000000)
time.sleep(1)  # Wait a bit

DISPLAY_WIDTH = 296
DISPLAY_HEIGHT = 128

# Create the display object - the third color is red (0xff0000)
display = adafruit_il0373.IL0373(
    display_bus,
    width=DISPLAY_WIDTH,
    height=DISPLAY_HEIGHT,
    rotation=90,
    busy_pin=epd_busy,
    highlight_color=0xFF0000,
)

# Create a display group for our screen objects
g = displayio.Group()
print("Please wait during startup safety buffer")
time.sleep(200)
while True:
    print("While Statement Started")
    if not door_button.value:
        print("Door is open")
        # select a random number to select a random quote
        # (adjust second number to the number of quotation images)
        quote_number = random.randint(1, 35)

        # Display a graphic from the root directory of the CIRCUITPY drive
        f = open(f"FLLresources/images/quote{quote_number}.bmp", "rb")

        pic = displayio.OnDiskBitmap(f)
        # Create a Tilegrid with the bitmap and put in the displayio group
        t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
        g.append(t)

        # time.sleep(display.time_to_refresh)
        # time.sleep(200)
        print("Wake up! Time to display the quote")

        # Place the display group on the screen
        display.show(g)

        # NOTE: Do not refresh eInk displays sooner than 180 seconds
        display.refresh()
        print("Time to update the visit count and then nap")
        visit_file = open("FLLresources/visit_count.txt", 'r+')
        visit_count = int(visit_file.read())
        visit_count += 1
        visit_file.seek(0)
        visit_file.write(str(visit_count))
        visit_file.close()
        time.sleep(200)
        # Draw simple text using the built-in font into a displayio group
        g.pop()
        # Display homescreen image
        f = open("FLLresources/images/eInkHomescreen.bmp", "rb")

        pic = displayio.OnDiskBitmap(f)
        # Create a Tilegrid with the bitmap and put in the displayio group
        t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
        g.append(t)

        # For smaller text, change scale=2 to scale=1
        text_group = displayio.Group(max_size=10, scale=2,
                                     x=DISPLAY_WIDTH - 195,
                                     y=DISPLAY_HEIGHT - 20)
        # Need to put in code that reads visit variable to visit_count
        visit_text = str(visit_count)
        text_area = label.Label(terminalio.FONT, text=visit_text, color=RED)
        text_group.append(text_area)
        g.append(text_group)

        text_group = displayio.Group(max_size=10, scale=1,
                                     x=DISPLAY_WIDTH - 145,
                                     y=DISPLAY_HEIGHT - 15)
        visit_text = "visits...and counting!"
        text_area = label.Label(terminalio.FONT, text=visit_text, color=BLACK)
        text_group.append(text_area)
        g.append(text_group)

        # Place the display group on the screen
        display.show(g)

        # NOTE: Do not refresh eInk displays sooner than 180 seconds
        # time.sleep(display.time_to_refresh)
        print("Wake up! It's time to show the visits!")
        display.refresh()
        g.pop()
        g.pop()
        g.pop()
        time.sleep(200)
    else:
        time.sleep(2)
        print("Door is closed")