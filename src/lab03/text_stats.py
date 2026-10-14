from src.lib.text import normalize, tokenize, count_freq, top_n
import sys 

phr =  sys.stdin.read()
norm_phr = normalize(phr)
wor = tokenize(norm_phr)
kol = count_freq(wor)
top = top_n(kol, n=5)
print(f'Всего слов: {len(wor)}')
print(f'Уникальных слов: {len(kol)}')
print(f'Топ 5: ')
for i in top:
    print(f'{i[0]}:{i[1]}')





















