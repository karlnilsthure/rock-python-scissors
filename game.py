import random
computerScore = 0
userScore = 0
gameOver = False
options = ['Rock', 'Python', 'Scissors']


def userWinsRound():
    global userScore
    print(f'Computer choose "{computerInput}"')
    print('1 point to you')
    userScore += 1


def computerWinsRound():
    global computerScore
    print(f'Computer choose "{computerInput}"')
    print('1 point to computer')
    computerScore += 1


def printScore():
    print()
    print('- - - - - - - - - - - - -')
    print('SCORE')
    print(f'Computer: {computerScore} --- {userName}: {userScore}')
    print('- - - - - - - - - - - - -')
    print()


def resetScore():
    global userScore
    global computerScore
    userScore = 0
    computerScore = 0


def endOfRound():
    global gameOver

    if userScore == 3 or computerScore == 3:
        wonOrLostStr = 'won' if (userScore == 3) else 'lost'

        playAgain = input(
            f'You {wonOrLostStr}! Would you like to play again? (y/n) ')

        if playAgain == 'y':
            gameOver = False
            resetScore()
            printScore()
        else:
            gameOver = True


userName = input('Enter your name please: ')
print()

while not gameOver:
    userInput = input('Type "Rock", "Python" or "Scissors": ')

    randomNumber = random.randint(0, 2)
    computerInput = options[randomNumber]

    if userInput == computerInput:
        print(f'Computer choose "{computerInput}"')
        print('Draw')
    elif userInput == 'Rock':
        if computerInput == 'Scissors':
            userWinsRound()
        else:
            computerWinsRound()

    elif userInput == 'Python':
        if computerInput == 'Rock':
            userWinsRound()
        else:
            computerWinsRound()

    elif userInput == 'Scissors':
        if computerInput == 'Python':
            userWinsRound()
        else:
            computerWinsRound()
    else:
        print('Invalid input')

    printScore()

    endOfRound()
