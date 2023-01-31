# imports
import random


# create the function for the whole game
def diceRollGame():
    diceType = []

    # create the function that chooses what dice
    def dice():
        diceQuest = input('What type of dice do you want?(d4, d6, d8, d10, d12, d20): ')
        diceCount = int(input('How many of that dice do you need?: '))
        diceNumCompare = 0

        # check if dice input is correct and add to list if correct
        if diceQuest == 'd4' or diceQuest == 'd6' or diceQuest == 'd8' or diceQuest == 'd10' or diceQuest == 'd12' or diceQuest == 'd20':
            while diceNumCompare < diceCount:
                diceType.append(diceQuest)
                diceNumCompare += 1
        else:
            print('input not recognized. Try again.')
            dice()

    dice()

    # create function to add more types of dice if the user wants
    def moreD():
        more = True
        while more:
            moreDice = input('Would you like to add more dice? 1 for yes, 2 for no: ')
            if moreDice == '1':
                dice()
            elif moreDice == '2':
                print(diceType)
                more = False
            else:
                print('Input not recognized try again')
                moreD()

    moreD()

    i = 0
    sumOfDice = 0

    # check the dice type against the list and roll a random integer based on which dice it is on
    while i < len(diceType):
        if diceType[i] == 'd4':
            diceNumRoll = random.randint(1, 4)
            sumOfDice += diceNumRoll
            print('d4 = ' + str(diceNumRoll))
            i += 1
        elif diceType[i] == 'd6':
            diceNumRoll = random.randint(1, 6)
            sumOfDice += diceNumRoll
            print('d6 = ' + str(diceNumRoll))
            i += 1
        elif diceType[i] == 'd8':
            diceNumRoll = random.randint(1, 8)
            sumOfDice += diceNumRoll
            print('d8 = ' + str(diceNumRoll))
            i += 1
        elif diceType[i] == 'd10':
            diceNumRoll = random.randint(1, 10)
            sumOfDice += diceNumRoll
            print('d10 = ' + str(diceNumRoll))
            i += 1
        elif diceType[i] == 'd12':
            diceNumRoll = random.randint(1, 12)
            sumOfDice += diceNumRoll
            print('d12 = ' + str(diceNumRoll))
            i += 1
        elif diceType[i] == 'd20':
            diceNumRoll = random.randint(1, 20)
            sumOfDice += diceNumRoll
            print('d20 = ' + str(diceNumRoll))
            i += 1

    print('The sum of your rolls is ' + str(sumOfDice))

    # determine if the user would like to play again
    def playAgain():
        playAgn = input('Would you like to roll again? 1 for yes, 2 for no: ')
        if playAgn == '1':
            diceRollGame()
        elif playAgn == '2':
            exit()
        else:
            print('incorrect entry, try again')
            playAgain()

    playAgain()


# run the program
diceRollGame()
