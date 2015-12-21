#Implementation of the game "Rock-paper-scissors-lizard-Spock"


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    convert name to a number
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Please input one of correct names!"


def number_to_name(number):
    """
    convert number to a name
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Please input one of correct numbers!"

def rpsls(player_choice): 
    print ""
    # print a blank line to separate consecutive games
    print "Player chooses %s" % player_choice
    # print out the message for the player's choice
    player_number = name_to_number(player_choice)
    # convert the player's choice to player_number
    import random
    comp_number = random.randrange(0,5)
    # compute random guess for comp_number 
    comp_name = number_to_name(comp_number)
    # convert comp_number to comp_choice 
    print "Computer chooses %s" %comp_name
    # print out the message for computer's choice
    if type(player_number) == int:
        diff = (comp_number - player_number) % 5
    # compute difference of comp_number and player_number modulo five
        if diff == 0:
            print "Player and computer tie!"
        elif diff == 1 or diff == 2:
            print "Computer wins!"
        else:
            print "Player wins!"
    # determine the winner and print winner message
    else:
        print "You have input a wrong name, so the result cannot be determined!"
    # print the message to remind the player of the wrong input
    
# test my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


