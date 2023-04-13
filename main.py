def select_pairs(sock_count, usage_probability, max_cycle):
    from time import time
    from washFunctions import wash_pairs
    from utility import count_values

    start_time = time()

    # Get the age of the socks
    sock_ages = wash_pairs(sock_count, usage_probability, max_cycle)

    # Convert it to number of socks with a certain age
    age_count = count_values(sock_ages)

    print(f"The simulation of 'selecting pair' was successfully executed in {time() - start_time:.3f} seconds!"
          f"\nIt simulated {sock_count} sock(s) with a probability of usage"
          f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).")

    return age_count


def select_singles(sock_count, usage_probability, max_cycle):
    from time import time
    from washFunctions import wash_singles
    from utility import count_values

    start_time = time()

    # Get the age of the socks
    sock_ages = wash_singles(sock_count, usage_probability, max_cycle)

    # Convert it to number of socks with a certain age
    age_count = count_values(sock_ages)

    print(f"The simulation of 'selecting singles' was successfully executed in {time() - start_time:.3f} seconds!"
          f"\nIt simulated {sock_count} sock(s) with a probability of usage"
          f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).")

    return age_count


def main(pairs=True, singles=True, save=False, parameters=None):
    from openpyxl import Workbook
    from time import time
    from dataFunctions import save_data

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    # Parameters as inputs
    if parameters is None:
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

    if pairs:
        # Get the age count for selecting pairs
        age_count = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE)

        if save:
            # Save the data
            # Workbook for raw data
            workbook = Workbook()
            worksheet = workbook.active
            worksheet.title = "Data"

            # Data column titles
            worksheet.cell(row=1, column=1, value="Age")
            worksheet.cell(row=1, column=2, value="Number of Socks")

            # Save the data
            save_data(worksheet, age_count, 1, 2)

            # Save the files with the ending 'FILE_END'
            workbook.save(FILE_PATH + "selecting_pairs" + FILE_END)

            print(f"The data of 'selecting pair' was saved to '{FILE_PATH}selecting_pairs{FILE_END}'.\n\n")
        else:
            print(age_count)

    if singles:
        # Get the age count for selecting pairs
        age_count = select_singles(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE)

        if save:
            # Save the data
            # Workbook for raw data
            workbook = Workbook()
            worksheet = workbook.active
            worksheet.title = "Data"

            # Data column titles
            worksheet.cell(row=1, column=1, value="Age")
            worksheet.cell(row=1, column=2, value="Number of Socks")

            # Save the data
            save_data(worksheet, age_count, 1, 2)

            # Save the files with the ending 'FILE_END'
            workbook.save(FILE_PATH + "selecting_singles" + FILE_END)

            print(f"The data of 'selecting singles' was saved to '{FILE_PATH}selecting_singles{FILE_END}'.\n\n")
        else:
            print(age_count)


if __name__ == '__main__':
    import os
    os.system('cls')

    # Parameters
    parameters = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 100,
    }
    main(pairs=True, singles=True, save=True, parameters=parameters)
