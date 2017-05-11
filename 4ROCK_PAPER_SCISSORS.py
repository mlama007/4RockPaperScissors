"""This is a simple game of rock, paper, scissors"""
from random import randint
from time import sleep

options = ["R", "P", "S"]

LOSE = "You lost!"
WIN = "You won!"

def decide_winner(user_choice, computer_choice):
    print "Your choice: %s" % user_choice
    print "Computer selecting..."
    sleep(1)
    print "Computer choice: %s" % computer_choice
    user_choice_index = options.index(user_choice)
    computer_choice_index = options.index(computer_choice)
    if user_choice_index == computer_choice_index:
       	print "This is a tie!"
    elif user_choice_index == 0 and computer_choice_index == 2:
        print WIN
    elif user_choice_index == 1 and computer_choice_index == 0:
    	  print WIN
    elif user_choice_index == 2 and computer_choice_index == 1:
      	print WIN
    elif user_choice_index > 2:
        print "Invalid Choice!"
        return
    else:
      	print "You lose!"
  
def play_RPS():
    print "Let's play rock, paper, scissors!"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ").upper()
    sleep(1)
    computer_choice = options[randint(0,len(options)-1)]
    decide_winner(user_choice, computer_choice)
  
play_RPS()