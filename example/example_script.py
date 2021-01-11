import os
# define path to the file
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import excel_worksheet_maker

print('test script: start')

file_name = 'test.xlsx'
file_path = os.path.abspath(file_name)
print('file_path',file_path)

# define column list of dicts
column_dict_list = [
    {'id': ['isummary', 'type'], 'name': 'Название'},
    {'id': ['status'], 'name': 'Статус'},
    {'id': ['quantity'], 'name': 'Количество'},
    ]

# define data list of dicts
data_dict_list = [
    {'isummary': 'tool 1', 'type': 'manual', 'status': 'repaired', 'quantity': '5'},
    {'isummary': 'tool 2', 'type': 'mechanical', 'status': 'broken', 'quantity': '2'},
    {'isummary': 'tool 3', 'type': 'electro', 'status': 'cool', 'quantity': '6'},
]

# call function and see file in example directory
excel_worksheet_maker.write_workbook(column_dict_list, data_dict_list, file_path)
print('test script: completed')
# write_workbook gets data by id from data_dict_list , concatenates it and write into column with column_dict_list.name
