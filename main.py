def run_simulation(parameters: dict, args: dict, file_name: str, graph_path: str):
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from saveDataFunctions import save_data, save_ages, plot_histogram
    from utility import select_pairs

    total_data = []

    MAX_RUN = len(parameters)

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    count_old = 0
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
        sock_ages = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE, run + 1, args["hide_messages"])

        save_ages(worksheet, sock_ages, count_old + 1, 1, str(run + 1))
        worksheet.cell(row=count_old + 1, column=3, value=f"{args['type']} - "
                                                          f"{parameters[f'P{run + 1}'][args['type']]}")
        count_old += SOCK_COUNT + 2

        # Plot to matplotlib
        title = str(args["type"]) + " " + f"{parameters[f'P{run + 1}'][args['type']]:.2f}"
        bins = plot_histogram(data=list(sock_ages.values()), range_min=0, range_max=MAX_CYCLE,
                              title=title, path=graph_path, show=args["show"])

        temp = list(sock_ages.values())
        temp.sort()
        total_data.append([MAX_CYCLE, title, temp, bins])

        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + file_name + FILE_END)

        # print(f"The data of 'selecting pair' was saved to '{FILE_PATH + file_name + FILE_END}'.\n\n")

    return total_data


def main(parameters: dict = None, args: dict = None, file_name: str = "selecting_pairs", graph_path: str = "graphs"):
    from statisticFunctions import normal_dist_expected, uniform_dist_expected
    from saveDataFunctions import plot_histogram

    if args is None:
        args = {
            "plot_expected": [True, False],  # Plot the expected distribution - [NORMAL, UNIFORM] (bool)
            "type": None,  # Type of the changing parameter
            "show": False,  # Show plots in the IDE
            "hide_messages": False,
        }

    # Run the simulation to get the observed distribution
    total_data = run_simulation(parameters, args, file_name, graph_path)

    for run in total_data:
        MAX_CYCLE = run[0]
        title = run[1]
        observed = run[2]

        normal_expected = normal_dist_expected(observed, run[3])  # Get the expected normal distribution
        if args["plot_expected"][0]:
            # Plot the expected normal distribution
            plot_histogram(data=normal_expected, range_min=0, range_max=MAX_CYCLE,
                           title=title + "_normal_expected", path=graph_path, show=args["show"], custom_bins=run[3])

        uniform_expected = uniform_dist_expected(observed, run[3])  # Get the expected normal distribution
        if args["plot_expected"][1]:
            plot_histogram(data=uniform_expected, range_min=0, range_max=MAX_CYCLE,
                           title=title + "_uniform_expected", path=graph_path, show=args["show"], custom_bins=run[3])


if __name__ == '__main__':
    import os
    from time import time
    from utility import parameter_create
    os.system('cls')

    # Parameters
    save_args = {
        "plot_expected": [True, False],  # Plot the expected distribution - [NORMAL, UNIFORM] (bool)
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
    save_args["type"] = "SOCK_COUNT"
    param_sock_count = parameter_create("SOCK_COUNT", base_param_sock_count, 46, 2)  # 46
    main(args=save_args, parameters=param_sock_count, file_name="increased_sock_count", graph_path="graphs/sock_count/")
    print(f"Time for the sock count simulation: {time() - start:.2f} seconds")

    start = time()
    save_args["type"] = "USAGE_PROBABILITY"
    param_prob = parameter_create("USAGE_PROBABILITY", base_param_prob, 100, 0.01)
    main(args=save_args, parameters=param_prob, file_name="increased_usage_probability",
         graph_path="graphs/usage_probability/")
    print(f"Time for the usage probability simulation: {time() - start:.2f} seconds")
    
    start = time()
    save_args["type"] = "MAX_CYCLE"
    param_cycle = parameter_create("MAX_CYCLE", base_param_cycle, 200, 1)
    main(args=save_args, parameters=param_cycle, file_name="increased_cycle", graph_path="graphs/cycle/")
    print(f"Time for the max cycle simulation: {time() - start:.2f} seconds")
