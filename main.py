from board import logo,board

board_list = ['' for _ in range(9)]
print(board_list)
print(logo)
choice = input('Do you want to play the game press Yes ,Enter No to Exit\n').lower()
user_icon = input('\nWhat you want to play with a "X" or a "O"\n').lower()
comp_icon = ''
if user_icon=='x':
    comp_icon = 'o'
else:
    comp_icon = 'x'
if choice == 'yes':
    user_input = int(input('Enter a position from 1 to 9 on the board\n'))
    board_list[user_input-1]=user_icon
    print(board.format(*board_list))


