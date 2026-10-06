
# Лабораторная работа №2



## Задание А (arrays.py)


### min_max

``` python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if nums == []:
        raise ValueError('список пуст')

    mal = nums[0]
    bol = nums[0]

    for x in range(len(nums)):
        if nums[x] <= mal:
            mal = nums[x]
        if nums[x] > bol:
            bol = nums[x]

    return (mal, bol)
```

Сначала происходит проверка на пустой список, далее находятся наименьшее и наибольшее значения в списке путем поочередного сравнения с предыдущим максимумом/минимумом.

![min_max](/images/lab02/arrays_min_max.png)


### unique_sorted


``` python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    for i in range(len(nums)-1):
        for x in range(len(nums)-1-i):
            if nums[x] > nums[x+1]:
                nums[x], nums[x+1] = nums[x+1], nums[x]
    for y in range(len(nums)-1, 0, -1):
        if nums[y] == nums[y-1]:
            del nums[y]
    return nums
```

Сначала сортировка сравнением каждого элемента друг с другом, далее удаление повторов

![unique_sorted](/images/lab02/arrays_unique_sorted.png)


### flatten

``` python
def flatten(mat: list[list | tuple]) -> list:
    
    result = []
    for i in range(len(mat)):
        if not isinstance(mat[i], list | tuple):
            raise TypeError('строка не строка строк матрицы')
        for j in range(len(mat[i])):
            
            result.append(mat[i][j])
    return result
```

Прверка матрицы на верные данные во всех строках, далее создание списка состоящего из всех элементов матрицы.

![flatten](/images/lab02/flatten.png)



## Задание B (matrix)


### transpose

``` python
def transpose(mat: list[list[float | int]]) -> list[list]:
    for i in range(len(mat)-1):
        if not len(mat[i]) == len(mat[i+1]):
            raise ValueError('рваная матрица')

    if mat == []:
        return mat
    
    row = len(mat)
    col = len(mat[0])
    result = []

    for x in range(col):
        result.append([0] * row)

    for j in range(row):
        for k in range(col):
            result[k][j] = mat[j][k]

    return result
```

Проверка матрицы на "прямоугольность", далее имндексы элементов "строка, столбец" меняются местами и добавляются в заранее созданную нулевую матрицу.

![transpose](/images/lab02/transpose.png)


### row_sums

``` python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    row = len(mat)
    col = len(mat[0])

    for i in range(1,len(mat)):
        if len(mat[i]) != len(mat[0]):
            raise ValueError('рваная матрица')

    result = []
    summ = 0

    for j in range(row):
        for k in range(col):
            summ += mat[j][k]
        result.append(summ)
        summ = 0 

    return(result)
```

Прверка на "прямоугольность", подсчет суммы каждой строки и добавление в новый список.

![row_sums](/images/lab02/row_sums.png)


### col_sums

``` python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    row = len(mat)
    col = len(mat[0])
    
    for i in range(1,len(mat)):
        if len(mat[i]) != len(mat[0]):
            raise ValueError('рваная матрица')

    result = []
    summ = 0 

    for j in range(col):
        for k in range(row):
            summ += mat[k][j]
        result.append(summ)
        summ = 0

    return result
```

Проверка на "прямоугольность", далее подсчет суммы столбцов и добавление в новый список.
p.s. можно было еще транспонировать матрицу и использовать функцию суммы строк

![col_sums](/images/lab02/col_sums.png)


## Задание C (tuples)

``` python
def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec

    if len(fio.split()) == 3:
        fam, name, otch = fio.split()
        fam_inic = (f'{fam.capitalize()} {name[0].upper()}.{otch[0].upper()}.')
    elif len(fio.split()) == 2:
        fam, name = fio.split()
        fam_inic = (f'{fam.capitalize()} {name[0].upper()}.')
    else:
        raise ValueError('Некорректное Имя')

    if not isinstance(group, str) or group.strip() == "" :
        raise ValueError('Некорректная группа')
    if not isinstance(gpa, float):
        raise TypeError('Некорректный GPA')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA не может быть больше 5 или меньше 0')
    
    result = (f'{fam_inic}, гр. {group}, GPA {gpa:.2f}')
    return result
```

Проверка корректности данных и вывод строки нужного вида.

![tuples](/images/lab02/tuples.png)