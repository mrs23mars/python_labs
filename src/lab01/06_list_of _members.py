n = int(input())

count_och = 0

for i in range(n):
    member = input()
    a, b, c, d = member.split()
    if d == 'True':
        count_och += 1

print(count_och, n - count_och)