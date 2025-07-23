def func(length, width):
    area = length * width
    perimeter = (length + area) * 2
    return area, perimeter

try:
    length = float(input("введите длину фигуры: "))
    width = float(input("введите ширину фигуры: "))
    area, perimetr = func(length, width)

except:
    print("одна из переменных не является числом")
print(f"площадь: {area}")
print(f"периметр: {perimetr}")

# todo вынести в отдельную функцию
