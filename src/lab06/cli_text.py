import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n
def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        with open(args.input, encoding='UTF-8') as file_in:
            for number, line in enumerate(file_in, start=1):
                if args.n:
                    print(f"{number}: {line}", end="")
                else:
                    print(line, end="")


    elif args.command == "stats":
        with open(args.input, encoding="UTF-8") as file_in:
            rtext = file_in.read()
            text = normalize(rtext)
            tokens = tokenize(text)
            freq = count_freq(tokens)
            result = top_n(freq, args.top)
            for word, count in result:
                print(f"{word}: {count}")

if __name__ == "__main__":
    main()