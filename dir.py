import os
import random
import sys
import time
import datetime
today = datetime.date.today()
#import _pydatetime
#from _pyrepl.readline import raw_input
#from time import sleep
from colorama import Fore
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
start = input(Fore.RED + "Start?: y/n: ")
phrase = 90
ff = "Main Directory"
ss = "select a script to run"
global dd1
global dd2
global dd3
if start == "y":
    print("\n" * 100)
    while True:
        print(Fore.RED + "Welcome to the Shitty Python Directory! (SPD)")
        print("Timestamp:", today.strftime("%m/%d/%Y"), "at", time.strftime("%I:%M %p"))
        time.sleep(1)
        print(Fore.GREEN + "1: See Available Scripts")
        time.sleep(1)
        print(Fore.BLUE + "2: About this Repository")
        time.sleep(1)
        print(Fore.YELLOW + "3: Usage (See for Copyright, rights to use, and rules for credit)")
        time.sleep(1)
        print(Fore.LIGHTBLUE_EX + "4: Contact admin")
        time.sleep(1)
        print(Fore.WHITE + "5: Exit")
        time.sleep(3)
        t = input(Fore.MAGENTA + "Function: ")
        if t == "1":
            print("\n" * 100)
            while True:
                print(str(ff))
                print(str(ss))
                print(Fore.WHITE + "1: Calculator 2: Area Finder 3: Change calculator 4: Square calculator N: Next page")
                dd1 = (input(Fore.MAGENTA + "Function: "))
                if dd1 == "1":
                    print("Calculator")
                    print("Loading.")
                    time.sleep(5)
                    pp = input("Begin? y/n: ")
                    if pp == "y":
                        qq = int(input("1: Addition 2: Subtraction 3: Multiplication 4: Division: "))
                        if qq == 1:
                            #while True:
                            s = 0
                            print("How many numbers you want to sum?")
                            numb = int(input())
                            for i in range(numb):
                                a = int(input(str(i + 1) + ". number "))
                                s += a
                            print("Result : " + str(s))
                            aa = (input("do it again?( y/n ): "))
                        if qq == 2:
                            result = 0
                            print("How many numbers do you want to subtract?")
                            numb = int(input())
                            for i in range(numb):
                                a = int(input(str(i + 1) + ". number "))
                                if i == 0:
                                    result = a  # Initialize result with the first number
                                else:
                                    result -= a
                            print("Result : " + str(result))
                            aa = (input("Do it again? (y/n): "))
                        if qq == 3:
                            product = 1
                            print("How many numbers do you want to multiply?")
                            numb = int(input())
                            for i in range(numb):
                                a = int(input(str(i + 1) + ". number "))
                                product *= a
                            print("Result : " + str(product))
                            aa = (input("Do it again? (y/n): "))
                        if qq == 4:
                            result = None
                            print("How many numbers do you want to divide?")
                            numb = int(input())
                            for i in range(numb):
                                a = int(input(str(i + 1) + ". number "))
                                if i == 0:
                                    result = a  # Initialize result with the first number
                                else:
                                    result /= a
                            print("Result : " + str(result))
                            aa = (input("Do it again? (y/n): "))
                if dd1 == "2":
                    print("Area Finder")
                    pp = input("Begin? y/n: ")
                    if pp == "y":
                        x = float(input("what is your shape? 1: Rectangle 2: Triangle 3: Square: "))
                        if x == 1:
                            y = int(input("what is your first side? "))
                            z = int(input("what is your second side? "))
                            a = y * z
                            print(a)
                        if x == 2:
                            b = int(input("what is your height? "))
                            h = int(input("what is your base? "))
                            e = (b * h) / 2
                            print(e)
                        if x == 3:
                            n = int(input("what is the length? "))
                            m = int(input("what is the width? "))
                            o = m * n
                            print(o)
                    aa = (input("Do it again? (y/n): "))
                if dd1 == "3":
                    print("Change calculator")
                    pp = input("Begin? y/n: ")
                    if pp == "y":
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
                        print("you have" + str(d) + "dimes")
                        print("you have" + str(n) + "nickels")
                        print("you have" + str(p) + "pennies")
                    aa = (input("Do it again? (y/n): "))
                if dd1 == "4":
                    print("Factorial calculator")
                    pp = input("Begin? y/n: ")
                    if pp == "y":
                        print("welcome to the square calculator!")
                        a = int(input("enter a positive integer and ill tell you what it is squared and cubed!:"))
                        b = a * 3
                        print(b)
                        c = a * 9
                        print(c)
                        aa = (input("Do it again? (y/n): "))
                if dd1 == "n":
                    print("\n" * 100)
                    #while True:
                    print("Q to return to the first page.")
                    print("5: Sorting 6: Guessing 7: Palindrome Finder 8: Hourly Pay Calculator N: Next page")
                    dd2 = input("Function: ")
                    if dd2 == "5":
                            print("\n" * 100)
                            print("Sorting")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                                    print("\n" * 100)
                                    print("Enter 3 numbers, and i will order them least to greatest")
                                    time.sleep(3)
                                    a = int(input("enter first number: "))
                                    b = int(input("enter second number: "))
                                    c = int(input("enter third number: "))

                                    n1 = min(a, b, c)
                                    n3 = max(a, b, c)
                                    n2 = (a + b + c) - n1 - n3
                                    print("Numbers sorted: ", n1, n2, n3)
                                    aa = (input("Do it again? (y/n): "))
                    if dd2 == "6":
                            print("\n" * 100)
                            print("Guessing Game")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                                    print("\n" * 100)
                                    right = 0
                                    mm = random.randrange(1, 10)
                                    print("Hi, welcome to the guessing game")
                                    time.sleep(1)
                                    xx = input("do you want to guess my number,(1) or should i guess yours?(2): ")
                                    if xx == "1":
                                        print("\n" * 100)
                                        while True:
                                            #os.system("clear")
                                            print("great, ill think of a number 1-10.")
                                            time.sleep(1)
                                            print("Alright, ive got a number")
                                            while right == 0:
                                                print("\n" * 100)
                                                z = int(input("guess the number: "))
                                                if z == mm:
                                                    print("\n" * 100)
                                                    print("You guessed it!")
                                                    right = 1
                                                elif z > mm:
                                                        print("\n" * 100)
                                                        print("your guess is too high")

                                                elif z < mm:
                                                    print("\n" * 100)
                                                    print("your guess is too low")
                                                    print(z)
                                            if right == 1:
                                                print("\n" * 100)
                                                break
                                        #xxx = input("try again? y/n: ")
                                        #if xxx == "n":
                                            #break
                                    if xx == "2":
                                        print("\n" * 100)
                                        while True:
                                            print("Alright, think of a number")
                                            time.sleep(3)
                                            xxxx = input("got it? y/n: ")
                                            time.sleep(1)
                                            if xxxx == "y":
                                                print("\n" * 100)
                                                print("alright, ill guess now")
                                                time.sleep(1)
                                                print(m)
                                                f = float(input(print(" was i right? 1/2")))
                                                while right == 0:
                                                    print("\n" * 100)
                                                    if f == 1:
                                                        print("Good game!")
                                                        right = 1
                                                    if f == 2:
                                                        print("darn, ill try again next time")
                                                        right = 1
                                        if right == 1:
                                            print("\n" * 100)
                                            break
                                    aa = (input("Do it again? (y/n): "))
                                    if aa == "y":
                                        print("\n" * 100)
                                        break
                    if dd2 == "7":
                            print("\n" * 100)
                            print("Palindrome Finder")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                                print("\n" * 100)
                                theword = str(input("whats your word:"))
                                print(theword)
                                ip = 1
                                j = len(theword)
                                letter = theword[0]
                                ll = theword[j - 1]
                                print(letter, ll)
                                for r in range(j):
                                    print(theword[r], theword[j - 1])
                                    if theword[r] != theword[j - 1]:
                                        print("No palindrome")
                                    j = j - 1
                                    if ip == 1:
                                        print("Palindrome")
                            aa = (input("Do it again? (y/n): "))
                            if aa == "y":
                                print("\n" * 100)
                                break
                    if dd2 == "8":
                            print("\n" * 100)
                            print("Hourly Pay Calculator")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                                print("\n" * 100)
                                h = float(input("What are your hours?:"))
                                p = float(input("what is your hourly pay?:"))
                                o = h - 40
                                a = h * p
                                if h > 40:
                                    a = h * p
                                    print(a)
                                w = a * p
                                print(w)
                                r = 40 * p
                                print(r)
                            aa = (input("Do it again? (y/n): "))
                            if aa == "n":
                                break
                    if dd2 in alphabet:
                        print("Invalid!")
                    if dd2 == "n":
                        print("\n" * 100)
                            #while True:
                        print("Q to return to the first page")
                        print("9: Jacket and Hat sizer 10: Vowel Finder")
                        dd3 = input("Function: ")
                        if dd3 == "9":
                                    #if dd == "9":
                                        print("\n" * 100)
                                        print("Jacket and Hat sizer")
                                        pp = input("Begin? y/n: ")
                                        if pp == "y":
                                            print("\n" * 100)
                                            h = float(input("what is your height?: "))
                                            w = float(input("what is your weight?: "))
                                            a = float(input("what is your age?: "))
                                            hat = (w/h) * 2.9
                                            print(hat)
                                            jj = h*w/288
                                            if a <= 40:
                                                jj + (1/8)
                                            print(jj)
                                            aa = (input("Do it again? (y/n): "))
                                            if aa == "n":
                                                break
                        if dd3 == "10":
                            print("\n" * 100)
                            print("Vowel Finder")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                                print("\n" * 100)
                                x = str(input("enter a word and ill tell you how many vowels there are:"))
                                s = len(x)
                                time.sleep(3)
                                print("Hmm, the length is", s)
                                v = x.count("a")
                                r = x.count("e")
                                t = x.count("i")
                                f = x.count("o")
                                y = x.count("u")
                                print("amount of A's:", v)
                                time.sleep(3)
                                print("amount of E's:", r)
                                time.sleep(3)
                                print("there are", t, "I's")
                                time.sleep(3)
                                print(f, "O's...")
                                time.sleep(3)
                                print("and", y, "U's")
                                time.sleep(5)
                                print("your word was", x)
                                time.sleep(5)
                                print("the length was:", s)
                                time.sleep(5)
                                print("List of vowels:")
                                print("A:", v, "E:", r, "I:", t, "O:", f, "U:", y)
                                aa = input("Do it again? (y/n): ")
                                if aa == "n":
                                    break

            if (dd1, dd2, dd3) == "q":
                break






            #if aa == "n":
                #break
        if t == "2":
            print("\n" * 100)
            while True:
                print("About this Repo")
                print("this is a repo of python scripts i made in my freshman year programming class")
                print("that's really about it. have fun.")
                cmd = input("press q to go back: ")
                if cmd == "q":
                    break
        if t == "3":
            print("\n" * 100)
            while True:
                print("Usage")
                print("i dont really care how you use it lol")
                cmd = input("press q to go back: ")
                if cmd == "q":
                    break
        if t == "4":
            print("\n" * 100)

        if t == "5":
            print("\n" * 100)
            print("Bye! Rerun to see options again.")
            sys.exit()
if start == "n":
    print("\n" * 100)
    print("Then why'd you run it? (Easter Egg 1/10)")
    if start == "n":
        sys.exit()