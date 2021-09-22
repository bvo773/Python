'''
ROCK > SCISSOR
SCISSOR > PAPER
PAPER > ROCK
'''
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

stringChoices = ["rock","paper","scissors"]
asciiChoices = [rock, paper, scissors]

print(rock,paper,scissors)
userChoice = str(input("ROCK, PAPER, OR SCISSORS:\n ")).lower()
cpuChoice = str(stringChoices[random.randint(0, len(stringChoices)-1)])

asciiCpu = ""
asciiUser = ""

rockCheck = stringChoices[0]
paperCheck = stringChoices[1]
scissorsCheck = stringChoices[2]

if cpuChoice == rockCheck: 
	asciiCpu = asciiChoices[0]
elif cpuChoice == paperCheck: 
	asciiCpu = asciiChoices[1]
else: 
	asciiCpu = asciiChoices[2]

if userChoice == rockCheck: 
	asciiUser = asciiChoices[0]
elif userChoice == paperCheck: 
	asciiUser = asciiChoices[1]
else: 
	asciiUser = asciiChoices[2]

if userChoice == cpuChoice:
	print(f"\nDRAW!\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}")
else:
	if (userChoice == rockCheck) and (cpuChoice == scissorsCheck):
		print(f"\nYOU WIN!\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}")
	elif (userChoice == scissorsCheck) and (cpuChoice == paperCheck):
		print(f"\nYOU WIN!\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}")
	elif (userChoice == paperCheck) and (cpuChoice == rockCheck):
		print(f"\nYOU WIN!\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}")
	else:
		print(f"\nSORRY, BETTER LUCK NEXT TIME!\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}")

		


