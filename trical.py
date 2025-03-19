print ("Ians Python Calculator (est 2021 All Rights Reserved")
r = int(input("1 for Triangle/ 2 for Rectangle:"))
if r == 1: 
  t1 = int(input("whats the first side:"))
  t2 = int(input("whats the second side:"))
  t3 = int(input("whats the third side:"))
  l = t1 + t2 + t3
if r == 2:
  r1 = int(input("whats the first line:"))
  r2 = int(input("whats the second line:"))
  l = (r1 + r2) * 2
print ("your answer is:")
print (l)
print ("also quick message: dont use a calculator in class or on your homework :) even if its python ")