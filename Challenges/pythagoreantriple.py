import sys

def userInput():
    print("---------------------------------------------------------------------")
    print("""\nHello! If you give me three numbers, I will check if they make a pythagorean triple!\n""")
    sides = raw_input("What numbers would you like me to check? > " + "\n")
    input_list = sides.split()
    input_list = [int(i) for i in input_list]
    for i in input_list:
        if input_list.count(i) < 3 or input_list.count(i) > 3:
            print("\nPlease enter 3 numbers or try entering three numbers seperated by spaces.\n")
            userInput()
        if input_list.count(i) == 3:
            c = max(sides)
            a = next(sides)
            b = next(sides)
            if a**2 + b**2 == c**2:
                print("It's a pythagorean triple!\n")
                again()
            else:
                print("Sorry, those numbers don't make a pythagorean triple\n")
                again()

def again():
    yesorno = raw_input("Would you like me to check some more numbers? > " + "\n")
    if yesorno == "no":
        print("Okay, bye!\n")
        sys.exit(0)
    elif yesorno == "yes":
        sides = raw_input("What numbers would you like me to check? > " + "\n")
        input_list = sides.split()
        input_list = [int(i) for i in input_list]
        for i in input_list:
            if input_list.count(i) < 3 or input_list.count(i) > 3:
                print("\nPlease enter 3 numbers or try entering three numbers seperated by spaces.\n")
                userInput()
            if input_list.count(i) == 3:
                c = max(sides)
                a = next(sides)
                b = next(sides)
                if a**2 + b**2 == c**2:
                    print("It's a pythagorean triple!\n")
                    again()
                else:
                    print("Sorry, those numbers don't make a pythagorean triple\n")
                    again()
    else:
        print("\nhuh?\n")
        again()

userInput()
