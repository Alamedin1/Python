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

def check_win(pl, board):
    #проверка на выйгрыш
    if board[1] == pl and board[2] == pl and board[3] == pl:
        print(pl+': Win')
        return 1
    elif board[4] == pl and board[5] == pl and board[6] == pl:
        print(pl+': Win')
        return 1
    elif board[7] == pl and board[8] == pl and board[9] == pl:
        print(pl+': Win')
        return 1
    elif board[1] == pl and board[4] == pl and board[7] == pl:
        print(pl+': Win')
        return 1
    elif board[2] == pl and board[5] == pl and board[8] == pl:
        print(pl+': Win')
        return 1
    elif board[3] == pl and board[6] == pl and board[9] == pl:
        print(pl+': Win')
        return 1
    elif board[1] == pl and board[5] == pl and board[9] == pl:
        print(pl+': Win')
        return 1
    elif board[3] == pl and board[5] == pl and board[7] == pl:
        print(pl+': Win')
        return 1
    else:
        return 0
 
def put_x(place):
    data_x_0[place] = 'X'

def put_0(place):
    data_x_0[place] = '0'

def emptyIndices(board): # возвращает найденные пустые клетки
    availableindex = []
    for i in range(1,len(board)):
        if i !='X' and i !='0':
            availableindex.append(i) # добавляет в массив i
    return availableindex

# функция минмакс
def minmax(newboard, human, kampukter, curent_player):
    availspots = emptyIndices(newboard) # доступные клетки
    if check_win(human, newboard): # проверка на поражение
        return -1
    if check_win(kampukter, newboard): # проверка на выйгрыш
        return 1
    if len(availspots) == 0: # проверка на ничью
        return 0
    moves = [] # массив для хранения всех объектов
    for i in availspots: # цикл по доступным клеткам
        move = {} # объект
        saveindex = newboard[i] # сохраняет i 
        newboard[i] = curent_player # далее ход за текущего игрока
        if curent_player == kampukter: # получаем очки 
            result = minmax(newboard, human, kampukter, human)
            move[i] = result
        else:
            result = minmax(newboard, human, kampukter, kampukter)
            move[i] = result
        newboard[i] = saveindex # очищаем клетку
        moves.append(move) # помещаем объект в массив
    bestmove = {}
    if curent_player == kampukter: 
        bestscore = -10
        for i in range(1,len(moves)): # пройти по ходам и выбрать ход с наибольшим кол-вом очков
            if moves[i] > bestscore:
                bestmove[i] = i
            else:
                bestscore = 10
                for i in range(1,len(moves)): # пройти по ходам и выбрать ход с наименьшим кол-вом очков
                    if moves[i] < bestscore:
                        bestmove[i] = i
    return moves[bestmove] # вернуть объект из массива ходов


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
    human = input('Enter: ')
    kampukter = ''
    if human.upper() == 'X':
        human = 'X'
        kampukter = '0'
    elif human.upper() == '0':
        human = '0'
        kampukter = 'X'
    else:
        print('Mistake. There is no such player ')
    return human, kampukter

if __name__ == '__main__':
    tmp =  minmax({1: '1', 2: 'X', 3: '3', 4: '0', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'},'0','X','X')
    print(tmp)
    # plot_table()
exit()