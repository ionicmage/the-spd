import turtle
t = turtle.Turtle()

x = 0
for s in range(4):
  t.forward(300)
  t.right(90)
for m in range(8):
  t.goto(x, 0)
  x = x + 100
  t.forward(90)
  t.right(90)