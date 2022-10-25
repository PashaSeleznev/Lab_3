Thingsdict = {'д': (1, 10),
              'в': (3, 25),
              'п': (2, 15),
              'б': (2, 15),
              'а': (2, 20),
              'н': (1, 15),
              'т': (3, 20),
              'о': (1, 25),
              'ф': (1, 15),
              'и': (1, 5),
              'к': (2, 20),
              'р': (2, 20)
              }
Utility = []
# В моем варианте должен обязательно быть антидот. Поэтому сделаем у него полезность 1000.
for thing in Thingsdict:
    if thing != 'д':
        Utility_0 = thing, Thingsdict[thing][0], Thingsdict[thing][1], Thingsdict[thing][1] / Thingsdict[thing][0]
    else:
        Utility_0 = thing, Thingsdict[thing][0], Thingsdict[thing][1], 1000

    Utility.append(Utility_0)
# Сортируем массив по ценности
Sor_Utility = sorted(Utility, key=lambda x: int(x[3]), reverse=True)
print(Sor_Utility)
# kol - количество занятых ячеек;
# sum_v - ценность вещей, вошедших в рюкзак;
# sum_out - ценность вещей, не вошедших в рюкзак;
# start_sum - начальный запас очков
kol = 0
i = 0
sum_v = 0
sum_out = 0
start_sum = 15
Sor_Utility_best = []
# Так как у меня матрица 3*3, количество ячеек равно 9
while kol < 9:
    kol += Sor_Utility[i][1]  # Увеличиваем количество занятых ячеек
    sum_v += Sor_Utility[i][2]  # Увеличиваем суммарную ценность вошедших в рюкзак вещей
    if kol > 9:
        kol -= Sor_Utility[i][1]
        sum_v -= Sor_Utility[i][2]
        sum_out += Sor_Utility[i][2]
    else:
        for j in range(Sor_Utility[i][1]):
            Sor_Utility_best.append(Sor_Utility[i][0])
    i += 1
for x in range(i, len(Thingsdict)):
    sum_out += Sor_Utility[x][2]

for i in range(0, 9, 3):
    print('[', '],['.join(Sor_Utility_best[i: i + 3]), ']', sep='')

print('Итоговые очки выживания:', sum_v + start_sum - sum_out)
print()
print('Дополнительное задание №1')

# Дополнительное задание №1
all_sum = 0  # Сумма всех элементов
for i in range(len(Sor_Utility)):
    all_sum += Sor_Utility[i][2]
# Добавляем несколько пустых элементов, чтобы не было выхода за пределы массива
for i in range(5):
    Sor_Utility.append(('', 0, 0, 0))
boolean = 0

# Делаем перебор возможных комбинаций, чтобы найти элементы, удовлетворяющие условию в 7 ячеек. Если такие комбинации есть, то мы их выведем. В противном случае, напишем, что решений нет.
for i1 in range(1, 12):
    for i2 in range(i1 + 1, 13):
        for i3 in range(i2 + 1, 14):
            for i4 in range(i3 + 1, 15):
                for i5 in range(i4 + 1, 16):
                    if (Sor_Utility[i1][1] + Sor_Utility[i2][1] + Sor_Utility[i3][1] + Sor_Utility[i4][1] +
                        Sor_Utility[i5][1] + Sor_Utility[0][1]) == 7:
                        if (start_sum - all_sum + 2 * (
                                Sor_Utility[i1][2] + Sor_Utility[i2][2] + Sor_Utility[i3][2] +
                                Sor_Utility[i4][2] + Sor_Utility[i5][2] +
                                Sor_Utility[0][2])) > 0:
                            print(Sor_Utility[0][0], Sor_Utility[i1][0], Sor_Utility[i2][0], Sor_Utility[i3][0],
                                  Sor_Utility[i4][0], Sor_Utility[i5][0])
                            boolean = 1
if boolean == 0:
    print('РЕШЕНИЙ НЕТ!')

print()
print('Дополнительное задание №2')

# Дополнительное задание №2
c = []
k = 0

for i1 in range(1, 12):
    for i2 in range(i1 + 1, 13):
        for i3 in range(i2 + 1, 14):
            for i4 in range(i3 + 1, 15):
                for i5 in range(i4 + 1, 16):
                    for i6 in range(i5 + 1, 17):
                        if (Sor_Utility[i1][1] + Sor_Utility[i2][1] + Sor_Utility[i3][1] + Sor_Utility[i4][1] +
                            Sor_Utility[i5][1] + Sor_Utility[i6][1] + Sor_Utility[0][1]) == 9:
                            if (start_sum - all_sum + 2 * (
                                    Sor_Utility[i1][2] + Sor_Utility[i2][2] + Sor_Utility[i3][2] +
                                    Sor_Utility[i4][2] + Sor_Utility[i5][2] + Sor_Utility[i6][2] +
                                    Sor_Utility[0][2])) > 0:
                                c.append([Sor_Utility[0][0], Sor_Utility[i1][0], Sor_Utility[i2][0], Sor_Utility[i3][0],
                                          Sor_Utility[i4][0], Sor_Utility[i5][0], Sor_Utility[i6][0]])
                                if k == 0:
                                    print(c[0])
                                elif k != 0 and c[k] != c[k - 1]:
                                    print(c[k])
                                k += 1
