#!/user/bin/env python

import random

def main():
    print("Try To Guess The Music Genre!")
    print("Test your luck!!")
    
    genre = [
        "rock",
        "hiphop",
        "kpop",
        "indie",
        "rnb",
        ]
    x = random.choice(genre)
    guess = None
    hint  = None
    rock  = None
    hiphop= None
    kpop  = None
    indie = None
    rnb   = None
    while x != guess: 
        guess= str(input("what genre do you think it is?"))
        if x == guess:
            print("you're lucky!congratulations,NAILED IT!".format(guess))
            break
        else:
            print("you got it wrong but..NEVER BACK DOWN NEVER WHAT?!?!".format(guess))
            print("YOUR HINTS=")
            
        if hint == rock:
                print(" .it's a hardcore music")
                
        if hint == hiphop:
                print(" .what is known as disco rap??")
                
        if hint == kpop:
                print(" .what is the trendy genre in our generation?")
                
        if hint == indie:
                print(" .what is similiar to lo-fi sounds?")
            
        if hint == rnb:
                print(" .what genre is originated in African American communities??")
                
main()