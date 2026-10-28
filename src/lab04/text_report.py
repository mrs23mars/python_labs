import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab04.io_txt_csv import read_text, write_csv

def main() -> None:
    parser = argparse.ArgumentParser(description="Парсер лабы")
    parser.add_argument("--in", dest="input", help="Путь к файлу", required=True)
    parser.add_argument("--out", help="Путь к отчёту", required=True)
    parser.add_argument("--encoding", default="utf-8", help="Кодировка")
    args = parser.parse_args()



    try:
        path = Path(args.input)
        out_path = Path(args.out)
        text = normalize(read_text(path=path, encoding=args.encoding))
        tokens=tokenize(text)
        counts = count_freq(tokens)
        rows = top_n(counts, len(counts))
        write_csv(rows=rows, path=out_path, header=('word', 'count'))
        print(f'Всего слов: {len(tokens)}')
        print(f'Уникальных слов: {len(counts)}')
        print(f'Топ-5:')
        for word, count in top_n(counts, n=5):
            print(f'{word}:{count}')

        
    except FileNotFoundError as error:
        print(f'Файл не найден: {error.filename}')
        return None
    except (UnicodeDecodeError, LookupError) as error:
        print(f'Ошибка кодировки')
    except error as error:
        print(f'Ошибка: {error}')

if __name__ == "__main__":
    main()