# todo сделать так, чтобы пользователь вводил знак операции и программа выполняла эту операцию с массивом


list = [0]
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
        number *= list[i]
        i += 1
    else:
        print("этот символ не является знаком")
        break
print(number)

# todo нужно сделать так, чтобы программа выводила все операции
