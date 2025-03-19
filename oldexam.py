import turtle

t = turtle.Turtle()
loop = 1
otherloop = 1

x = int(input("start? 1/2"))
if x == 1:
	while otherloop == 1:
		print("Welcome to the IanOS")
		print("you have a few options")
		print("please choose 1")
		print("Option 1: Draw circles")
		print("Option 2: Add em together")
		print("Option 3: End program")
		l = int(input("please enter the number of the program you wish to run:"))
		if l == 1:
			t.pendown
			t.fillcolor("orange")
			t.begin_fill()
			t.circle(60)
			t.end_fill()
			t.penup
			t.forward(200)
			t.fillcolor("blue")
			t.begin_fill()
			t.circle(60)
			t.end_fill()
			t.penup()
		if l == 2:
			while loop == 1:
				z = int(input("Enter a number:"))
				h = int(input("enter a second number:"))
				m = z + h
				if m == 60:
					print("Passed!")
					loop = 2
				elif m >= 60:
					print("try again")
		if l == 3:
			quit
			otherloop = 2
			loop = 2
		