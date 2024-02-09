import csv
import re
from pprint import pprint

def main() -> None:

    """
    Главная функция модуля, запускающая программу.
    """

        # Открытие CSV-файла в виде вложенных списков.
    with open(file="phonebook_raw.csv", mode="r", encoding="utf-8-sig") as file:
        result = csv.reader(file)
        contact_list = list(result)

        # Форматирование контактных номеров по шаблону.
    for contact in contact_list[1:]:
        pattern = r"\+?(7|8)\s?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})\-?(\d{2})\s?\(?(\w{3}\.)?\.?\s?(\d{4})?\)*"
        pattern_2 = r"+7(\2)\3-\4-\5 \6 \7"
        contact[5] = re.sub(pattern, pattern_2, contact[5])

        # Ниже пытаюсь правильно разбить по колонкам ФИО.
        # [0] - last_name, [1] - first_name, [2] - surname
    for contact in contact_list:
        for element in contact[:3]:
            if bool(element):
                variable_list = element.split()
                if len(variable_list) == 3:
                    contact[0] = variable_list[0]
                    contact[1] = variable_list[1]
                    contact[2] = variable_list[2]
                elif len(element.split()) == 2:
                    contact[0] = variable_list[0]
                    contact[1] = variable_list[1]

        # В этом цикле обхожу все обновлённые контакты для наглядности.
    for order, contact in enumerate(contact_list):
        print(f"{order+1}) {contact}")
        print()
    
    """
    В контакте под номером 4 ФИО стоят не по своим местам. 
    Как вообще оптимизировать данный процесс? Или вообще есть
    какая-нибудь альтернатива, как это быстро сделать? То что
    в ДЗ писали про join я не понял. Где его тут вообще можно
    использовать. Если только потом, чтобы избавиться от
    дубликатов
    """

if __name__ == "__main__":
    #  Точка входа.
    main()