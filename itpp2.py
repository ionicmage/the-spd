import time
import random
right = 0
m = random.randrange(1,10)
print("Hi, welcome to the guessing game")
time.sleep(1)
x = float(input(print("do you want to guess my number,(1) or should i guess yours?(2):")))
if x == 1:
  print("great, ill think of a number.")
  time.sleep(1)
  print("Alright, ive got a number")
  while right == 0:
    z = float(input(print("guess the number")))
    if z == m:
      print("You guessed it!")
      right = 1
    elif z > m:
      print("your guess is too high")
    elif z < m:
      print("your guess is too low")
if x == 2:
  print("Alright, think of a number")
  time.sleep(3)
  print("got it?")
  time.sleep(1)
  print("alright, ill guess now")
  time.sleep(1)
  print (m)
  f = float(input(print(" was i right? 1/2")))
  while right == 0:
    if f == 1:
      print("Good game!")
      right = 1
    if f == 2:
      print("darn, ill try again next time")
      right = 1
      