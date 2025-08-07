list = [11, 33, 44, 66]
i = 0
sum = 0
min = 0
mul = 1
while i < len(list):
    try:
        sum += list[i]
        min -= list[i]
        mul *= list[i]
        i += 1
    except:
        print("этот символ не является знаком")
        break
print(sum, min, mul,)


