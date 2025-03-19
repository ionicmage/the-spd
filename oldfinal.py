import turtle
import random
import time
import random
t = turtle.Turtle()
c = turtle.Screen()

playgame = True

score = 1
letter = 0
correct = 0
level = 0
letters = 0
x = letters
y = 0
letters = ("a")
t = turtle.Turtle()

def newletter():
	global y
	y = 100
	z = 0


for c in range(4):
    t.color(c)
    t.forward(750)
    t.left(90)
t.left(90)
t.forward(50)
t.right(90)
t.forward(750)

print("Very simple, type the letter before it hits the line for points")
while playgame:
	t.penup()
	t.goto(0,y)
	t.pendown()
	t.write(letters, font=("Arial", 16, "normal"))
	t.clear()
	y -= 1