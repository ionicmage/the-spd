change = int(input("What is your change?:"))
q = 0
d = 0
n = 0
p = 0
while change >= 25:
  change = change - 25
  q = q + 1
while change >= 10:
  change = change - 10
  d = d + 1
while change >= 5:
  change = change - 5
  n = n + 1
while change >= 1:
  change = change - 1
  p = p + 1


print("you have" + str(q) + "quarters")
print ("you have" + str(d) + "dimes")
print("you have" + str(n) + "nickels")
print ("you have" + str(p) + "pennies")
