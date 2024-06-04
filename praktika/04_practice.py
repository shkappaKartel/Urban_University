from nim_engine import *
from termcolor import cprint, colored

put_stones()
user_number = 1
while True:
    cprint('current position:', 'green')
    cprint(get_bunches(), 'black', 'on_white')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Player {} turn'.format(user_number), color=str(user_color))
    pos = input(colored('take from...', color=user_color))
    qua = input(colored('how many', color=user_color))
    take_from_bunch(position=int(pos)-1, quantity=int(qua))
    if is_gameover():
        break
    user_number = 2 if user_number == 1 else 1

cprint(f'Player {user_number} has won!', color='red')
