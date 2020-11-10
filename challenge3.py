#!/usr/bin/env python3

heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
char_name = input("Which character do you want to know about? (Flash, Batman, Superman) ")
char_stat = input("Which statistic do you want to know about? (strength, speed, or intelligence) ")
cap = char_name
print(f"{cap.capitalize()}'s {char_stat} is: {heroes[char_name][char_stat]}")
print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name][char_stat]}")
