
from mouse import *




sine_mouse_wave()

# Place cursor at centre of Screen
mouse_centre()

# Wait a moment. . .
time.sleep(1)


for i in range(5):
  spiral_mouse(i * 30 + 30)

# Wait a moment . . .
time.sleep(1)

zig_zag(4)
