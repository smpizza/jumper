# Lab 6 Rock Paper Scissors

import random


# welcome message
print("Hello, lets play rock, paper, scissors! \n") # \n means new line
print("To play, press r for rock, press s for scissors, and press p for paper \n")

while True:

    # start of game
    user = input("Your move:  ")
    options = ["r", "p", "s"] # change to numbers? easier to use with operators
    computer = random.choice(options)


    # user ties
    if user == computer:
        print(f"computer picks {computer} and you chose {user}. It's is a tie! \n") # displays results
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass


    # user loses    
    elif user == "r" and computer == "p": # user rock vs co paper
        print(f"computer picks {computer} and you chose {user}. You lose!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass

    elif user == "p" and computer == "s": # user paper vs co scisssors
        print(f"computer picks {computer} and you chose {user}. You lose!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass

    elif user == "s" and computer == "r": # user scissors vs co rock
        print(f"computer picks {computer} and you chose {user}. You lose!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass           

    # User wins       
    elif user == "r" and computer == "s": # user rock vs co scissors
        print(f"computer picks {computer} and you chose {user}. You win!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass

    elif user == "p" and computer == "r": # user paper vs co rock
        print(f"computer picks {computer} and you chose {user}. You win!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass

    elif user == "s" and computer == "p": # user scissors vs co paper
        print(f"computer picks {computer} and you chose {user}. You win!\n")
        exit = input("Continue Playing? yes or no ")
        if exit == "no":
            break
        else:
            pass            





# nothing to see here, but I'm glad you took the time to read this.