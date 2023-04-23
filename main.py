def select_pairs(sock_count: int, usage_probability: float, max_cycle: int, run: int):
    from time import time
    from washFunctions import wash_pairs
    from utility import count_values

    start_time = time()

    # Get the age of the socks
    sock_ages = wash_pairs(sock_count, usage_probability, max_cycle)

    # Convert it to number of socks with a certain age
    age_count = count_values(sock_ages)

    print(f"The simulation of 'selecting pair'#{run} was successfully executed in {time() - start_time:.3f} seconds!"
          f"\nIt simulated {sock_count} sock(s) with a probability of usage"
          f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).")

    return [sock_ages, age_count]


def select_singles(sock_count: int, usage_probability: float, max_cycle: int, run: int):
    from time import time
    from washFunctions import wash_singles
    from utility import count_values

    start_time = time()

    # Get the age of the socks
    sock_ages = wash_singles(sock_count, usage_probability, max_cycle)

    # Convert it to number of socks with a certain age
    age_count = count_values(sock_ages)

    print(f"The simulation of 'selecting singles'#{run} was successfully executed in {time() - start_time:.3f} seconds!"
          f"\nIt simulated {sock_count} sock(s) with a probability of usage"
          f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).")

    return [sock_ages, age_count]


def main(pairs: bool = True, singles: bool = False, save: bool = False, parameters: dict = None, max_run: int = 1):
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from dataFunctions import save_data, convert_to_column

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    # Parameters
    if parameters is None:
        # Parameters as inputs
        SOCK_COUNT = int(input("Enter total number of pairs: ")) * 2
        if SOCK_COUNT <= 0:
            print("Invalid input")
            return
        USAGE_PROBABILITY = float(input("Enter the usage probability of a pair (between 0 and 1): "))
        if not (0 <= USAGE_PROBABILITY < 1):
            print("Invalid input")
            return
        MAX_CYCLE = int(input("Enter total number of cycles: "))
        if MAX_CYCLE <= 0:
            print("Invalid input")
            return
    else:
        # Predefined parameters
        SOCK_COUNT = parameters["SOCK_COUNT"]
        USAGE_PROBABILITY = parameters["USAGE_PROBABILITY"]
        MAX_CYCLE = parameters["MAX_CYCLE"]

    workbook = worksheet = None
    if pairs:
        if save:
            # Workbook for raw data
            workbook = Workbook()
            worksheet = workbook.active
            worksheet.title = "Data"
            worksheet.cell(row=1, column=1, value="Sock")
            save_data(worksheet, [i for i in range(1, SOCK_COUNT + 1)], 1, 2)

        for run in range(max_run):
            # Get the age count for selecting pairs
            [sock_ages, age_count] = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1)

            if save:
                # Data column titles
                worksheet.cell(row=1, column=run + 2, value=f"Ages#{run + 1}")

                # Save the data
                save_data(worksheet, list(sock_ages.values()), run + 2, 2)
            else:
                print(sock_ages)

        if save:
            # Create the table
            tab = Table(displayName="PairsTable", ref=f"A1:{convert_to_column(max_run + 1)}{SOCK_COUNT + 1}")

            # Add a default style with striped rows and banded columns
            style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                   showLastColumn=False, showRowStripes=True, showColumnStripes=True)
            tab.tableStyleInfo = style  # Apply the style

            # Add table to the worksheet
            worksheet.add_table(tab)
            # Save the files with the ending 'FILE_END'
            workbook.save(FILE_PATH + "selecting_pairs" + FILE_END)

            print(f"The data of 'selecting pair' was saved to '{FILE_PATH}selecting_pairs{FILE_END}'.\n\n")

    if singles:
        if save:
            # Workbook for raw data
            workbook = Workbook()
            worksheet = workbook.active
            worksheet.title = "Data"
            worksheet.cell(row=1, column=1, value="Sock")
            save_data(worksheet, [i for i in range(1, SOCK_COUNT + 1)], 1, 2)

        for run in range(max_run):
            # Get the age count for selecting pairs
            [sock_ages, age_count] = select_singles(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1)

            if save:
                # Data column titles
                worksheet.cell(row=1, column=2, value="Age")

                # Save the data
                save_data(worksheet, list(sock_ages.values()), run + 2, 2)
            else:
                print(sock_ages)

        if save:
            # Create the table
            tab = Table(displayName="PairsTable", ref=f"A1:{convert_to_column(max_run + 1)}{SOCK_COUNT + 1}")

            # Add a default style with striped rows and banded columns
            style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                   showLastColumn=False, showRowStripes=True, showColumnStripes=True)
            tab.tableStyleInfo = style  # Apply the style

            # Add table to the worksheet
            worksheet.add_table(tab)

            # Save the files with the ending 'FILE_END'
            workbook.save(FILE_PATH + "selecting_singles" + FILE_END)

            print(f"The data of 'selecting singles' was saved to '{FILE_PATH}selecting_singles{FILE_END}'.\n\n")


if __name__ == '__main__':
    import os
    os.system('cls')

    # Parameters
    parameters = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 100,
    }

    main(pairs=True, singles=False, save=True, parameters=parameters)
