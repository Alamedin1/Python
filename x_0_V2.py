#import toc_tic

main_board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

 
def plot_board(board):
    #построение игрового поля
    for i in range(7):
        if i in [0, 3, 6]:
            print('-'*13)
            print('| '+str(board[i+1])+ ' | '+str(board[i+2])+' | '+str(board[i+3])+' | ')
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
 
def put_x(place,board):
    board[place] = 'X'

def put_0(place,board):
    board[place] = '0'

def emptyIndices(board): # возвращает найденные пустые клетки
    availableindex = []
    for i in range(1,len(board)+1):
        if board[i] !='X' and board[i] !='0':
            availableindex.append(i) # добавляет в массив i
    return availableindex

class Move:
    def __init__(self,index,score):
        self.index = index
        self.score = score

# функция минмакс
def minmax(newboard, human, kampukter, curent_player):
    availspots = emptyIndices(newboard) # доступные клетки
    if check_win(human, newboard): # проверка на поражение компьютера
        return Move(-1,-1)
    if check_win(kampukter, newboard): # проверка на выйгрыш компьютера
        return Move(-1,1)
    if len(availspots) == 0: # проверка на ничью
        return Move(-1,0)
    moves = [] # массив для хранения всех объектов
    for i in availspots: # цикл по доступным клеткам
        print("check empty cell ",i)
        move = Move(i,-1) # объект
        saveindex = newboard[i] # сохраняет i 
        newboard[i] = curent_player # далее ход за текущего игрока
        if curent_player == kampukter: # получаем очки 
            print("try to make kampukter move on cell ",i)
            result = minmax(newboard, human, kampukter, human)
            print("got score ",result.score," for kampukter on cell ",i)
            move.score = result.score
        else:
            print("try to make player move on cell ",i)
            result = minmax(newboard, human, kampukter, kampukter)
            print("got score ",result.score," for player on cell ",i)
            move.score = result.score
        newboard[i] = saveindex # очищаем клетку
        moves.append(move) # помещаем объект в массив
    
    bestmove = Move(-1,-10)
    if curent_player == kampukter:
        for m in moves: # пройти по ходам и выбрать ход с наибольшим кол-вом очков
            if m.score > bestmove.score:
                bestmove = m
    else:
        bestmove.score = 10
        for m in moves: # пройти по ходам и выбрать ход с наименьшим кол-вом очков
            if  m.score < bestmove.score:
                bestmove =  m
    print("show current player moves:")
    for m in moves:
        print("index ",m.index," score ",m.score)
 
    if bestmove.index == -1:
        print("error index!!")
        exit()
    
    print("best move is ",bestmove.index," with score ",bestmove.score)
    return bestmove # вернуть объект из массива ходов


# try|except позволяет вылавливать любые исклчения и их обрабатывать
def choose_place(player,board):
    while True:
        try:
            place = input('Write number from 1 to 9 '+player+": ")
            place = int(place)
            if 1 <= place <= 9:
                if board[place] == 'X' or board[place] == '0':
                    print('This place is not free')
                else:
                    if player == '0':
                        put_0(place,board)
                    elif player =='X':
                        put_x(place,board)
                    return
        except Exception as e: # вылавливает все исключения и их выводит
            print(e)
        plot_board(board)
        print ('Enter error, you should to write number from 1 to 9 suka!')

def choose_player():
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

def test_func():
    test_board = {1: '1', 2: 'X', 3: 'X', 4: '0', 5: '5', 6: '0', 7: '7', 8: '0', 9: '9'}
    plot_board(test_board)


if __name__ == '__main__':
    human,kampukter = choose_player()
    print('Your sign is ',human)
    print('Kampukter sign is ',kampukter)

    plot_board(main_board) #выводим состояние текущей доски
    current_player = '' #выбираем кто ходит первый
    if human == 'X':
        current_player = human
    else:
        current_player = kampukter
    
    test_board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    game_over = False
    while not game_over:
        current_kampukter_move = minmax(test_board,human,kampukter,current_player)
        if current_kampukter_move.index == -1:
            print("Game over!")
            game_over = True
            if current_kampukter_move.score == 1:
                print("Kampukter win!")
            else:
                if current_kampukter_move.score == -1:
                    print("Player win!")
                else:
                    print("Fucking nichya!")
        else:
            plot_board(test_board)
            if kampukter == current_player:
                print("kampukter should to go in cell ",current_kampukter_move.index)
                test_board[current_kampukter_move.index] = kampukter
                current_player = human
            else:
                print("make your move suka!")
                choose_place(human,test_board)
                current_player = kampukter
        plot_board(test_board)
    exit()

