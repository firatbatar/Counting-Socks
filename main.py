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


def main(parameters: dict = None, save: dict = None, file_name: str = "selecting_pairs"):
    MAX_RUN = len(parameters)
    if save is None:
        save = {
            "is_save": True,
            "ages": True,
            "counts": False,
        }

    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from time import time
    from dataFunctions import save_data, save_ages, save_counts

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    workbook = worksheet = None
    count_old = 0
    if save["is_save"]:
        # Workbook for raw data
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Data"

    for run in range(MAX_RUN):
        # Parameters
        SOCK_COUNT = parameters[f"P{run + 1}"]["SOCK_COUNT"]
        USAGE_PROBABILITY = parameters[f"P{run + 1}"]["USAGE_PROBABILITY"]
        MAX_CYCLE = parameters[f"P{run + 1}"]["MAX_CYCLE"]
        # Get the age count for selecting pairs
        [sock_ages, age_count] = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1)

        if save["is_save"]:
            if save["ages"]:
                save_ages(worksheet, sock_ages, count_old + 1, 1, str(run + 1))
                count_old += SOCK_COUNT + 2
            elif save["counts"]:
                save_counts(worksheet, age_count, count_old + 1, 1, str(run + 1))
                count_old += len(age_count) + 2

        else:
            if save["ages"]:
                print(sock_ages)
            elif save["counts"]:
                pass


    if save["is_save"]:
        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + "selecting_pairs" + FILE_END)

        print(f"The data of 'selecting pair' was saved to '{FILE_PATH + file_name + FILE_END}'.\n\n")


if __name__ == '__main__':
    import os
    from utility import parameter_create
    os.system('cls')

    # Parameters
    base_parameters = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 100,
    }

    save_arg = {
        "is_save": True,
        "ages": True,
        "counts": False
    }

    parameters_arg = parameter_create("SOCK_COUNT", base_parameters, 3, 10)
    main(save=save_arg, parameters=parameters_arg, file_name="increased_sock_count")
