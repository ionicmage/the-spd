x = float(input("what is your shape? 1: Rectangle 2: Triangle 3: Square: "))
if x == 1:
  y = int(input("what is your first side? "))
  z = int(input("what is your second side? "))
  a = y * z
  print (a)
if x == 2:
  b = int(input("what is your height? "))
  h = int(input("what is your base? "))
  e = (b*h)/2
  print (e)
if x == 3:
  n = int(input("what is the length? "))
  m = int(input("what is the width? "))
  o = m*n
  print (o)