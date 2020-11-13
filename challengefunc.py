#!/usr/bin/env python3

print("What math you need?")

while True:
    print("Give me that first number: ")
    num1 = input()
    try:
        int(num1)
        break
    except:
        print("That's not an integer!")

while True:
    print("Give me that second number: ")
    num2 = input()
    try:
        int(num2)
        break
    except:
        print("That's not an integer!")
    
valid = ["+", "-", "*", "/", "a", "s", "m", "d"]
op = ""

while op.lower() not in valid:
    print("What you want to do with them? ")
    op = input()
    if op.lower() not in valid:
        print("Can't do, dude, try one of these?")
        for count in valid:
            print(count, end = " ")
        print()

def calc(num1, num2, op):

    valid = ["+", "-", "*", "/", "a", "s", "m", "d"]
    if isinstance(num1, int) and isinstance(num2, int) and op in valid:

        if op == "+" or op == "a":
            print(str(num1+num2))
            return(num1+num2)
        if op == "-" or op == "s":
            print(str(num1-num2))
            return(num1-num2)
        if op == "*" or op == "m":
            print(str(num1*num2))
            return(num1*num2)
        if op == "/" or op == "d":
            print(str(num1/num2))
            return(num1/num2)

    else:
        print("Invalid input, function needs integers and a valid operator input")

input("uhhh crap, I don't have enough fingers for that")
print("ugh fine, the answer is", end = " ")
calc(int(num1), int(num2), op)
#calc(num1, num2, op)
"""        
calc(1,2,"+")
calc(5,3,"s")
calc(2,4,"*")
calc(9,3,"d")
"""
