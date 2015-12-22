# Implementation of the game "Guess the number"

import simplegui
import random
import math

global temp # variable temp is the upper bound of the range
temp = 100

# helper function to start and restart the game
def new_game():
    print "New game. Range is [0,", temp, ")"
    # initialize global variables
    global secret_number, count
    secret_number = random.randrange(0, temp)
    count = int(math.ceil(math.log(temp+1)/math.log(2)))
    print "Number of remaining guesses is", count
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global temp
    temp = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global temp
    temp = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	 
    guess = int(guess)
    print "Guess was", guess
    
    global count
    count -= 1
    print "Number of remaining guesses is", count
    
    if count == 0: 
        if guess != secret_number:
            print "You ran out of guesses.  The number was", secret_number
        else:
            print "Correct!"
            
        print ""
        new_game()
    else:  
        if guess < secret_number:
            print "Higher!"
            print ""
        elif guess > secret_number:
            print "Lower!"
            print ""
        else:
            print "Correct!"
            print ""
            new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_input("Guess the number", input_guess, 100)

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)

# call new_game 
new_game()

