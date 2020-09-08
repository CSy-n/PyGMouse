
from mouse import *


width, height = screen_size()


sine_mouse_wave()

# Place cursor at centre of Screen
mouse_centre()

# Wait a moment. . .
time.sleep(1)


circle_mouse(300)

# Wait a moment. . .
time.sleep(0.8)



spiral_mouse(height / 2, 15) 

# iterations = 5
# for i in range(iterations):

#   # r - radius
#   # height - height
#   radius = i / iterations * (height / 2 - 30) 
#   spiral_mouse(30 + radius - 5)
#   print(f"Iteration: {i}; Radius: {radius}")
#   print(f"i / iterations: {i/iterations}; height: {height}")
#   # time.sleep(2)

# Wait a moment . . .
time.sleep(1)

zig_zag(4)
