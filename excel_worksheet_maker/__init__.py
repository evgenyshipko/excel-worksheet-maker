from xlsxwriter import Workbook


def write_workbook(column_data_list, row_data_list, file_path):

    workbook = Workbook(file_path)
    worksheet = workbook.add_worksheet()

    row_index = 0
    for i in range(len(column_data_list)):
        worksheet.write(row_index, i, column_data_list[i].get('name'))

    for row_data in row_data_list:
        row_index = row_index + 1
        for i in range(len(column_data_list)):
            column_id_list = column_data_list[i]['id']
            value = ""
            for column_id in column_id_list:
                key_value = row_data.get(column_id)
                if key_value is not None and key_value != []:
                    value += str(key_value) + ' '

            worksheet.write(row_index, i, value)

    workbook.close()
    return workbook


def test_func():
    print("is_test")