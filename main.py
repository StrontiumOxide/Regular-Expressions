import csv
import re

def main() -> None:

    """
    Главная функция модуля, запускающая программу.
    """

        # Открытие CSV-файла в виде вложенных списков.
    with open(file="phonebook_raw.csv", mode="r", encoding="utf-8-sig") as file:
        contact_list = list(csv.reader(file))

        # Изъятие заголовков из списка для дальнейшей записи в CSV-файл
    field = contact_list.pop(0)

        # Форматирование контактных номеров по шаблону.
    for contact in contact_list[1:]:
        pattern = r"\+?(7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})\-?(\d{2})\s?\(?(\w{3}\.)?\.?\s?(\d{4})?\)*"
        pattern_2 = r"+7(\2)\3-\4-\5 \6 \7"
        contact[5] = re.sub(pattern, pattern_2, contact[5]).strip()

        # Данная сортировка работает, если ФИО записаны в правильном порядке.
    for contact in contact_list:
        fio = " ".join(contact[:3]).split()

        if len(fio) == 3:
            contact[0] = fio[0]
            contact[1] = fio[1]
            contact[2] = fio[2]
        elif len(fio) == 2:
            contact[0] = fio[0]
            contact[1] = fio[1]
        elif len(fio) == 1:
            contact[0] = fio[0]

        # Генератор словаря с контактами. Нужен для того чтобы избавиться от дубликатов.
        # Сортировка списков по отчеству нужна для того, чтобы в словарь попадала более объёмная информация.
    contact_dict = {" ".join(contact[:2]): contact for contact in sorted(contact_list, key=lambda x: x[2])}

        # Запись новой информации в новый CSV-файл.
    with open(file="phonebook.csv", mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(field)
        writer.writerows(sorted(contact_dict.values()))

if __name__ == "__main__":
    #  Точка входа.
    main()