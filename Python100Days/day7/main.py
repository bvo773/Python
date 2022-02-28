'''
HANGMAN PROJECT
- FOR & WHILE LOOPS
- IF/ELSE
- LISTS
- STRINGS
- RANGE
- RANDOM MODULES
'''

import random
import hangman_art
import hangman_words

wordList = hangman_words.word_list
stagesList = hangman_art.stages
print(hangman_art.logo)

#TODO - Generate, Randomly choose a word from the wordList and assign it to chosenWord
chosenWord = random.choice(wordList)
print("shhhhhh.. don't look at the solution...: " + chosenWord)

#TODO - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO- Create an empty List called displayList.
#For each letter in the chosenWord, add a "_" to 'display'.
#So if the chosenWord was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
displayList = []
for i in range(0, len(chosenWord)):
  displayList.append('_')

#TODO- Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_". 
# Join all the elements in the list with a 'blankspace' and turn it into a String.
print(f"{' '.join(displayList)}")

#TODO - Use a while loop to let the user guess again. The loop should only stop once the user
#has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
endOfGame = False
while not endOfGame:
  #TODO- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter: " ).lower()

  #TODO: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in displayList:
    print(f"You have already guessed '{guess}'" )

  #TODO- Loop through each position in the chosenWord;
  #If the letter at that position matches 'guess' then reveal that letter in the displayList at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then displayList should be ["_", "p", "p", "_", "_"].
  for i in range(len(chosenWord)):
    if guess == chosenWord[i]:
      displayList[i] = chosenWord[i]
  
  if guess not in chosenWord:
    print(f"You guessed '{guess}', that's not in the word. You lose a life.")
    lives -= 1
  
  #TODO - Show current state of blanklist and player's lives remaning
  print(f"{' '.join(displayList)}")
  print(stagesList[lives])

  if "_" not in displayList:
    print("You win!")
    endOfGame = True
  elif lives == 0:
    print("You Lose! Game over!")
    endOfGame = True
  
    
