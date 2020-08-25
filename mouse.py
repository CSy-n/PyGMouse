import autopy
import math
import time
import random
import sys
import os
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

def mouse_move_delayed(x, y, delay=0.75):
  sx, sy = mouse_position()
  ct = st = current_time()

  end_time = delay + st

  while ct <= end_time:
    ct = current_time()
    cx, cy = mouse_position()

    nx = sx + (x - sx) * (ct - st) / delay
    ny = sy + (y - sy) * (ct - st) / delay

    if nx == x and ny == y:
        break
    if ny < 0:
        print(f"ny: {ny}, sy: {sy}, y: {y}, ct: {ct}, delay: {delay}")

    mouse_move(nx, ny)
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
        print("In Region!")
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



# def zig_zag(divisions, delay):
#     width, height = screen_size()
#     dw = width/divisions
#     dh = height/divisions

#     mouse_centre()

#     for division in range(1, divisions):
#         dx = division * dw
#         dy = division * dy
#         mouse_move_delayed(dx, dy, delay)
#         mouse_move_delayed(dx, dy, delay)
#         mouse_move_delayed(dw*(division+1), dh*division, delay)
#         mouse_move_delayed(dw*(division), dh*(division), delay)


def sine_mouse_wave():
    """
    Moves the mouse in a sine wave from the left edge of
    the screen to the right.
    """
    width, height = autopy.screen.size()
    height /= 2
    height -= 10  # Stay in the screen bounds.

    for x in range(int(width)):
        y = int(height * math.cos((2* TWO_PI * x) / width) + height)
        autopy.mouse.move(x, y)
        time.sleep(random.uniform(0.001, 0.003))




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
