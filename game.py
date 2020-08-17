import random
computerScore = 0
userScore = 0
gameOver = False
options = ['Rock', 'Python', 'Scissors']


def userWins():
    global userScore
    print(f'Computer choose "{computerInput}"')
    print(f'1 point to you')
    userScore += 1


def computerWins():
    global computerScore
    print(f'Computer choose "{computerInput}"')
    print(f'1 point to computer')
    computerScore += 1


def printScore():
    print()
    print('- - - - - - - - - - - - -')
    print('SCORE')
    print(f'Computer: {computerScore} --- {userName}: {userScore}')
    print('- - - - - - - - - - - - -')
    print()


def endOfRound():
    global gameOver
    global userScore
    global computerScore
    if userScore == 3:
        playAgain = input('You won! Would you like to play again? (y/n) ')

        if playAgain == 'y':
            gameOver = False
            userScore = 0
            computerScore = 0
            printScore()
        else:
            gameOver = True

    if computerScore == 3:
        playAgain = input('You lost! Would you like to play again? (y/n) ')

        if playAgain == 'y':
            gameOver = False
            userScore = 0
            computerScore = 0
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
            userWins()
        else:
            computerWins()

    elif userInput == 'Python':
        if computerInput == 'Rock':
            userWins()
        else:
            computerWins()

    elif userInput == 'Scissors':
        if computerInput == 'Python':
            userWins()
        else:
            computerWins()
    else:
        print('Invalid input')

    printScore()

    endOfRound()
