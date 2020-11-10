#!/usr/bin/env python3

petrock = 0
dwayne = 0
music = 0

print("Let's figure out what kind of rock you are! Please answer using the numbers!")
print("Question: where is your favorite vacation destination?")
print("1. Hotel California")
print("2. Beautiful Samoa")
print("3. ...")

answer = 5
while True:
    try:
        answer = int(input())
        if answer <4:
            break
        else:
            print("Hey, that's not one of the options! Try again")
    except:
        print("Put in a number. What? Do you live under a rock?")

if answer == 1:
    music += 1
elif answer == 2:
    dwayne += 1
elif answer == 3:
    petrock += 1

print("Question: how do you like to travel?")
print("1. The midnight train going anywhere")
print("2. Cars. Fast and furious.")
print("3. ...")

answer = 5
while True:
    try:
        answer = int(input())
        if answer <4:
            break
        else:
            print("Hey, that's not one of the options! Try again")
    except:
        print("Put in a number. What? Do you live under a rock?")

if answer == 1:
    music += 1
elif answer == 2:
    dwayne += 1
elif answer == 3:
    petrock += 1

if music > dwayne + petrock:
    print("You're a rock star!")
elif dwayne > petrock + music:
    print("You're The Rock!")
elif petrock > dwayne + music:
    print("You're an actual rock!")
else:
    print("You're more than one kind of rock!")
