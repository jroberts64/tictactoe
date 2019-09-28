
PLAYERS = ['X', 'O']


def display_board(board):
    print('\n\n\n\n\n')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print()


def get_move(board, player):
    loc = 0

    while not (is_valid_loc(loc) and is_loc_empty(board, loc)):
        try:
            loc = int(input(f'Where do you want to put your {player}? (1-9) '))
            if not is_valid_loc(loc):
                raise ValueError('Bad location value')
        except ValueError:
            print('Error: Please enter a number between 1 and 9')

    return loc


def is_loc_empty(board, loc):
    return board[loc] == ' '


def is_valid_loc(loc):
    return loc in range(1, 10)


def init_board(board):
    board[0] = ''
    for i in range(1, 10):
        board[i] = ' '


def update_board(board, player, loc):
    if loc in range(1, 10):
        board[loc] = player


def check_board_for_win(board):
    winners = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7],
               [3, 6, 9], [4, 5, 6], [7, 8, 9]]

    for locs in winners:
        if board[locs[0]] != ' ' and board[locs[0]] == board[locs[1]] == board[locs[2]]:
            return board[locs[0]]

    if is_board_full(board):
        return 'tie'

    return ''


def is_board_full(board):
    return ' ' not in board


def init_game(board):
    player = ' '
    init_board(board)
    display_board(board)

    while player not in PLAYERS:
        player = input(f'Who should go first, X or O? ').upper()
    return player


def main():
    board = ['', '', '', '', '', '', '', '', '', '']
    win = ''

    first_player = init_game(board)
    player_index = PLAYERS.index(first_player)

    while win == '':
        update_board(board, PLAYERS[player_index], get_move(board, PLAYERS[player_index]))
        display_board(board)
        win = check_board_for_win(board)
        player_index = not player_index

    print(f'The winner is {win}')


main()
