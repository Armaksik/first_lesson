
first_number = float(input("введите первое число: "))
second_number = float(input("введите второе число: "))
third_number = float(input("введите третье число: "))

def average(first_number, second_number, third_number):
    return (first_number + second_number + third_number) / 3
aver = average(first_number, second_number, third_number)
print(f"среднее арифметическое 3-х чисел: {aver} ")




# todo вынести в отдельную функцию
