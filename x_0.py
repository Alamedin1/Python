#import toc_tic

data_x_0 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
#массив выбранных позиций
chousen = []

 
def plot_table():
    #построение игрового поля
    for i in range(7):
        if i in [0, 3, 6]:
            print('-'*13)
            print('| '+str(data_x_0[i+1])+ ' | '+str(data_x_0[i+2])+' | '+str(data_x_0[i+3])+' | ')
    print('-'*13)

def check_win(pl):
    #проверка на выйгрыш
    if data_x_0[1] == pl and data_x_0[2] == pl and data_x_0[3] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[4] == pl and data_x_0[5] == pl and data_x_0[6] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[7] == pl and data_x_0[8] == pl and data_x_0[9] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[1] == pl and data_x_0[4] == pl and data_x_0[7] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[2] == pl and data_x_0[5] == pl and data_x_0[8] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[3] == pl and data_x_0[6] == pl and data_x_0[9] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[1] == pl and data_x_0[5] == pl and data_x_0[9] == pl:
        print(pl+': Win')
        return 1
    elif data_x_0[3] == pl and data_x_0[5] == pl and data_x_0[7] == pl:
        print(pl+': Win')
        return 1
    else:
        return 0
 
def put_x(place):
    data_x_0[place] = 'X'

def put_0(place):
    data_x_0[place] = '0'

# try|except позволяет вылавливать любые исклчения и их обрабатывать
def chouse_place(player):
    try:
        place = input('Write number from 1 to 9 '+player+": ")
        place = int(place)
        if 1 <= place <= 9:
            if place in chousen:
                print('This place is not free')
                return 1
            else:
                chousen.append(place)
                if player == '0':
                    put_0(place)
                elif player =='X':
                    put_x(place)
                return 0
        else:
            print ('Write number from 1 to 9:')
            return 1
    except Exception as e: # вылавливает все исключения и их выводит
        print(e)
        return 1

def chouse_player():
    print('Choose who to play for Х or 0: ')
    player_1 = input('Enter: ')
    player_2 = ''
    if player_1.upper() == 'X':
        player_1 = 'X'
        player_2 = '0'
    elif player_1.upper() == '0':
        player_1 = '0'
        player_2 = 'X'
    else:
        print('Mistake. There is no such player ')
    return player_1, player_2


def two_player():
    pl_1, pl_2 = chouse_player()
    round = 0 # каждый раз при ничье эта переменная увеличивается
    plot_table()
    while True:
        if pl_1 == "X":
            round += 1
            # Chouse player for X
            res = chouse_place(pl_1)
            while res:
                res = chouse_place(pl_1)
            if check_win(pl_1):
                break
            plot_table()

            # Chouse player for 0
            res = chouse_place(pl_2)
            while res:
                res = chouse_place(pl_2)
            if check_win(pl_2):
                break
            plot_table()            
        if pl_1 == "0":
            round += 1
            # Chouse player for X
            res = chouse_place(pl_2)
            while res:
                res = chouse_place(pl_2)
            if check_win(pl_2):
                break
            plot_table()

            # Chouse player for 0
            res = chouse_place(pl_1)
            while res:
                res = chouse_place(pl_1)
            if check_win(pl_1):
                break
            plot_table()

            # Draw
            if round == 4:
                print('Draw!')
                break


if __name__ == '__main__':
    two_player()
    plot_table()


exit()
#==========================================
# new cod

#def two_player():