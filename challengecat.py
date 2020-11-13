#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    
    # Challenge#1:pull different values/keys out, make fun of person making the fact
    num = 0
    names = []
    newname = ""
    for catfact in r.json()["all"]:
        try:
            newname = catfact.get("user").get("name").get("first")+" " + catfact.get("user").get("name").get("last")
        except:
            pass
        if newname not in names:
            names.append(newname)
        num += 1
        
    x = 0
    while x < len(names) - 1:
        print(names[x], end = ", ")
        x += 1
    print("and, of course,", names[x], end = "")
    print("; all yall are dum dum")
    print("Man, I went through ", num, " entries for this, ugh.", sep = "")

    # Challenge#2:keeps track of higest upvote and associated comment
    max_up = 0
    max_comment = ""
    for catfact in r.json()["all"]:
        if int(catfact.get("upvotes")) > max_up: # the .get() method returns NONE if key not found
            max_up = int(catfact.get("upvotes"))
            max_comment = catfact.get("text")
    print("The most upvoted (",max_up,") comment is: ", max_comment.strip(), sep = "")       

    # Challenge#3:random fact
    facts = []
    fact = ""
    for catfact in r.json()["all"]:
        fact = catfact.get("text")
        if fact not in facts:
            facts.append(fact)
    print("This moment's random cat fact is:", random.choice(facts))

main()

