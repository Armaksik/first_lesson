dict = {"имя": "Максим",
        "фамилия": "Ваганов",
        "Возраст": 16
}
print(dict.get("имя"))

other_dict = {"имя": "Александр",
        "фамилия": "Аликин",
        "Возраст": 26
}

print(dict.keys()) # возвращает ключи.

print(dict.values()) # возвращает значения.

print(dict.items()) # возвращает пары (ключ, значение).

print(dict.pop("имя")) # удаляет ключ и возвращает значение.

print(dict.update(other_dict)) # обновляет словарь.

print(dict.clear()) # очищает словарь.

dict.setdefault(key, default) # возвращает значение, если ключ есть, иначе добавляет default