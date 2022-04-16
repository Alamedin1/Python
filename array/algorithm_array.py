#Условие:
# 1. Есть массив отсортированных чисел
# Пример:
# [-3, -1, 3, 7, 10]
# 2. Есть дополнительное число 
# Пример:
# Число 6
# 3. Необходимо найти в этом массиве два числа, которые в сумме дают дополнительное число

# Для примера выше ответом будет [-1, 7], тк -1+7=6
# Если в массиве нету такой пары, то ответом будет пустой массив []

# Еще несколько примеров:
# 1. [-20, -7, -3, 6, 8] и 5
# Ответ [-3, 8]
# 2. [-2, -1, 3, 4, 5] и 2
# Ответ [-2, 4] или [-1, 3]
# 3. [3, 5, 6, 8] и 8
# Ответ [] тк пары нету

number = 9
matrix = [-1, -3, 7, 10]
# [-2, -1, 3, 4, 5]
# [-1, -3, 7, 10]
result = []
def sorting (array):
    for i in range(len(array)):
        small_elem =  i
        for j in range(i+1, len(array)):
            if array[j] < array[small_elem]:
                small_elem = j
        array[i], array[small_elem] = array[small_elem], array[i]
    return print(matrix)

def algorithm_two_cycle (array, number):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == number:
                return print(array[i], array[j])
    return print("Таких чисел нет! Ответ: [] ")

def algorithm_simple (array, number):
    left_border = 0
    right_border = len(array)-1
    while (left_border < right_border):
        if array[left_border] + array[right_border] > number:
            right_border = right_border - 1
        elif array[left_border] + array[right_border] == number:
            return print("Answer Index: ", left_border + 1, right_border + 1, "Answer Elements: ",  array[left_border], array[right_border])
        else:
            left_border = left_border + 1
    return []


def algorithm_index (array, number):
    # class object:
    #     def __init__(self, array, index):
    #       object[array[index]] = index  
    object = {}
    for i in range(len(array)):
        object[array[i]] = i
        print(object)
        print(array[i])
        print(i)
    for i in range(len(array)):
        decision = number - array[i]
        print(decision)
        if object[decision] and object[decision] != i:
            print(object[decision])
            return print(i, object[decision])
    return print([])


def algorithm_to_answer (array, number):
    for i in range(len(array)):
        find = number - array[i]
        print(find)
        left_border = i+1
        print(left_border)
        right_border = len(array)-1
        print(right_border)
        while (left_border <= right_border):
            middle = left_border + (right_border - left_border)/2
            if array[int(middle)] == find:
                return print(array[i], array[int(middle)])
            if find < array[int(middle)]:
                right_border = middle - 1
            else:
                left_border = middle + 1
    return ("Таких чисел нет! Ответ: [] ")

sorting (matrix)
# algorithm_two_cycle(matrix, number)
# algorithm_simple(matrix, number)
# algorithm_index(matrix, number)
# algorithm_to_answer(matrix, number)

