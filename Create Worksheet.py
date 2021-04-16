
from openpyxl import Workbook

filename = "asset_list.xlsx"

workbook = Workbook()
sheet = workbook.active

workbook.save(filename=filename)