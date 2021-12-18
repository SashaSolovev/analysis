alpha = []
OK = []
try:
    
    HowMuch = int(input("количество критериев:"))
    
    Matrix = [[0 for a in range(HowMuch)] for o in range(HowMuch)]
    for a in range(HowMuch):
        for o in range(HowMuch):
            if a == o:
                Matrix[a][o] = 1
            elif a - o > -1:
                Matrix[a][o] = int(
                    input('Введите данные попарного сравнения критериев ' + str(o + 1) + " и " + str(a + 1)
                          + " : "))
                if (Matrix[a][o] < 1 or Matrix[a][o] > 9):
                    quit("Ошибка! Надо от 0 до 9")
                Matrix[o][a] = Matrix[a][o]

    count = 1
    First = 0
    Second = 1
    OKsum = 0

    for m in range(HowMuch):
        for p in range(HowMuch):
            if p < Second:
                count = count * Matrix[First][p]
            else:
                count = count * (1 / Matrix[First][p])
        alpha.append(count)
        OK.append(pow(alpha[m], 1 / HowMuch))
        OKsum += OK[m]
        count = 1
        First += 1
        Second += 1



    for p in range(HowMuch):
        
        print("Весовой коэффициент для " + str(p + 1) + "-го критерия: " + str(round((OK[p] / OKsum), 2)))


except ValueError:
    quit("Ошибка!")
