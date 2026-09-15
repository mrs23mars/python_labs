FIO = input('ФИО: ')
a, b, c = FIO.split()
print(f'Инициалы: {a[0]}{b[0]}{c[0]}')
print(f'Длина (символов): {len(a) + len(b) + len(c) + 2}') 