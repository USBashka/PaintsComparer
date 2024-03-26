# Export data to csv files

import csv
import json


def export_csv(data: dict[str, list[str, float, str]], file: str) -> None:
    with open(file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        headers = ["Артикул", "Наименование", "Цена за грамм", "Комментарий"]
        writer.writerow(headers)

        for key, values in data.items():
            row = [key] + list(values)
            writer.writerow(row)


def export_colors_json(colors: dict[str, dict], file: str):
    try:
        with open(file, 'w', encoding='utf-8') as file:
            json.dump(colors, file, ensure_ascii=False, indent=4)
    except IOError:
        print("Произошла ошибка при записи файла.")
