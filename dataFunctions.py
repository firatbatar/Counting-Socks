def save_data(ws, data: dict, start_row: int, start_column: int):
    from openpyxl import load_workbook, Workbook

    idx = 0
    for key in data.keys():
        # Save the keys to first column of the worksheet starting from the second row
        ws.cell(row=start_row + idx, column=start_column, value=key)

        # Save the values to second column of the worksheet starting from the second row
        ws.cell(row=start_row + idx, column=start_column + 1, value=data[key])

        idx += 1


def save_ages(ws, data: dict, row: int, column: int, title_num: str):
    from openpyxl.worksheet.table import Table, TableStyleInfo

    # Data column titles
    ws.cell(row=row, column=column, value="Sock")
    ws.cell(row=row, column=column + 1, value="Age#" + title_num)

    # Save the data
    save_data(ws, data, row + 1, column)

    # Create the table
    tab = Table(displayName="PairsTable" + title_num, ref=f"A{row}"
                                                          f":B{row + len(data)}")
    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style  # Apply the style
    # Add table to the worksheet
    ws.add_table(tab)


def save_counts(ws, data: dict, row: int, column: int, title_num: str):
    from openpyxl.worksheet.table import Table, TableStyleInfo

    # Data column titles
    ws.cell(row=row, column=column, value="Age#" + title_num)
    ws.cell(row=row, column=column + 1, value="Count")

    # Save the data
    save_data(ws, data, row + 1, column)

    # Create the table
    tab = Table(displayName="PairsTable" + title_num, ref=f"A{row}"
                                                          f":B{row + len(data)}")
    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                           showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style  # Apply the style
    # Add table to the worksheet
    ws.add_table(tab)
