####The Magic Ball Game
import random

def get_user_input():
	return input("What is your question?")

def get_answer():
    Possible_Answer = [ "It is certain",
                    "It is decidedly so",
                    "Without a doubt",
                    "Yes definitely",
                    "You may rely on it",
                    "As I see it, yes",
                    "Most likely",
                    "Outlook good",
                    "Yes",
                    "Signs point to yes",
                    "Reply hazy try again",
                    "Ask again later",
                    "Better not tell you now",
                    "Cannot predict now",
                    "Concentrate and ask again",
                    "Don't count on it",
                    "My reply is no",
                    "My sources say no",
                    "Outlook not so good",
                    "Very doubtful"]

    return random.choice(Possible_Answer)

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

		else:
			print("I’m sorry, I can only answer questions.")
			check = True
	

magic_8()

