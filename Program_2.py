# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# import random
# x = random.randint(1, 1000)
# print(x)
# y = random.randint(1, 1000)
# print(y)
# clue_1 = x + y
# print(f"подсказка 1 сумма числа  x и y  = {clue_1}")
# clue_2 = x * y
# print((f"подсказка 2 произведение чисел  x и y  = {clue_2}"))
# numbers = (0, 0)
#
#
# for x_result in range(clue_1):
#     y_result = clue_1 - x_result
#     if x_result * y_result == clue_2:
#         numbers = (x_result, y_result)
#         break
#
# print(numbers)






import math
import random

x = random.randint(1, 1000)
print(x)
y = random.randint(1, 1000)
print(y)
clue_1 = x + y
print(f"подсказка 1 сумма чисел x и y = {clue_1}")
clue_2 = x * y
print(f"подсказка 2 произведение чисел x и y = {clue_2}")
numbers = (0, 0)

D = clue_1 ** 2 - 4 * clue_2

if D >= 0:
    x = (clue_1 + math.sqrt(D)) / 2
    y = (clue_1 - math.sqrt(D)) / 2
    print("Найдены два числа:")
    print(x, y)
else:
    print("Нет действительных решений для заданных условий.")