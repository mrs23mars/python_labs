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
        raise ValueError('')

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

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")