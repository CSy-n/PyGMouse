import autopy
import math
import time
import random
import sys
import os
import math
from datetime import datetime

TWO_PI = math.pi * 2.0



def write_text(text, word_per_minute=None):
    autopy.key.write_string(text, words_per_minute)


def mouse_click(x=None, y=None, delay=None):
    autopy.mouse.click(delay=delay)

# Convenience wrapper around toggle() that holds down and then
# releases the given mouse button. By default, the left button is
# pressed.
# speed: float (pixels per second)

def mouse_move(x=None, y=None, speed=None):

    
  # print("Coords: ", x, y)

  if x is None:
      x = 0
  if y is None:
      y = 0
      
  if speed is None:
    autopy.mouse.move(x, y)
  else:
    mouse_move_delayed(x, y, speed)



# Simply an alias for `mouse_move'
def mouse_move_absolute(x=None, y=None, speed=None):
    mouse_move(x, y, speed)
    
# moves mouse relative to coordinates,
# Negative is left, positive is right
# CONSIDERATIONS:
# Exception for ValueError
def mouse_move_relative(dx=None, dy=None, delay=None):
  sx, sy = mouse_position()
  # print('dx, dy: ',dx, dy)

  if dx is None:
      mouse_move(sx, (sy + dy), delay)
  elif dy is None:
      mouse_move((sx + dx), sy, delay)
  else:
      mouse_move((sx + dx), (sy + dy), delay)

# Checks incase of time-excede bug
# CONSIDERATIONS:
# Handles Point out of Bounds Badly.
def mouse_move_delayed(x, y, delay=0.75):
  sx, sy = mouse_position()
  ct = st = current_time()

  et = delay + st

  while ct <= et:
    ct = current_time()
    cx, cy = mouse_position()

    nx = sx + (x - sx) * (ct - st) / delay
    ny = sy + (y - sy) * (ct - st) / delay

    # Incase the time is exceded
    if ct - et > 0:
      nx = x
      ny = y

    try:
      mouse_move(nx, ny)
    except Exception as e:
      print(f"nx: {nx}, sx: {sx}, x: {x}")
      print(f"ct: {ct}, st: {st}, et: {et}, delay: {delay}")
      print(e)
      print("="*80)
      print(f"(ct - st): {(ct - st)}")
      print(f"(x - sx): {(x - sx)}")
      raise e

    time.sleep(random.uniform(0.001, 0.003))


def mouse_position():
    return autopy.mouse.location() 


def screen_size():
    return autopy.screen.size()

# region is a tuple: (x, y, width, height)
def mouse_in_region(region):
    mx, my = mouse_position()
    rx, ry, width, height = region
    if mx > rx and mx < rx + width and my > ry and my < ry + height:
        return True
    return False


def screen_capture(region=None):
    if region is not None:
        x, y, width, height = region
        return autopy.bitmap.capture_screen( ((x,y), (width,height)) )
    return autopy.bitmap.capture_screen()

def screen_capture_save(path, region=None, name=None):
    if name is None:
        name = 'img-' + simple_date_text() + '.png'
    os.path.join(path, name)
    # Capture Region of Screen:
    image = capture_screen(region)
    image.save( os.path.join(path, name) )
    


def mouse_centre():
    width, height = autopy.screen.size()
    mouse_move(width / 2, height / 2)


def circle_mouse(radius, delay=1.5, resolution=100):
    width, height = screen_size()
    sx, sy = mouse_position()
    sx -= radius
    cw = width / 2

    # mouse_centre()

    # First we just want to make it go around a circle at 1 degrees
    for iteration in range(1, resolution + 1):
        nx = sx + radius * math.cos(math.radians(iteration * 360 / resolution))
        ny = sy + radius * math.sin(math.radians(iteration * 360 / resolution) )

        mouse_move_absolute(nx, ny, delay / resolution)


def swirl_mouse(radius, swirls=3, delay=1.5, resolution=100):
    width, height = screen_size()
    sx, sy = mouse_position()
    cw = width / 2
    sx -= radius
    
    
    # Bigger it is faster the gaps,

    # mouse_centre()

    # First we just want to make it go around a circle at 1 degrees
    for iteration in list(range(1, swirls * resolution + 1)) + list(range(swirls * resolution - 1, 0, -1)):
        r = radius * iteration / resolution
        nx = sx + r * math.cos(math.radians(iteration * 360 / resolution))
        ny = sy + r * math.sin(math.radians(iteration * 360 / resolution) )

        mouse_move_absolute(nx, ny, delay / resolution / swirls)
        
    mouse_move(sx, sy)

def zig_zag(divisions, delay=1.5):
    width, height = screen_size()

    # Offset for Region on Screen
    ox = width / 3
    oy = height / 5

    # Region Occupied accounted for Top-Bottom
    dw = width / divisions
    dh = (height - oy * 2) / divisions

    cw = width / 2

    # Set Mouse at Centre
    mouse_centre()

    for division in range(divisions):
        x = ox
        y = oy + division * dh
        mouse_move_delayed(x, y, delay)
        mouse_move_delayed(x + abs(ox - cw) * 2, y, delay)



def sine_mouse_wave():
    """
    Moves the mouse in a sine wave from the left edge of
    the screen to the right.
    """
    width, height = screen_size()
    height /= 2
    height -= 10  # Stay in the screen bounds.

    for x in range(int(width)):
        y = int(height * math.cos((2* TWO_PI * x) / width) + height)
        autopy.mouse.move(x, y)
        time.sleep(random.uniform(0.0006, 0.00009))




##############################
# 	UTILITIES
##############################

def negate_number(number):
    return -number

def simple_date_text():
    return datetime.strftime(datetime.now(), "%d-%m-%y:%M%S")

def current_time():
  return time.time()

def create_delay(delay):
    time.sleep(delay)

def distance_from(sp, ep): 
     sx, sy = sp 
     ex, ey = ep 
     return math.sqrt(  math.pow(abs( sx - ex), 2) +  math.pow(abs( sy - ey ), 2))

sine_mouse_wave()
