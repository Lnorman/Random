import sys

def userInput(): # ask the question
    input_list = [] # set up an empty list to hold the user_input
    while len(input_list) != 3: # keep asking the question as long as use has not entered 3 numbers
        sides = raw_input("\nWhat numbers would you like me to check? > ")
        input_list = [int(i) for i in sides.split()] # call int() for each number entered by the user seperated by spaces and put it into a list
    if len(input_list) == 3: # user has entered 3 numbers
        a, b, c = sorted(input_list) # assign value to each number with "c" being the largest or the hypotenuse
        if a**2 + b**2 == c**2: # pythagorean theorem
            print("\nIt's a pythagorean triple!\n")
            again()
        else: # if numbers dont make pythagorean triple, go to again
            print("\nSorry, those numbers don't make a pythagorean triple\n")
            again()
    else: # if numbers dont make pythagorean triple, go to again
        print("\nSorry, those numbers don't make a pythagorean triple\n")
        again()

def again():
    yesorno = raw_input("Would you like me to check some more numbers? > ")
    if yesorno == "no": # exit if no more numbers to check
        print("\nOkay, bye!\n")
        sys.exit(0)
    elif yesorno == "yes": # call userInput() if more numbers to check
        userInput()
    else: # catch errors
        print("\nhuh?\n")
        again()


print("---------------------------------------------------------------------") # What will print on start, followed by calling userInput()
print("""\nHello! If you give me three numbers, I will check if they make a pythagorean triple!\n""")
userInput()
