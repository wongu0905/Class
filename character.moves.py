from pico2d import *
import os

os.chdir('c:\\python')
open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')

x = 0
while x < 800:
	clear_canvas()
	gra.draw(400, 30)
	ch.draw(x, 85)
	x += 2
	update_canvas()
	delay(0.01)
	get_events()
	

delay(1)

close_canvas()
