import storage

# storage.remount("/FLLresources/visit_count.txt", False)

import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D12)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the the B button on the eink is pressed during startup, CircuitPython can write to the drive.
# Otherwise, if not pressed, the computer can edit the files
storage.remount("/", switch.value)