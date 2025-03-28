import os
import random
import sys
import time
import datetime
today = datetime.date.today()

# Colorama, colored text. Might not work with hosts. 
#from colorama import Fore

# List for the script to recognize an invalid syntax
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# i also recommend the print_slow function

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
start = input("Start?: y/n: ")
phrase = 90
ff = "Main Directory"
ss = "select a script to run"
global dd1
global dd2
global dd3
if start == "y":
    print("\n" * 100)
    while True:
        print("Welcome to the (xyz) Python Directory!")
        print("Timestamp:", today.strftime("%m/%d/%Y"), "at", time.strftime("%I:%M %p"))
        time.sleep(1)
        print("1: See Available Scripts")
        time.sleep(1)
        print("2: About this Repository")
        time.sleep(1)
        print("3: Usage (See for Copyright, rights to use, and rules for credit)")
        time.sleep(1)
        print("4: Contact admin")
        time.sleep(1)
        print("5: Exit")
        time.sleep(3)
        t = input("Function: ")
        if t == "1":
            print("\n" * 100)
            while True:
                print(str(ff))
                print(str(ss))
                print("1: script N: Next page")
                dd1 = (input("Function: "))
                if dd1 == "1":
                    print("script 1")
                    print("Loading.")
                    time.sleep(5)
                    pp = input("Begin? y/n: ")
                    if pp == "y":
                       print("your script here")
                            aa = (input("Do it again? (y/n): "))
                if dd1 == "n":
                    print("\n" * 100)
                    #while True:
                    print("Q to return to the first page.")
                    print("page 2 N: Next page")
                    dd2 = input("Function: ")
                    if dd2 == "5":
                            print("\n" * 100)
                            print("Sorting")
                            pp = input("Begin? y/n: ")
                            if pp == "y":
                               print("your code here")
                            aa = (input("Do it again? (y/n): "))
                            if aa == "n":
                                break
                    if dd2 in alphabet:
                        print("Invalid!")
                    if dd2 == "n":
                        print("\n" * 100)
                            #while True:
                        print("Q to return to the first page")
                        print("10: page 3")
                        dd3 = input("Function: ")
                                            aa = (input("Do it again? (y/n): "))
                                            if aa == "n":
                                                break
                        if dd3 == "10":
                            print("your script here")
                            
            if (dd1, dd2, dd3) == "q":
                break

        if t == "2":
            print("\n" * 100)
            while True:
                print("About this Repo")
                print("here"
                cmd = input("press q to go back: ")
                if cmd == "q":
                    break
        if t == "3":
            print("\n" * 100)
            while True:
                print("Usage")
                print("xyz")
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
    if start == "n":
        sys.exit()
