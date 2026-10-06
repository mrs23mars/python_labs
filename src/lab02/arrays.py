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

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    for i in range(len(nums)-1):
        for x in range(len(nums)-1-i):
            if nums[x] > nums[x+1]:
                nums[x], nums[x+1] = nums[x+1], nums[x]
    for y in range(len(nums)-1, 0, -1):
        if nums[y] == nums[y-1]:
            del nums[y]
    return nums

def flatten(mat: list[list | tuple]) -> list:
    
    result = []
    for i in range(len(mat)):
        if not isinstance(mat[i], list | tuple):
            raise TypeError('строка не строка строк матрицы')
        for j in range(len(mat[i])):
            
            result.append(mat[i][j])
    return result

choice = input()
print(f'Ввод:            Вывод:')

if choice == 'min_max':
    print('[3, -1, 5, 5, 0]->', min_max([3, -1, 5, 5, 0]))
    print('[42]->', min_max([42]))
    print('[-5, -2, -9]->', min_max([-5, -2, -9]))
    print('[1.5, 2, 2.0, -3.1]->', min_max([1.5, 2, 2.0, -3.1]))
    print('[]->', min_max([]))

elif choice == 'unique_sorted':
    print('[3, 1, 2, 1, 3]->', unique_sorted([3, 1, 2, 1, 3]))
    print('[]->', unique_sorted([]))
    print('[-1, -1, 0, 2, 2]->', unique_sorted([-1, -1, 0, 2, 2]))
    print('[1.0, 1, 2.5, 2.5, 0]->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))

elif choice == 'flatten':
    print('[[1, 2], [3, 4]]->', flatten([[1, 2], [3, 4]]))
    print('[[1, 2], (3, 4, 5)]->', flatten([[1, 2], (3, 4, 5)]))
    print('[[1], [], [2, 3]]->', flatten([[1], [], [2, 3]]))
    print('[[1, 2], "ab"]->', flatten([[1, 2], "ab"]))

