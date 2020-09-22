import turtle as t

t.speed(0)

size = 40
count = 5
linelength = count * size

def line(start, end):
	t.penup
	t.goto(*start)
	t.pendown()
	t.goto(*end)

x1, y1 = t.pos()
x1, y2 = x1 + linelength, y1 + linelength

for i in range(count + 1):
	n = i * size
	line((x1, n), (x2, n))
	line((n, y1), (n, y2))

t.exitonclick()