import json
import pygsheets

# authorization
gc = pygsheets.authorize(service_file='/Users/PX11/PycharmProjects/myAssetList/boreal-airway-310911-c6beb5a45ae8.json')

# open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
spreadsheet = gc.open('asset_list')

# from openpyxl import load_workbook

# workbook = load_workbook(filename="asset_list.xlsx")

# sheet = workbook.active
# sheet.title = "Monitors"

monitors = spreadsheet.worksheet('index', 0)

column_index = {'index': 1,
                'model': 2,
                'dimension': 3,
                'location': 4,
                'condition': 5
                }


# print column
def print_column():
    col_name = input("What would you like to retrieve?\n"
                     "1. Index\n"
                     "2. Model\n"
                     "3. Dimension\n"
                     "4. Location\n"
                     "5. Condition\n")

    # add user input validation
    my_col = monitors.get_col(column_index[col_name], 'cell', False)
    for x in range(len(my_col)):
        print(my_col[x].value)


# create a new entry
def create_log():
    my_row = monitors.get_col(1, 'cell', False)
    asset_row = len(my_row) + 1
    print("Please provide details of monitor below")
    model = input("Model: ")
    dimension = int(input("Dimension: "))
    location = input("Location: ")
    condition = input("Condition: ")

    id_cell = "A" + str(asset_row)
    model_cell = "B" + str(asset_row)
    dimension_cell = "C" + str(asset_row)
    location_cell = "D" + str(asset_row)
    condition_cell = "E" + str(asset_row)

    monitors.cell(id_cell).value = asset_row
    monitors.cell(model_cell).value = model
    monitors.cell(dimension_cell).value = dimension
    monitors.cell(location_cell).value = location
    monitors.cell(condition_cell).value = condition

    return


def read_log(my_row):
    products = {}
    for row in sheet.iter_rows(min_row=my_row,
                               max_row=my_row,
                               values_only=True):
        product_id = row[0]
        product = {
            "model": row[1],
            "dimension": row[2],
            "location": row[3],
            "condition": row[4]
        }
        products[product_id] = product

    print(json.dumps(products))


def get_new():
    pass


def summary():
    pass


def remove():
    pass


def get_number():
    return len(sheet["A"])


def print_rows():
    for row in sheet.iter_rows(values_only=True):
        print(row)


def main():
    create_log()
    # read_log(5)


if __name__ == "__main__":
    main()
