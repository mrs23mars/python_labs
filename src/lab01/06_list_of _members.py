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