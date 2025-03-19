import turtle
c = turtle.Screen()
s = turtle.getscreen()
t = turtle.Turtle()
c.bgcolor("black")
t.pencolor("white")

howmany = int(input("How many squares would you like?:"))
b = 20
d = 30
for a in range(howmany):
  t.circle((a+1)*10)
  t.left(d)
  d = d + 10