"""1) Попросите пользователя ввести количество элементов для списка.

2) Создайте список, состоящий из целых случайных чисел от 0 до 100, заданного пользователем количества.

3) Выведите этот список с помощью цикла while.

4) С помощью множеств удалите из списка все повторяющиеся значения.

5) Выведите получившийся список с помощью цикла for."""
import random


number = int(input("введите количество элементов для списка: " ))
list = []

for i in range (number):
    random_number = random.randint(0, 100)
    list.append(random_number)

counter = 0

while counter < len(list):
    print(list[counter])
    counter += 1

print("----------")
set = set(list)
for i in set:
    print(i)


print("----------")
print(f"количество элементов в списке {len(list)}")
print(f"количество элементов в множестве {len(set)}")



# random_number = random.randint(0, 100)





