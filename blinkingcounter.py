import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

visits = 0
print("No visitors so far.")
time.sleep(1)

while visits<10:
  DoorIsOpened = True
  if DoorIsOpened is True:
    visits += 1
    print(f"You are visitor #{visits}")
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(1)

if visits == 10:
    print("10 visits! Wow, this place is popular!!!!!")