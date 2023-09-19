def even_numbers_sort():
    n = int(input('Введите количество элементоу:\n'))
    list_1 = [0] * n
    num_1 = 0
    for i in range(n):
        print("list_1[", i, "]=\n", sep="", end="")
        list_1[i] = int(input())
    print("Получившийся список:", list_1)
    for i in range(n):
        if list_1[i] % 2 == 0:
            num_1 = num_1 + 1
    print("Количество чётных элементов:", num_1)

even_numbers_sort()


"""
Лабораторная 1_9
Написать функцию, которая принимает целочисленный список, состоящий 
из n элементоу и возвращает количествочётных чисел в списке
"""