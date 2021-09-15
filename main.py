from board import logo, board
from random import randint

board_list = ['' for _ in range(9)]
print(logo)
user_list, comp_list = [], []


def check_win(check_list):
    matches = [[0, 1, 2], [3, 4, 5],
               [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
    if check_list in matches:
        return True
    else:
        return False


choice = input('Do you want to play the game press Yes ,Enter No to Exit\n').lower()
user_icon = input('\nWhat you want to play with a "X" or a "O"\n').lower()
comp_icon = ''
if user_icon == 'x':
    comp_icon = 'o'
else:
    comp_icon = 'x'
game_is_on = True
while game_is_on:
    if choice == 'yes':
        user_input = int(input('Enter a position from 1 to 9 on the board\n'))
        user_list.append(user_input)
        board_list[user_input - 1] = user_icon
        computer_input = randint(1, 9)
        while True:
            if board_list[computer_input-1] == '':
                board_list[computer_input - 1] = comp_icon
                break
            else:
                computer_input = randint(1,9)
        print(board.format(*board_list))
        res = check_win(user_list)
        if res:
            print('You Won The game thank you')
            game_is_on = False
        else:
            pass
    else:
        game_is_on = False
        print('Thank you for playing the Game')
