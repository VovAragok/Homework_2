# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import math
# n = int(input("введите число N "))
# temp = 1
# i = 1
#
# while i < n:
#     i = i * 2
#     print(i)
#     temp += 1



# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


# N = int(input("Введите число N: "))
#  k = 0
#  power = 1 while power <= N:
#  print(power)
#  k += 1
#  power = 2 ** k


n = int(input("введите число "))
k = 0
i = 1
while i < n:
    print(i)
    k += 1
    i = 2 ** k
