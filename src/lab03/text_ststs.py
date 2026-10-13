from lib.text import normalize, tokenize, count_freq, top_n

phr = input()
norm_phr = normalize(phr)
wor = tokenize(norm_phr)
kol = count_freq(wor)
top = top_n(kol, n=5)
print(f'Всего слов: {len(wor)}\
        Уникальных слов: {len(kol)}\
        Топ 5: ')
for i in top:
    print(f'{i[0]}:{i[1]}')





















