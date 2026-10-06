def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec

    if len(fio.split()) == 3:
        fam, name, otch = fio.split()
        fam_inic = (f'{fam.capitalize()} {name[0].upper()}.{otch[0].upper()}.')
    elif len(fio.split()) == 2:
        fam, name = fio.split()
        fam_inic = (f'{fam.capitalize()} {name[0].upper()}.')
    else:
        raise ValueError('Некорректное Имя')

    if not isinstance(group, str) or group.strip() == "" :
        raise ValueError('Некорректная группа')
    if not isinstance(gpa, float):
        raise TypeError('Некорректный GPA')
    if not 0.0 <= gpa <= 5.0:
        raise ValueError('GPA не может быть больше 5 или меньше 0')
    
    result = (f'{fam_inic}, гр. {group}, GPA {gpa:.2f}')
    return result

print(f'Ввод:                                    Вывод:')
print('("Иванов Иван Иванович", "BIVT-25", 4.6)', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print('("Петров Пётр", "IKBO-12", 5.0)', '     ', format_record(("Петров Пётр", "IKBO-12", 5.0)))
print('("Петров Пётр Петрович", "IKBO-12", 5.0)', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print('("  сидорова  анна   сергеевна ", "ABB-01", 3.999)', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print('("Иванов", "BIVT-25", 4.6)', '           ',format_record(("Иванов", "BIVT-25", 4.6)))
