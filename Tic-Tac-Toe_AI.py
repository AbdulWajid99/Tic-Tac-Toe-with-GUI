# Base Board

board = [' ' for x in range[10]]


def insetLetter(letter, pos):
    board[pos] = letter


def spaceFree(pos):
    return board(pos)

# %%


def printBoard(board):
    print('    |    |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]+' | ')
    print('    |    |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]+' | ')
    print('    |    |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]+' | ')


def isWinner(b0, le):
    pass


def compMove():
    pass


def selectRandom(board):
    pass


def is boardFull():
    pass


def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
