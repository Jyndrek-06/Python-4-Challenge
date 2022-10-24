from game import game
# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.
name = input("What is your name?")
print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess. What number do you think it is?")
      
import random
secret = random.randint(1, 101)
count = 0

game()

      