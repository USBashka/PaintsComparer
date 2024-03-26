## Programm entry point

import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QHeaderView

import importer, exporter


def main(args = sys.argv):

    def _on_new_color_clicked():
        print("Adding new color...")

    def _on_colors_table_clicked(index):
        first_column_index = model.index(index.row(), 0)  # 0 - это номер первого столбца
        value = model.data(first_column_index, role=Qt.ItemDataRole.DisplayRole)
        window.color_info = uic.loadUi("scenes/color_dialog.ui")

        window.color_info.ColorName.setText("Цвет: " + value)
        window.color_info.Date.setText(colors[value]["date"])
        window.color_info.Comment.setText(colors[value]["comment"])
        window.color_info.Variant1Name.setText(colors[value]["variants"][0]["name"])
        window.color_info.Variant2Name.setText(colors[value]["variants"][1]["name"])
        window.color_info.TotalWeight1.setText(str(round(sum(colors[value]["variants"][0]["recipe"].values()), 2)) + " г")
        window.color_info.show()
    
    colors = importer.import_colors_json("test.json")
    app = QtWidgets.QApplication(args)

    window = uic.loadUi("scenes/main.ui")

    window.AddColor.clicked.connect(_on_new_color_clicked)
    window.ColorsTable.setModel(get_colors_table_model(colors))
    header = window.ColorsTable.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    window.ColorsTable.clicked.connect(_on_colors_table_clicked)
    window.show()
    app.exec()


def get_colors_table_model(colors: dict):
    global model
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(["Название цвета", "Вариант 1", "Вариант 2", "Экнономия"])

    for i, name in enumerate(colors):
        model.setItem(i, 0, QStandardItem(name))
        price1 = QStandardItem(str(colors[name]["variants"][0]["price"]))
        price1.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        model.setItem(i, 1, price1)
        price2 = QStandardItem(str(colors[name]["variants"][1]["price"]))
        price2.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        model.setItem(i, 2, price2)
        saving = QStandardItem(str(colors[name]["saving"]) + "%")
        saving.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        model.setItem(i, 3, saving)
    
    return model


if __name__ == "__main__":
    main()