from GAME import ConsoleGame
while True:

	print("\n**ITS THE NUMBERS GAME**")
	option=input("\nDo you want to start a new game? y/n?\nYour Choice: ")
	if option=='y':
		user=ConsoleGame()
		user.generate()
		user.choice()
		user.run()
	if option=='n':
		print("\n***GAME OVER***")
		break
