gram_weight = ("penny": "2.500g", "nickel": "5.000g", "dime": "2.268g", "quarter dollar": "5.670g", "half dollar": "11.340g", "dollar": "8.1g")

lb_weight = ("penny": "0.0055 lbs", "nickel": "0.01 lbs", "dime": "0.005000 lbs", "quarter dollar": "0.0125 lbs", "half dollar": "0.025000 lbs", "dollar": "0.018 lbs")

def userInput():
    user_in = raw_input("What is the weight of your coins? > ") # ask user to input coins
    in_list = [i for i in user_in.split()



print("-------------------------------------------------------------------------")
print("Hello! This program allows you to enter the weight of your coins and it will tell you how many of each you have.")
print("Please enter the weight in grams (g) or pounds (lbs) followed by the type of coin.")
userInput()
