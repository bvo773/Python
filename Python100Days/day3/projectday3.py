
print('''
*********************************
PROJECT RESCUING PRINCESS HINATA!
																	/,   ,|   ,|
													/| /(  ,' / ,//
										\`( |/ /,'  (,/ |
											\ \ ` `   `  /--,
									_,_\ `  ` `  ``  /__
										'-.____________`  /
												[  \@,    :] `--,-..-
												[__________]__,'-._/
													)'o\ ' o) \/ )
													\  /   __  ./
														\=`   ==,\..\ 
															\ -. `,' (333
															3`--''    333.
													,333_) /mm33333:.
												|:#:mmmmmm333333::
												|:#:333333333::##'
												':#:ctr3333''#####
													|:#:#############
													|:#:#############
													|:#:###########|#
													/:#:|:::|::::::|:(
													):#:|::::::::::|:/
												/:#;/:::::<::::::|(
***********************************
''')



print("Welcome to Saving Princess Hinata Quest! .")
print("Your mission is to find princess Hinata and bring her back alive!")

choice = str(input("There is a lot of dangerous shinobies in front. Would you like to go \"Left\" or \"Right\"?\n ")).lower()
if choice == "left":
	choice = str(input('"I can sense her chakra inside the tunnel". "Go" or Wait"?\n ')).lower()
	if choice == "wait":
		choice = str(input("Which chambers to open? \"Red\",\"Blue\",\"Yellow\"?\n ")).lower()
		if choice == "red":
			print("You were burned by fire. Game Over!")
		elif choice == "blue":
			print("You were attacked by Orochimarau!")
		elif choice == "yellow":
			print("\"Naruto reunited with Hinata. You Win!\"")
		else:
			print("GAME OVER")
	else:
		print("You were ambused and swallowed by Kabuto's snakes. Game over")    
	print()
else:
	print("You fell into a booby trap. Game over!")
