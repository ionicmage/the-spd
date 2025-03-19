print ("welcome to the square calculator!")
a = int(input("enter a positive integer and ill tell you what it is squared and cubed!:"))
b = a * 3
print (b)
c = a * 9
print (c)
d = float(input("run again? (1 for yes, 2 for no):"))
if d == 2:
  print ("moving on")
while d == 1:
  range(1)
  x = int(input("what number do you wanna square/cube?:"))
  y = x * x
  z = x * x * x
  print (y,z)
  d=int(input("do you wannna do it again? (1:yes 2:no):"))
e = int(input("enter another positive integer and ill give you its factorial:"))
f = e * 2
print (f)
g = int(input("run again?: (1 for yes, 2 for no):"))
while g == 1:
  m = int(input("enter another number to factorial:"))
  n = m * 2
  g = int(input("again? (1:yes 2:no):"))
if g == 2:
  print ("thanks for using my calculator")