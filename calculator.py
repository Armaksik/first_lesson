def is_zero(number1):
    if number1 == 0:
        return True
    else:
        return False


try:
    x = input("введите первое число: ")
    c = input("введите второе число: ")
    x = int(x)
    c = int(c)
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
except:
    print("одна из переменных не является числом")



