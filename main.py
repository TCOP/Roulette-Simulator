#ONLY COLOR NOT NUMBER

import random

#CONSTANTS
Money = 100


def Roll():
    roll = random.randint(0,39)  #0,1 green     #2-20 black     #21-39 red

    return roll

def Bet():
    while True: # loop until valid bet amount is entered
        try:
            bet_amount = int(input("Enter Bet Amount: "))
            if bet_amount > 0 and bet_amount <= Money: # bet amount should be positive and not more than available money
                return bet_amount
            else:
                print(f"Bet amount should be more than 0 and less than or equal to {Money}")
        except ValueError: # in case non-integer is entered
            print("Invalid bet amount. Please enter a number.")
    

while Money > 0:
    bet_amount = Bet() # get the bet amount
    Money -= bet_amount # subtract bet amount from total money

else:
    print("Out of Money!")

