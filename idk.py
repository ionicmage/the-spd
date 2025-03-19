number1 = float(input("enter a number:"))
number2 = float (input("enter a second number:"))
print ("what do you want to do?")
print ("1: add")
print ("2 subtract")
print ("3 multiply")
print ("4 divide")
choice = float(input("choice:"))
answer = number1 + number2
if choice == 1:
  answer = number1 + number2
  print (answer)
if choice == 2:
  answer = number1 - number2
  print (answer)
if choice == 3:
  answer = number1 * number2
  print (answer)
if choice == 4:
  answer = number1 / number2
  print (answer)