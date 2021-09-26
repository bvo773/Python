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

userNumChoice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS.\n "))
cpuNumChoice = random.randint(0, len(stringChoices)-1)

if (userNumChoice < 0 or userNumChoice > 2):
		print("Invalid choice, you lose!")
else:
		userChoice = stringChoices[userNumChoice]	
		cpuChoice = stringChoices[cpuNumChoice]

		asciiUser = asciiChoices[userNumChoice]
		asciiCpu = asciiChoices[cpuNumChoice]

		rockCheck = stringChoices[0]
		paperCheck = stringChoices[1]
		scissorsCheck = stringChoices[2]

		if userChoice == cpuChoice:
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n DRAW!")
		else:
			if (userChoice == rockCheck) and (cpuChoice == scissorsCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n YOU WIN!")
			elif (userChoice == scissorsCheck) and (cpuChoice == paperCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n YOU WIN!")
			elif (userChoice == paperCheck) and (cpuChoice == rockCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n YOU WIN!")
			else:
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n YOU LOSE")


