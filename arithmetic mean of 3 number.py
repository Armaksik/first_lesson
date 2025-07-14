try:
    first_number = int(input("введите первое число: "))
    second_number = int(input("введите второе число: "))
    third_number = int(input("введите третье число: "))

    print(f"среднее арифметическое 3-х чисел: {(first_number + second_number + third_number)/3} ")
except:
    print("одна из переменных не является числом")
