import sys

players = ['X','O']


def displayBoard(board):
    print('\n\n\n\n\n')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print()


def getMove(board,player):
    loc = 0

    while not (isValidLoc(loc) and isLocEmpty(board,loc)):
        try:
            loc = int(input(f'Where do you want to put your {player}? (1-9) '))
            if not isValidLoc(loc):
                raise ValueError('Bad location value')
        except:
            print('Error: Please enter a number between 1 and 9')
            
    return loc


def isLocEmpty(board,loc):
    return board[loc] == ' '


def isValidLoc(loc):
    return loc in range(1,10)


def initBoard(board):
    board[0] = ''
    for n in range(1,10):
        board[n] = ' '


def updateBoard(board,player,loc):
    if loc in range(1,10):
        board[loc] = player


def checkBoardForWin(board):
    winners = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],
        [3,6,9],[4,5,6],[7,8,9]]

    for locs in winners:
        if board[locs[0]] != ' ' and board[locs[0]] == board[locs[1]] == board[locs[2]]:
            return board[locs[0]]
    if isBoardFull(board):
        return 'tie'
    else:
        return ''


def isBoardFull(board):
    return ' ' not in board


def initGame(board):
    player = ' '
    initBoard(board)
    displayBoard(board)

    while player not in players:
        player = input(f'Who should go first, X or O? ').upper()
    return player


def main():
    board = ['','','','','','','','','','']
    win = ''

    first_player = initGame(board)
    player_index = players.index(first_player)

    while win == '':
        updateBoard(board,players[player_index],getMove(board,players[player_index]))
        displayBoard(board)
        win = checkBoardForWin(board)
        player_index = not player_index

    print(f'The winner is {win}')


main()
