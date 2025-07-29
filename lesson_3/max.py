list = [22, 13, 11, 44, 65, 34]
i = 1
max =[]

while i < len(list):
    if list[i] > list[i - 1]:
        max.append(list[i])
    i += 1

print("Элементы, которые больше педыдушего: ", max)
