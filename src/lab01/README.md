# Лабораторная работа №1


## Задание №1

```
name = input('Имя: ')
age = int(input('Возраст: '))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
После ввода данных программа выводит приветствие с помощью f-строки.

![1 задание](/images/lab01/01_greeting.png)


## Задание №2

```
a = float(input("a: ").replace(",", "."))
b = float(input('b: ').replace(',', '.'))
print(f'sum={(a+b):.2f}; avg={(a+b)/2:.2f}')
```
При вводе данных заменяет "," на ".", если такое требуется, далее выводит сумму и среднее значение с округлением до 2 знаков после запятой.

![2 задание](/images/lab01/02_sum_avg.png)


## Задание №3

```
price = float(input('Цена: '))
discount = float(input('Скидка: '))
vat = float(input('НДС: '))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')
```
После ввода данных считает цену со скидкой, сумму НДС и итоговую сумму. С помощью f-строки выводит красивый чек.

![3 задание](/images/lab01/03_discount_vat.png)


## Задание №4 

```
minutes = int(input('Минуты: '))
hh = minutes//60
mm = minutes%60
print(f'{hh}:{mm:02d}')
```
С помощью целочисленного деления и деления с остатком считает часы и минуты. Выводит с помощью f-строки.

![4 задание](/images/lab01/04_minutes_to_hhmm.png)


## Задание №5 

```
FIO = input('ФИО: ')
a, b, c = FIO.split()
print(f'Инициалы: {a[0]}{b[0]}{c[0]}.')
print(f'Длина (символов): {len(a) + len(b) + len(c) + 2}') 
```
После ввода данных разделяет ФИО и выводит первые символы фамилии имен и отчества, длину ФИО с помощью len.

![5 задание](/images/lab01/05_initials_and_len.png)

## Задание №6

```
n = int(input('in_1: '))

count_och = 0

cin = 1

for i in range(n):
    cin += 1
    member = input(f'in_{cin}: ')
    a, b, c, d = member.split()
    if d == 'True':
        count_och += 1

print(f'out: {count_och} {n - count_och}')
```
После ввода количества строк, через цикл фор вводятся самми строки, разделяются, далее проверяется True/False, если True счетчик+1. Выводится количество людей на очном формате обучения=счетчику, на заочном формате обучения=количество строк-счетчик

![6 задание](/images/lab01/06_list_of_members.png)

