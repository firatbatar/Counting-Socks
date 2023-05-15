def main(parameters: dict = None, save: dict = None, file_name: str = "selecting_pairs", graph_path: str = "graphs"):
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from saveDataFunctions import save_data, save_ages, plot_histogram
    from utility import select_pairs

    MAX_RUN = len(parameters)
    if save is None:
        save = {
            "is_save": True,  # Save to excel
            "type": None,  # Type of the changing parameter
            "show": False  # Show plots in the IDE
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
        # Get the age count for selecting pairs
        sock_ages = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1, save["hide_messages"])

        if save["is_save"]:
            save_ages(worksheet, sock_ages, count_old + 1, 1, str(run + 1))
            worksheet.cell(row=count_old + 1, column=3, value=f"{args['type']} - "
                                                              f"{parameters[f'P{run + 1}'][args['type']]}")
            count_old += SOCK_COUNT + 2

        else:
            print(sock_ages)

        # Plot to matplotlib
        title = str(save["type"]) + " " + f"{parameters[f'P{run + 1}'][save['type']]:.2f}"
        plot_histogram(data=list(sock_ages.values()), range_min=0, range_max=MAX_CYCLE,
                       title=title, path=graph_path, show=args["show"])

    if save["is_save"]:
        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + file_name + FILE_END)

        # print(f"The data of 'selecting pair' was saved to '{FILE_PATH + file_name + FILE_END}'.\n\n")


if __name__ == '__main__':
    import os
    from time import time
    from utility import parameter_create
    os.system('cls')

    # Parameters
    args = {
        "is_save": True,  # Save to excel - bool
        "type": None,  # Type of the changing parameter (just for naming) - str
        "show": False,  # Show plots in the IDE - bool
        "hide_messages": True
    }

    base_param_sock_count = {
        "SOCK_COUNT": 10,
        "USAGE_PROBABILITY": 0.22,
        "MAX_CYCLE": 100,
    }

    base_param_prob = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.01,
        "MAX_CYCLE": 100,
    }

    base_param_cycle = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.22,
        "MAX_CYCLE": 10,
    }

    start = time()
    args["type"] = "SOCK_COUNT"
    param_sock_count = parameter_create("SOCK_COUNT", base_param_sock_count, 46, 2)
    main(save=args, parameters=param_sock_count, file_name="increased_sock_count", graph_path="graphs/sock_count/")
    print(f"Time for the first simulation: {time() - start:.2f} seconds")

    start = time()
    args["type"] = "USAGE_PROBABILITY"
    param_prob = parameter_create("USAGE_PROBABILITY", base_param_prob, 100, 0.01)
    main(save=args, parameters=param_prob, file_name="increased_usage_probability",
         graph_path="graphs/usage_probability/")
    print(f"Time for the second simulation: {time() - start:.2f} seconds")

    start = time()
    args["type"] = "MAX_CYCLE"
    param_cycle = parameter_create("MAX_CYCLE", base_param_cycle, 200, 1)
    main(save=args, parameters=param_cycle, file_name="increased_cycle", graph_path="graphs/cycle/")
    print(f"Time for the third simulation: {time() - start:.2f} seconds")
