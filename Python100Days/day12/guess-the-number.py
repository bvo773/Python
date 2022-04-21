#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def check_attempts(attempts, guess)-> int:
  if guess == 0:
    return attempts - 1
  return attempts

# return 0 if user guess incorrectly else return the correct num
def check_guess(guess_num, random_num)-> int:
  if guess_num > random_num:
    print("Too high.\nGuess again.")
    return 0
  elif guess_num < random_num:
    print("Too low.\nGuess again.")
    return 0
  else:
    return guess_num

def set_difficulty(difficulty):
  if difficulty == "easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def print_result(attempts, guess_check):
  if attempts != 0 and guess_check == 0:
    print(f"You have {attempts} remaining to guess the number.")
  elif attempts == 0 and guess_check == 0:
    print(f"You've run out of guesses, you lose!")
  elif guess_check != 0 and (attempts <= 10 and attempts >= 1):
    print(f"You got it! The answer was {guess_check}.")
def game():

  random_num = random.randint(0, 100)
  print("I'm thinking of a number between 1 and 100.")
  print(f"Psst, the correct answer is {random_num}")

  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  attempts = set_difficulty(difficulty)
  # Initially guess_check is set to 0 meaning they haven't guess the number correctly yet since it's the start of the game
  guess_check = 0  
  print_result(attempts, guess_check)
  while attempts != 0 and guess_check == 0:
    guess_num = int(input("Make a guess: "))
    guess_check = check_guess(guess_num, random_num) # return 0 - wrong number or the correct number if guess correctly
    attempts = check_attempts(attempts, guess_check) # if guess_check = 0, deduct one life
    print_result(attempts=attempts, guess_check=guess_check)
    
    
print(logo)
game()