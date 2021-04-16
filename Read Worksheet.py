from openpyxl import load_workbook

workbook = load_workbook(filename="asset_list.xlsx")

sheet= workbook.active


sheet["F1"] ="test"

workbook.save(filename="changed workbook.xlsx")
