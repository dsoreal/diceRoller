import random


def diceRollGame():
    numOfDice = int(input('How many dice would you like to roll?: '))

    i = 0
    sumOfDice = 0

    while i < numOfDice:
        i += 1
        dice = random.randint(1, 6)
        sumOfDice += dice
        print(dice)

    print('The sum of your rolls is ' + str(sumOfDice))

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


diceRollGame()
