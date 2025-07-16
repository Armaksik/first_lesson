try:
    first_number = float(input("введите первое число: "))
    second_number = float(input("введите второе число: "))
    third_number = float(input("введите третье число: "))

    sum_nums = (first_number + second_number + third_number)

    print(f"среднее арифметическое 3-х чисел: {(sum_nums/3)} ")
except:
    print("одна из переменных не является числом")


# todo вынести в отдельную функцию
