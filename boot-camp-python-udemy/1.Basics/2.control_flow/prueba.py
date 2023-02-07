import random

secret_num = random.randint(1, 100)

player_guesses = []

got_it = False

while not got_it:
    num = int(input("dime un número: \n"))

    if (num < 1) or (num > 100):
        print('u are out of bound')
        continue

    if num == secret_num:
        print('u did it, congrats')
        got_it = True
        break

    if len(player_guesses) == 0:

        if abs(num - secret_num) < 10:
            print(' warm')
        else:
            print('cold')

        player_guesses.append(num)
    else:
        if abs(num - secret_num) < 10:
            if abs(num - secret_num) < abs(player_guesses[-1] - secret_num):
                print('warmER')
            else:
                print('coolER')
        else:
            if abs(num - secret_num) > abs(player_guesses[-1] - secret_num):
                print('coolER')
            else:
                print('warmER')
        player_guesses.append(num)


name = 'davod'
# %% 
