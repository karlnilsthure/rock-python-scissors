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


userName = input('Type your name: ')
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

    if userScore == 3:
        gameOver = True
        print('You win')

    if computerScore == 3:
        gameOver = True
        print('You loose')
