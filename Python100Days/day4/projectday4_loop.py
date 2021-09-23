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

sleep = '''
                 _____|~~\_____      _____________
             _-~               \    |    
             _-    | )     \    |__/    \   \   
             _-         )   |   |  |     \   \   
             _-    | )     /    |--|      |  |
            __-_______________ /__/_______|  |_________
           (                |----         |  |
            `---------------'--\\\\      .`--'          
                                         `||||
'''

rocket = '''
                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\ 
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \:.    / `.
                   / .-'':._.'`-. \  
                   |/    /||\    \|
             jgs _..--"""````"""--.._
           _.-'``                    ``'-._
         -'                                '-
'''

def playGame():

	stringChoices = ["rock","paper","scissors"]
	asciiChoices = [rock, paper, scissors]

	print(rock,paper,scissors)

	userNumChoice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS.\n==> "))
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
			print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n\t DRAW!")
		else:
			if (userChoice == rockCheck) and (cpuChoice == scissorsCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n\t YOU WIN!")
			elif (userChoice == scissorsCheck) and (cpuChoice == paperCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n\t YOU WIN!")
			elif (userChoice == paperCheck) and (cpuChoice == rockCheck):
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n\t YOU WIN!")
			else:
				print(f"\nUSER CHOICE:\n {asciiUser}\n\nCPU CHOICE:\n {asciiCpu}\n\t YOU LOSE...")


# START GAME
try:
	while(True):
		playGame()
		userChoice = input("\nCONTINUE PLAYING? 0 = YES, 1 = NO.\n==> ")
		userChoiceNum = int(userChoice)

		if (userChoiceNum == 1):
			print("\n\tTHANKS FOR PLAYING KEEP ROCKING, PAPERING, AND SCISSORINGS!")
			print("\n\tTERMINATING...\n")
			print(f"{rocket}{sleep}")
			break
		elif (userChoiceNum == 0):
			continue
		else:
			print("\n\tINVALID CHOICE. NEXT TIME TRY 0 = YES, 1 = NO. LETS PLAY AGAIN SOON...\n\n\tTERMINATING...\n")
			print(f"{rocket}{sleep}")
			break

except ValueError: # to catch invalid type that is not an integer choice - eg) invalid string -  "fsfdftv"
	print("\n\tINVALID CHOICE. LETS PLAY AGAIN SOON...\n\n\tTERMINATING...\n")
	print(f"{rocket}{sleep}")

