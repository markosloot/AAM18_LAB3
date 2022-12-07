#!/usr/bin/env python3
# coding=utf-8

import random


def random_array(n, m, max_value=21):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randrange(-20, max_value, 1)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%5d\t" % j, end='')
        print()


def counting(array):
    print()
    min_value = array[0][0]
    sum1 = 0
    mini = 0
    minj = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < min_value:
                min_value = array[i][j]
                mini = i
                minj = j
            if i == 0:
                sum1 += array[i][j]
    print("Минимум: %d [%d][%d]" % (min_value, mini, minj))
    print("Сумма первой строки: %d" % sum1)
    print()
    return min_value, mini, minj, sum1


def main():
    array = random_array(7, 8)
    print("Условие задания:\n"
          "Если сумма элементов первой строки больше \n"
          "минимального элемента, то заменить этот минимальный\n"
          "элемент на найденную сумму")

    print_array(array)
    min_value, mini, minj, sum1 = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':
            array = random_array(7, 8)
            print_array(array)
            min_value, mini, minj, sum1 = counting(array)
        elif key == '2':
            if sum1 < min_value:
                print("Сумма элементов первой строки (%d) не больше минимума %d" % (sum1, min_value))
                print("Задание не будет выполнено.")
            else:
                print("Сумма элементов первой строки (%d) больше минимума %d" % (sum1, min_value))
                array[mini][minj] = sum1

                print("Минимум заменен на сумму первой строки")
                print_array(array)
                break
        elif key == '3':
            exit(0)


if __name__ == '__main__':
    main()
