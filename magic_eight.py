####The Magic Ball Game
def get_user_input():
	return input("What is your question?")

def get_answer():
	return 0

def magic_8():
	check = True
	while check:
		answer = get_user_input()
		answer.strip()
		if answer[-1]=='?':
			print(get_answer())
			if input("Do you want to quit? type in quit.").lower() == "quit":
				check = False

			else:
				check = True

	

magic_8()