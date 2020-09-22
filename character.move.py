from pico2d import *
import os

os.chdir('c:\\python')
open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')

x = 0
while x < 800:
	clear_canvas_now()
	gra.draw_now(400, 30)
	ch.draw_now(x, 85)
	x += 2
	delay(0.02)
	
delay(1)

close_canvas()    
