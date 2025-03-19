import random
import turtle

score = 0
roll = 0
point = 0
theroll = 0

t = turtle.Turtle()

def randomnum():
  n = random.randrange(1,7)
  return n
  print n

dice1 = randomnum()
dice2 = randomnum()
thesum = dice1 + dice2
m = str(input("roll the dice?"))

if m == 'y':
  t.pendown()
  #for l in range(4):
    #t.forward(100)
    #t.right(90)
  if thesum == 1:
    score = 1
    print("you rolled a 1")
    for q in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.penup()
  if thesum == 2:
    score = 3
    print("You rolled a 2")
    for l in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(10,20)
    t.pendown()
    t.forward(5)
    t.penup()
  if thesum == 3:
    score = 3
    print("You rolled a 3")
    for m in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(10,20)
    t.pendown
    t.forward(5)
    t.penup()
    t.goto(20,40)
    t.pendown
    t.forward(5)
    t.penup()
  if thesum == 4:
    score = 4
    print("You rolled a 4")
    for l in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.pendown()
    t.goto(10,20)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(20,40)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(40,80)
    t.pendown
    t.forward(5)
    t.penup()
  if thesum == 5:
    score = 5
    print("You rolled a 5")
    for l in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(10,20)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(20,40)
    t.pendown
    t.forward(5)
    t.penup()
    t.goto(40,80)
    t.pendown
    t.forward(5)
    t.penup()
  if thesum == 6:
    roll = 6
    print ("you rolled a 6")
    while roll == 6:
      theroll = thesum + 1
    if theroll == 7:
      roll = 7
    elif thesum == 7:
      print("gameover")
  if thesum == 7:
    score = 7
    print("You rolled a 7")
    for l in range(4):
      t.forward(50)
      t.right(90)
    t.penup()
    t.goto(5,10)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(10,20)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(20,40)
    t.pendown
    t.forward(5)
    t.penup()
    t.goto(40,80)
    t.pendown
    t.forward(5)
    t.penup()
    t.goto(80,160)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(160,320)
    t.pendown()
    t.forward(5)
    t.penup()
    t.goto(320,640)
    t.pendown
    t.forward(5)
    t.penup()
    
  