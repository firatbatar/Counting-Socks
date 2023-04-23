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


def main(save: bool = False, parameters: dict = None, max_run: int = 1):
    if len(parameters) != max_run:
        raise ValueError("Parameters do not match with the number of runs")

    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from time import time
    from dataFunctions import save_data

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    workbook = worksheet = None
    SOCK_COUNT_OLD = 0
    if save:
        # Workbook for raw data
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Data"

    for run in range(max_run):
        # Parameters
        SOCK_COUNT = parameters[f"P{run + 1}"]["SOCK_COUNT"]
        USAGE_PROBABILITY = parameters[f"P{run + 1}"]["USAGE_PROBABILITY"]
        MAX_CYCLE = parameters[f"P{run + 1}"]["MAX_CYCLE"]

        # Get the age count for selecting pairs
        [sock_ages, age_count] = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1)

        if save:
            # Data column titles
            worksheet.cell(row=SOCK_COUNT_OLD + 1, column=1, value="Sock")
            worksheet.cell(row=SOCK_COUNT_OLD + 1, column=2, value=f"Age#{run + 1}")

            # Save the data
            save_data(worksheet, sock_ages, 1, SOCK_COUNT_OLD + 2)

            # Create the table
            tab = Table(displayName=f"PairsTable{run + 1}", ref=f"A{SOCK_COUNT_OLD + 1}"
                                                                f":B{SOCK_COUNT_OLD + SOCK_COUNT + 1}")
            # Add a default style with striped rows and banded columns
            style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                   showLastColumn=False, showRowStripes=True, showColumnStripes=True)
            tab.tableStyleInfo = style  # Apply the style
            # Add table to the worksheet
            worksheet.add_table(tab)

        else:
            print(sock_ages)

        SOCK_COUNT_OLD += SOCK_COUNT + 2

    if save:
        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + "selecting_pairs" + FILE_END)

        print(f"The data of 'selecting pair' was saved to '{FILE_PATH}selecting_pairs{FILE_END}'.\n\n")


if __name__ == '__main__':
    import os
    os.system('cls')

    # Parameters
    parameters = {
        "P1": {
            "SOCK_COUNT": 50,
            "USAGE_PROBABILITY": 0.2,
            "MAX_CYCLE": 100,
        },
        "P2": {
            "SOCK_COUNT": 60,
            "USAGE_PROBABILITY": 0.2,
            "MAX_CYCLE": 100,
        },
        "P3": {
            "SOCK_COUNT": 50,
            "USAGE_PROBABILITY": 0.2,
            "MAX_CYCLE": 100,
        }
    }

    main(save=True, parameters=parameters, max_run=3)
