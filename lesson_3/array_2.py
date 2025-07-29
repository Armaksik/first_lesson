# todo сделать так, чтобы пользователь вводил знак операции и программа выполняла эту операцию с массивом


list = [1, 20, 32]
i = 0
number = 0
Operation = input("введите операцию: ")
while i < len(list):
    if Operation == "+":
        number += list[i]
        i += 1
    elif Operation == "-":
        number -= list[i]
        i += 1
    elif Operation == "*":
        multiplicatot = int(input("введите число для умножения: "))
        multiplicatot *= list[i]
        i += 1
print(number or multiplicatot)

# todo не получилось решить
