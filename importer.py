# Import materials from .xlsx file

import pandas as pd


def import_data(file: str) -> dict[str, tuple[str, float]]:
    sheet = pd.read_excel(file, sheet_name=0)
    data: dict[str, tuple[str, float]] = {}
    for i, a in enumerate(sheet["Unnamed: 5"]):
        if a and str(a) != "nan" and a != "Артикул":
            data[a] = (sheet["Unnamed: 0"][i], sheet["Unnamed: 11"][i])
    
    return data


def main() -> None:
    print(import_data("test.xlsx"))


if __name__ == "__main__":
    main()