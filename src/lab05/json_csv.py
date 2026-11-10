import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:

    if Path(json_path).suffix.lower() != ".json":
        raise ValueError('Входной файл должен быть json')
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError("Выходной файл должен быть csv")

    try:
        with open(json_path, encoding="UTF-8") as file_in:
            records = json.load(file_in)

    except json.JSONDecodeError:
        raise ValueError('пустой файл или неподдерживаемая структура')

    if not isinstance(records, list) or not records or not all(isinstance(item, dict) for item in records):
        raise ValueError('пустой json или не тот формат')

    header = set()
    for item in records:
        for key in item:
            header.add(key)
    
    header = sorted(header) #алфавитный

    if not header:
        raise ValueError('не содержить данных для csv')
    if any(not key.strip() for key in header):
        raise ValueError('пустое назваание')
    
    rows = []
    for item in records:
        row = []
        for key in header:
            row.append(item.get(key, ""))
        rows.append(row)

    
    with open(csv_path, 'w', encoding="UTF-8", newline="") as file_out:
        writer = csv.DictWriter(file_out, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(zip(header, row)))

def csv_to_json(csv_path: str, json_path: str) -> None:

    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError('Входной файл должен быть csv')
    if Path(json_path).suffix.lower() != ".json":
         raise ValueError("Выходной файл должен быть json")

    try:
        with open(csv_path, encoding="UTF-8") as file_in:
            reader = csv.DictReader(file_in)
            records = list(reader)
    
    except(csv.Error, UnicodeDecodeError):
        raise ValueError('файл не читается')

    if not reader.fieldnames:
        raise ValueError('нет заголовка')
    if not records or not all(isinstance(item, dict) for item in records):
        raise ValueError('файл пуст или не тот формат')
    
    if any(not name.strip() for name in reader.fieldnames):
        raise ValueError("пустое название колонки")

    if len(set(reader.fieldnames)) != len(reader.fieldnames):
        raise ValueError("названия колонок не должны повторяться")

    with open(json_path, 'w', encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)