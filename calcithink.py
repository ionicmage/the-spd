x = int(input("enter your first number:"))
y = int(input("enter your second number"))
z = (x + y)*2
print (z)
a = float(input("do it again?(1=yes 2=no): "))
while a == 1:
  x = int(input("enter your first number: "))
  y = int(input("enter your second number: "))
  z = (x + y)*2
  a = int(input("run again?: (1 for yes, 2 for no): "))
  if a == 1:
    x = int(input("enter your first number: "))
    y = int(input("enter your second number: "))
    z = (x + y)*2
if a == 2:
  print("ended, thanks!")