from pico2d import *
import os

os.chdir('c:\\python')

open_canvas()

ch = load_image('character.png')
ch.draw_now(300, 400)
