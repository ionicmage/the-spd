import time
import turtle
c = turtle.Screen()
t = turtle.Turtle()

print("Hi there!")
time.sleep(1)
print("this is a two player game")
time.sleep(2)
print("Player One writes a word and hands the device to Player Two for them to guess")
time.sleep(2)
theword= str(input("put in a word:")) 

howlong = len(theword)
print(howlong)

print "you have", howlong, "guesses"

for g in range(howlong):
  t.goto(g*50, 0)
  t.pendown()
  t.forward(40)
  t.penup()
playgame = 1
correct = 0
body = 1
incorrect = 0

while playgame == 1:
  incorrect = 0
  guess = str(input("put in a letter to guess:"))
  for m in range(howlong):
    if guess == theword[m]:
      correct += 1
      incorrect = 1
      t.goto(m*50+15,10)
      t.pendown
      t.write(guess, font=("Arial", 16, "normal"))
      t.penup
  if incorrect == 0:
    print("incorrect,drawing head")
    if body == 1:
      t.goto(-100,50)
      t.pendown()
      t.circle(25)
      t.penup()
      body = 2
    elif body == 2:
      print("incorrect, drawing torso")
      body = 3
      t.goto(-100,40)
      t.pendown()
      t.right(90)
      t.forward(65)
      t.penup()
    elif body == 3:
      print("incorrect, drawing a leg")
      body = 4
      t.goto(-100,-30)
      t.pendown()
      t.right(55)
      t.forward(50)
      t.penup()
    elif body == 4:
      body = 5
      print("incorrect, drawing second leg")
      t.goto(-100,-30)
      t.pendown()
      t.right(-60)
      t.forward(50)
      t.penup()
    elif body == 5:
      body = 6
      print("incorrect, drawing arm")
      t.goto(-100, 30)
      t.pendown()
      t.right(90)
      t.forward(50)
      t.penup()
    elif body == 6:
      body=7
      print("incorrect, drawing second arm")
      t.goto(-80, 30)
      t.pendown()
      #t.right(90)
      t.forward(30)
      t.pendown()
  else:
    print("that is correct")
  if correct == howlong:
    print("You Win!")
    playgame = 0
  if body == 7:
    print("Game Over! the word was", theword)
    playgame = 0
t.hideturtle()   