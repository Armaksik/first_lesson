set = {11, 22, 11, 44, 77, 11, 11}
print(set)
iterable = [11, 200, 300]
other_set = {80, 22, 11}

print(set.add(210)) # добавляет x в множество.

print(set.remove(11)) # удаляет x (если нет – KeyError).

print(set.discard(1)) # удаляет x, если он есть (без ошибки).

print(set.pop()) # удаляет и возвращает случайный элемент.

print(set.clear()) # очищает множество.

print(set.update(iterable)) # добавляет все элементы из iterable.

print(set.union(other_set)) # возвращает объединение множеств (|).

print(set.intersection(other_set)) # возвращает пересечение (&).

print(set.difference(other_set)) # возвращает разность (-).

print(set.symmetric_difference(other_set)) # возвращает симметричную разность (^).