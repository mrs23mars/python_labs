import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е')

    text = ' '.join(text.split())

    return text

def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for w in tokens:
        freq[w] = freq.get(w, 0) + 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError
    
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))

prik = input()

if prik == 'normalize':
    print('Ввод:                    Вывод:')
    print('ПрИвЕт\\nМИр\\t ->      ', normalize("ПрИвЕт\nМИр\t"))
    print('ёжик, Ёлка ->           ', normalize("ёжик, Ёлка"))
    print('Hello\\r\\nWorld ->     ', normalize("Hello\r\nWorld"))
    print('  двойные   пробелы   ->', normalize("  двойные   пробелы  "))

elif prik == 'tokenize':
    print('Ввод:                   Вывод:')
    print('привет мир ->         ', tokenize("привет мир"))
    print('hello,world!!! ->     ', tokenize("hello,world!!!"))
    print('по-настоящему круто ->', tokenize("по-настоящему круто"))
    print('2025 год ->           ', tokenize("2025 год"))
    print('emoji 😀 не слово ->  ', tokenize("emoji 😀 не слово"))

elif prik == 'count_freq and top_n':
    print('Ввод:                        Вывод:')
    print('["a","b","a","c","b","a"] ->', count_freq(["a", "b", "a", "c", "b", "a"]))
    print('                            ', top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
    print('["bb","aa","bb","aa","cc"] ->', count_freq(["bb", "aa", "bb", "aa", "cc"]))
    print('                             ', top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))