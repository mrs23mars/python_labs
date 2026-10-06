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


choice = input()
print(f'Ввод:         Вывод:')
if choice == 'transpose':
    print('[[1, 2, 3]]->', transpose([[1, 2, 3]]))
    print('[[1], [2], [3]]->', transpose([[1], [2], [3]]))
    print('[[1, 2], [3, 4]]->', transpose([[1, 2], [3, 4]]))
    print('[]->', transpose([]))
    print('[[1, 2], [3]]->', transpose([[1, 2], [3]]))
elif choice == 'row_sums':
    print('[[1, 2, 3], [4, 5, 6]]->', row_sums([[1, 2, 3], [4, 5, 6]]))
    print('[[-1, 1], [10, -10]]->', row_sums([[-1, 1], [10, -10]]))
    print('[[0, 0], [0, 0]]->', row_sums([[0, 0], [0, 0]]))
    print('[[1, 2], [3]]->', row_sums([[1, 2], [3]]))
elif choice == 'col_sums':
    print('[[1, 2, 3], [4, 5, 6]]->', col_sums([[1, 2, 3], [4, 5, 6]]))
    print('[[-1, 1], [10, -10]]->', col_sums([[-1, 1], [10, -10]]))
    print('[[0, 0], [0, 0]]->', col_sums([[0, 0], [0, 0]]))
    print('[[1, 2], [3]]->', col_sums([[1, 2], [3]]))