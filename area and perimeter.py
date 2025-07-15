try:
    length = float(input("введите длину фигуры: "))
    width = float(input("введите ширину фигуры: "))

    print(f"периметр: {(length + width)*2}")
    print(f"пплощадь: {length * width}")
except:
    print("одна из переменных не является числом.")
