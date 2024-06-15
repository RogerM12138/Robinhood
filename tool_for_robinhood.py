import pandas as pd
import numpy as np

file_name = input('file_name:')
file = pd.read_csv('/Users/Roger/Desktop/'+file_name, on_bad_lines='skip').dropna(how='all')
col = list(file.columns)
trans_code_mapping = list(pd.unique(file[col[5]]))
deposit_code = ['ACH', 'DCF']

def amount_cleaning(amount):
    if amount[0] == '$':
        return amount[1:].replace(",", "")
    else:
        return '-'+amount[2:-1].replace(",", "")

file['derived_price'] = file[col[-1]].apply(amount_cleaning)
file['derived_price'] = pd.to_numeric(file['derived_price'])

gain = file['derived_price'][file['derived_price']>0].sum()
invest = file['derived_price'][file['derived_price']<0].sum()
deposit = file[file[col[5]].isin(deposit_code)]['derived_price'].sum()

print('\nbalance:', income+outcome, 'deposit:', deposit, 'gain:', gain+invest-deposit)
print('\ngain by stock:', file.groupby([col[3]])['derived_price'].sum())