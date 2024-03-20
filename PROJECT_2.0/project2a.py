"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Slavík

email: slavik.work@seznam.cz

discord: slavisut

"""

import random
import time
import math

history = {}
play_count = 0
next = True
game_start_time = time.time()

print("Hi there! \n"+"-"*40+"\nI've generated a random 4 digit number for you"
"\nLet's play a bulls and cows game.")

# This loop defines how long the game itself is played
while next == True:
    play_count += 1
    guess_count = 0
    start_time = time.time()
    randlist = []
    rand4 = ''
    unique_char = True
    correct_guess = False

# Loop generating a unique 4-digit number, not starting with '0'
    while len(randlist)<4:
      rand1 = random.randint(0,9)
      if randlist.count(str(rand1)) == 0:
        randlist.append(str(rand1))
        if randlist[0] == '0':
          randlist.pop(0)
    rand4 = ''.join(randlist)
    #print(rand4)
# A loop which runs until the full guess is correct
    while correct_guess == False:
      bulls = 0
      cows = 0
      print('-'*40)
      guess = input('Enter a 4 digit number: ')
      print('-'*40)
# Loop checking if all numbers in guess are unique, if not, you will be asked for new guess
      for digit in guess:
        if guess.count(digit) > 1:
          unique_char = False
          break
        else:
          unique_char = True
# Check if length, character type and non zero first digit conditions are met
      if len(guess) == 4 and guess.isnumeric() and unique_char and guess[0] != '0' :
        guess_count +=1
      else:
        print(guess,'= Invalid input: Must be 4 unique digits, not starting with zero')
        continue
      if rand4 == guess:
        correct_guess = True
      else:
# Loop for evaluating nb of Bulls & Cows
        for x in range(1,5):
          guess_x = guess[int(x)-1]
          rand4_x =rand4[int(x)-1]
          if guess_x == rand4_x:
            bulls += 1
          elif guess_x in rand4:
            cows += 1
        print(f"{bulls} bulls, {cows} cows")
    print("Correct, you've guessed the right number!\n")
# Spent time measurement for one run, the formula is also used for total time
    end_time = time.time()
    elapsed_time = (end_time-start_time)
    def time_format(duration : float) -> str :
      hours = math.floor(duration / 3600)
      minutes = math.floor((duration % 3600) / 60)
      seconds = round(duration % 60 ,2)
      play_time = f" {hours:02d}:{minutes:02d}:{seconds:05.2f}"
      return play_time, hours, minutes, seconds
    play_time, hours, minutes, seconds = time_format(elapsed_time)
    print(f"You have played this session for: \n{hours} hours, {minutes} minutes and {seconds} seconds")
    print(f"Number of guesses used: {guess_count}")
    print('-'*40 + '\n')

# Update time played and nb of guesses into history dictionary, giver at the close of the game
    history.update({"Run_"+str(play_count):[play_time,guess_count]})

# Do you want to play another run?
    if input("Play again? (y/n): ").lower() == 'y':
      print("\n")
      next = True
    else:
      next = False

# Total statistics + final print
game_end_time = time.time()
total_time = game_end_time - game_start_time
play_time, hours, minutes, seconds = time_format(total_time)

print('-' * 40 + '\n\nYour playing history is: \nRunX : [Time, Guesses]')
print(history)
print(f"\nTotal time spent playing: \n{hours} hours, {minutes} minutes and {seconds} seconds \n Thank you for playing!")
