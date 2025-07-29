list = [11, 80, 44, 80, 33, 66]
max_value = list[0]
max_index = 0
i = 1

while i < len(list):
    if list[i] > max_value:
        max_value = list[i]
        max_index = i
    i += 1
print(f"наибольший элемент: {max_value}")
print(f"индекс наибольшего элемента: {max_index}")

