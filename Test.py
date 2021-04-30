import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='/Users/PX11/PycharmProjects/myAssetList/boreal-airway-310911-c6beb5a45ae8.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('asset_list')

#select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(1,1))