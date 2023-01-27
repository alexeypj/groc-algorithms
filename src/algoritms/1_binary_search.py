# Бинарный поиск
# Это алгоритм, который принимает на вход отсортированный массив.
# Поиск работает путём постоянного деления массива на равные(условно) части и сравнения результата "больше" или меньше
# при этом на каждом шаге одна из частей отбрасываетя
# Алгоритм возвращает позицию элемента в массиве 

def binary_search(list, item):
    low = int(0)
    high = int(len(list) - 1)

    while low <= high:
        mid = int((low + high) / 2)       
        guess = list[mid]       
        if guess == item:
            print(mid)
            return mid
        if guess > item:
            high = int(mid - 1)
        else:
            low = int(mid + 1)
            print('None')
            return None 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search(list, 5) 



