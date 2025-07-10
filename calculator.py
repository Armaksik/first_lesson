def is_zero(number1):
    if number1 == 0:
        return True
    else:
        return False

def is_number(number1, number2):
    if isinstance(number1, int) and isinstance(number2, int):
        return True
    else:
        return False

x = input("введите первое число: ")
c = input("введите второе число: ")
if is_number(x,c):
    print(f"сумма чисел: {x+c}" )
    #print(f"сумма чисел: " , {x+c} )
    #print(f"сумма чисел: " + {x+c} )
    print(f"разность чисел: {x-c}" )
    print(f"умножение чисел: {x*c}" )


    if is_zero(c):
       print("число с равно 0")
    else:
        print(f"деление чисел: {x / c}")
        print(f"остаток от деления чисел: {x%c}" )
        print(f"деление без остатка чисел: {x//c}" )
else:
    print("одна из переменных не является числом")



