def save_data(ws, data: dict, start_column: int, start_row: int):
    from openpyxl import load_workbook, Workbook

    idx = 0
    for key in data.keys():
        # Save the keys to first column of the worksheet starting from the second row
        ws.cell(row=start_row + idx, column=start_column, value=key)

        # Save the values to second column of the worksheet starting from the second row
        ws.cell(row=start_row + idx, column=start_column + 1, value=data[key])

        idx += 1
