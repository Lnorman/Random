import random
import sys
import time

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
                "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def question(): # ask the initial question
    user_input = raw_input("\nWhat is your question? > ")
    if user_input: # if question asked
        print("\nThinking..\n")
        time.sleep(1)
        print(random.choice(answers) + "\n")
    else: # catch an error
        print "huh?\n"
        question()
    again()

def again(): # after question, ask if another question
    user_input = raw_input("Would you like to ask another question? > ")
    if user_input == "yes": # if yes, go back to question()
        question()
    if user_input == "no": # if no, exit
        print("\nOkay, bye!\n")
        sys.exit(0)
    else: # if not yes or no
        print("\nhuh?\n")
        again()

print("\nYou may ask the magic 8 ball anything you desire!") # What will be printed on start, followed by calling question()
question()
