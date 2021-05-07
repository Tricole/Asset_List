import json
import pygsheets

# authorization
gc = pygsheets.authorize(service_file='/Users/PX11/PycharmProjects/myAssetList/boreal-airway-310911-c6beb5a45ae8.json')

# open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
spreadsheet = gc.open('asset_list')

# monitors = spreadsheet.worksheet('index', 0)
# TODO: removed for in function instance of worksheet (ws_name)

column_index = {'index': 1,
                'model': 2,
                'dimension': 3,
                'location': 4,
                'condition': 5
                }
# TODO: removed for in function instance (fields)


def print_column(ws_name, fields):
    """
    A function to print out values of a specific worksheet filtered by specific properties (fields).
    :param ws_name: The name of the worksheet in question.
            The validity of the ws_name should be checked before passing into function.
    :param fields: A list of column fields to be outputted
            EX: fields = ['Index', 'Model', 'Dimension', 'Location'...'n']
            This way when you start to access multiple worksheets,
            you can just pass the right fileds list from the caller.
    """

    # Create worksheet instance:
    work_sheet = spreadsheet.worksheet(ws_name, 0)

    # Get filter type from user (desired column)
    col_name = ""
    while col_name not in fields:
        for f in range(len(fields)):
            print(f"{f}. {fields[f]}")
        col_name = input("Which field to sort by: ")

    # output to the user the data
    my_col = work_sheet.get_col(column_index[col_name], 'cell', False)
    for x in range(len(my_col)):
        # Clean user output
        print(f"{x+1}: {my_col[x].value}")

    # TODO: Add ability to isolate unwanted values


def create_log(ws_name, promts):
    """
    Get user input to create new row of data for a specific worksheet
    :param ws_name: The name of the worksheet in question.
            The validity of the ws_name should be checked before passing into function.
    :param promts: A list of prompts for the user to respond to when gather data about a new product
    """
    # Create worksheet instance and set up basic info:
    work_sheet = spreadsheet.worksheet(ws_name, 0)
    my_row = work_sheet.get_col(1, 'cell', False)
    asset_row = len(my_row) + 1

    # have to do ID cell separate from other that require user input:
    id_cell = "A" + str(asset_row)
    work_sheet.cell(id_cell).value = asset_row

    # get the rest of the user input for the fields
    cell_letters = ['B', 'C', 'D', 'E']
    count = 0
    for prompt in promts:
        user_input_field = input(f"{prompt}: ")
        field_cell = cell_letters[count] + str(asset_row)
        work_sheet.cell(field_cell).value = user_input_field


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
    # test data to be passed into create_log()
    """
    monitor_data: This data structure could be modified in many ways, and it can all be expanded in many ways
    I decided to add this so you could try and add the other worksheet name/coulms/indexes
    Here is a breakdown of the structure:
    ----worksheet name
    -------column (names)
    -------index (not sure what this was for)
    note: This would most likely be hard-coded in a seperate file in production,
          with a function to read this structure in and use it.
    """
    monitor_data = {'monitors':
                        {'columns': ['index', 'model', 'dimension', 'location', 'condition'],
                         'index': [1, 2, 3, 4, 5]
                         }
                    }

    work_sheet = monitor_data['monitors']
    f = monitor_data['monitors']['columns']
    create_log()

if __name__ == "__main__":
    main()
