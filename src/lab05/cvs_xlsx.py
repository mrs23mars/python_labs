import csv
from pathlib import Path
from openpyxl import Workbook



def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    if Path(csv_path).suffix.lower() != '.csv':
        raise ValueError('Входной файл должен быть csv')
    if Path(xlsx_path).suffix.lower() != '.xlsx':
        raise ValueError('Выходной файл должен быть xlsx')

    try:
        with open(csv_path, encoding="UTF-8", newline="") as file_in:
            reader = csv.reader(file_in)
            rows = list(reader)
    except (csv.Error, UnicodeDecodeError):
        raise ValueError('Файл не читается')    

    if not rows:
        raise ValueError("файл пустой")
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)

    for column in ws.columns:
        max_len = 0

        for cell in column:
            if len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

    ws.column_dimensions[column[0].column_letter].width = max_len

    wb.save(xlsx_path)
