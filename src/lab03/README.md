# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание А (lib/text.py)
### normalize
``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е')

    text = ' '.join(text.split())

    return text
```
Функция меняет регистр на нижний, заменяет ё на е и заполняет строку нормальными словами через 1 пробел 
![normalize](/images/lab03/normalize.png)

### tokenize
``` python 
def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)
```
Разделяет слова подходящие под критерии и возвращает список 
![tokenize](/images/lab03/tokenize.png)

### count_freq and top_n
``` python 
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for w in tokens:
        freq[w] = freq.get(w, 0) + 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError

    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
```
count_freq в пустой словарь добавляет слова из списка токенов с количеством повторений этих слов
top_n сортирует слова по количеству повторений, поднимает ошибку если словарь пуст
![count_freq_and_top_n](/images/lab03/count_freq_and_top_n.png)


## Задание B (text_stats)
``` python 
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
```
![text_stats](/images/lab03/text_stats_test01.png)
