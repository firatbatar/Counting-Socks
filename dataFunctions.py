def save_data(ws, data: list, start_column: int, start_row: int):
    from openpyxl import load_workbook, Workbook

    idx = 0
    for idx in range(len(data)):
        ws.cell(row=start_row + idx, column=start_column, value=data[idx])


def convert_to_column(idx: int):
    idx -= 1
    column = ""
    while idx > 25:
        rem = idx % 26

        column = chr(65 + rem) + column
        idx = (idx // 26) - 1

    column = chr(65 + idx) + column

    return column
