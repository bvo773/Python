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
#Step 1 

wordList = ["aardvark", "baboon", "camel"]
stagesList = hangman_art.stages

#TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)

#TODO - Put blank in a blanklist and use that list to reassign the corrected guess letter
blanklist = list()
for i in range(0, wordLength):
  blanklist.append('_')
  print(blanklist[i], end=" ")

  

#TODO - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print()
guess = str(input("Guess a letter:" )).lower()

#TODO - Print the blanklist
def printBlankList(blankList):
  for letter in blankList:
    print(letter, end=" ")

#TODO - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Replace the blanklist with the corrected guess letter
i = 0
life = 6
guessCheck = 0
for letter in chosenWord:
  if guess == letter:
    #print(f"Right:{i}")
    blanklist[i] = letter
    printBlankList(blanklist) 
    
  else:
    print("Wrong")
    guessCheck += 1
  


#TODO - Show current state of blanklist and player's chances remaning
printBlankList(blanklist)
print(stagesList[life])
  
    

  


def main():
  print("Hello world")
                                                                                                                                                                                                                                                                                                                   
if __name__ == "__main__":
  main()