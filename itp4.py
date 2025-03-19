import time
print("Enter 3 numbers, and i will order them least to greatest")
time.sleep(3)
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

n1 = min(a, b, c)
n3 = max(a, b, c)
n2 = (a + b + c) - n1 - n3
print("Numbers sorted: ", n1, n2, n3)
