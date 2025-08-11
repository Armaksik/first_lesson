cars = ["mersedes", "BMW", "Hummer"]
print(cars[1])
print(cars[-1])
iterable = [1, 2, 2]
print(cars.append("lamb")) # добавляет x в конец списка.

print(cars.extend(iterable)) # добавляет все элементы из iterable в список.

print(cars.insert(0, "volvo")) # вставляет x на позицию i.

print(cars.remove("mersedes")) # удаляет первый элемент со значением x (иначе ValueError).

print(cars.pop(0)) # удаляет и возвращает элемент на позиции i (по умолчанию последний).

print(cars.index("BMW")) # возвращает индекс первого вхождения x.

print(cars.count("Hummer")) # считает, сколько раз x встречается в списке.

print(cars.reverse()) # разворачивает список.

print(cars.copy()) # поверхностная копия списка

print(cars.clear()) # очищает список.