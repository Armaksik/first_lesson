"""1) Создайте список из 5 чисел.

2) Определите сумму чисел в списке и выведите её.

3) Определите среднее арифметическое чисел в списке и выведите его."""

def sum(num):
     summ = 0
     for numbers in num:
          summ += numbers
     return summ
def aver(num):
     if not num:
          return 0
     summ = sum(num)
     return summ / len(num)


def main():
     num = [100, 29, 55, 77]
     summ_result = sum(num)
     aver_result = aver(num)

     print(f"среднее арифметическое списка: {summ_result}")
     print(f"среднее арифметическое списка: {aver_result}")
if __name__ == '__main__':
     main()
# todo узнать смысл 26 строки

