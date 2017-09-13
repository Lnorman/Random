import random
import sys
import time

answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
                "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def question():
    question = raw_input("What is your question? > ")
    if question:
        print("\nThinking..\n")
        time.sleep(1)
        print(random.choice(answers) + "\n")
    else:
        print "huh?\n"
    again()

def again():
    question = raw_input("Would you like to ask another question? > ")
    if question == "yes":
        raw_input("\nWhat is your question? > ")
        if question:
            print("\nThinking..\n")
            time.sleep(1)
            print(random.choice(answers) + "\n")
        else:
            print "huh?"
        again()
    else:
        print("\nOkay, bye!\n")
        sys.exit(0)

print("\nYou may ask the magic 8 ball anything you desire!\n")
question()
