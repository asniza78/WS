#!/usr/bin/env python

import random

def main():
    """Start a colour guessing game."""
    print()
    print("We have 4 choices of colours (blue, green, red, brown)")
    
    # Senarai warna
    colour = [
        "blue",
        "green",
        "red",
        "brown"
        ]

    # Pilih satu warna secara rawak
    x =random.choice(colour)

    
    #print(x)
    
    guess = (input("Guess my favourite colour? "))

    # Semak tekaan pengguna    
    if x == guess:
            print("You guessed.Congratulations you got it right!")
            print()
        
    else:
            print()
            print("That is not my favourite colour.")
            print("Please Try again")
            print()
main()