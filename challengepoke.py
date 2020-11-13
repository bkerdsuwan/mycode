#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/mew").json()

    print("*In pokedex voice* This is mew. For a different view:")
    print(pokeapi.get("sprites").get("front_default"))
    print("It's been in",len(pokeapi.get("game_indices")), "games.")
   # for x in pokeapi.get("moves"):
    max_moves = len(pokeapi.get("moves"))
    x = 0
    """
    while x < max_moves:
        print(pokeapi.get("moves")[x].get("move").get("name"), end = ",")
        x += 1
    """
    for move in pokeapi["moves"]:
        print(move["move"]["name"], end = ",")
main()
