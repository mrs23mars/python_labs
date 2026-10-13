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
![normalize](/images/lab03/normalize.png)

### tokenize
``` python 
def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)
```
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
    
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))
```
![count_freq_and_top_n](/images/lab03/count_freq_and_top_n.png)