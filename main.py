def main(parameters: dict = None, save: dict = None, file_name: str = "selecting_pairs", graph_path: str = "graphs"):
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from time import time
    from dataFunctions import save_data, save_ages, save_counts, plot_histogram
    from utility import select_pairs

    MAX_RUN = len(parameters)
    if save is None:
        save = {
            "is_save": True,
            "ages": True,
            "counts": False,
        }

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
        BIN_WIDTH = parameters[f"P{run + 1}"]["BIN_WIDTH"]
        # Get the age count for selecting pairs
        [sock_ages, age_count] = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1)

        if save["is_save"]:
            if save["ages"]:
                save_ages(worksheet, sock_ages, count_old + 1, 1, str(run + 1))
                worksheet.cell(row=count_old + 1, column=3, value=f"{save_arg['type']} - "
                                                                  f"{parameters[f'P{run + 1}'][save_arg['type']]}")
                count_old += SOCK_COUNT + 2
            elif save["counts"]:
                save_counts(worksheet, age_count, count_old + 1, 1, str(run + 1))
                worksheet.cell(row=count_old + 1, column=3, value=f"{save_arg['type']} - "
                                                                  f"{parameters[f'P{run + 1}'][save_arg['type']]}")
                count_old += len(age_count) + 2

        else:
            if save["ages"]:
                print(sock_ages)
            elif save["counts"]:
                pass

        # Plot to matplotlib
        title = str(save["type"]) + " " + f"{parameters[f'P{run + 1}'][save['type']]:.2f}"
        bin_count = MAX_CYCLE // BIN_WIDTH
        plot_histogram(data=list(sock_ages.values()), bin_count=bin_count, range_min=0, range_max=MAX_CYCLE,
                       title=title, path=graph_path, show=save_arg["show"])

    if save["is_save"]:
        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + file_name + FILE_END)

        # print(f"The data of 'selecting pair' was saved to '{FILE_PATH + file_name + FILE_END}'.\n\n")


if __name__ == '__main__':
    import os
    from utility import parameter_create
    os.system('cls')

    # Parameters
    save_arg = {
        "is_save": True,
        "ages": True,
        "counts": False,
        "type": None,
        "show": False
    }

    base_param_sock_count = {
        "SOCK_COUNT": 10,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 50,
        "BIN_WIDTH": 10
    }

    base_param_prob = {
        "SOCK_COUNT": 10,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 50,
        "BIN_WIDTH": 5
    }

    base_param_cycle = {
        "SOCK_COUNT": 30,
        "USAGE_PROBABILITY": 0.2,
        "MAX_CYCLE": 10,
        "BIN_WIDTH": 5
    }

    save_arg["type"] = "SOCK_COUNT"
    param_sock_count = parameter_create("SOCK_COUNT", base_param_sock_count, 11, 4)
    main(save=save_arg, parameters=param_sock_count, file_name="increased_sock_count", graph_path="graphs/sock_count/")

    save_arg["type"] = "USAGE_PROBABILITY"
    param_prob = parameter_create("USAGE_PROBABILITY", base_param_prob, 10, 0.05)
    main(save=save_arg, parameters=param_prob, file_name="increased_usage_probability",
         graph_path="graphs/usage_probability/")

    save_arg["type"] = "MAX_CYCLE"
    param_cycle = parameter_create("MAX_CYCLE", base_param_cycle, 10, 10)
    main(save=save_arg, parameters=param_cycle, file_name="increased_cycle", graph_path="graphs/cycle/")
