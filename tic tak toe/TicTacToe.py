board = [' ' for x in range(10)]


def insertLetter(letter, pos): # function to insert a letter on the board
    board[pos] = letter


def spaceIsFree(pos): # function to check if any empty space is available or not
    return board[pos] == ' '


def printBoard(board):# function to print the board
    print("       ||     ||")
    print("   "+board[1]+"   ||  "+board[2]+"  ||  "+board[3])
    print("       ||     ||")
    print("-----------------------")
    print("-----------------------")
    print("       ||     ||")
    print("   "+board[4]+"   ||  "+board[5]+"  ||  "+board[6])
    print("       ||     ||")
    print("-----------------------")
    print("-----------------------")
    print("       ||     ||")
    print("   "+board[7]+"   ||  "+board[8]+"  ||  "+board[9])
    print("       ||     ||")


def isWinner(bo, le): # function to check if we have a winner
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove(): # function to take input from user and make the move on the specified location
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0] #it is the empty spaces on the board
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:] #A copy of board is made to check where to place the move
            boardCopy[i] = let 
            if isWinner(boardCopy, let): # if the winning move is let then move = i
                move = i 
                return move

    cornersOpen = []  #check for empty corners 
    for i in possibleMoves: 
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0: # if there are open corners present in the list then select the corner as a move
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves: # if 5 is available in possible move then select move = 5
        move = 5
        return move

    edgesOpen = [] # if edges are empty then make a list
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)  #select an edge as move

    return move


def selectRandom(li):  # function to select Random move 
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):  # function to check if the board is full or not
    if board.count(' ') > 1:
        return False
    else:
        return True


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
