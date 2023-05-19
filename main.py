def run_simulation(parameters: dict, args: dict, file_name: str, graph_path: str):
    from openpyxl import Workbook
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from dataSaveFunctions import save_data, save_ages, plot_histogram
    from utility import select_pairs

    total_data = dict()

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
        title = f"{parameters[f'P{run + 1}']['SOCK_COUNT']} Socks\n" \
                f"{parameters[f'P{run + 1}']['MAX_CYCLE']} Cycles\n" \
                f"{parameters[f'P{run + 1}']['USAGE_PROBABILITY']:.2f} Prob."

        observed = list(sock_ages.values())
        observed.sort()
        data = plot_histogram(observed=observed, range_min=0, range_max=MAX_CYCLE,
                              title=title, path=graph_path, show=args["show"])

        total_data[str(run)] = data

        # Save the files with the ending 'FILE_END'
        workbook.save(FILE_PATH + file_name + FILE_END)

        # print(f"The data of 'selecting pair' was saved to '{FILE_PATH + file_name + FILE_END}'.\n\n")

    return total_data


def main(parameters: dict = None, args: dict = None, file_name: str = "selecting_pairs", graph_path: str = "graphs"):
    from utility import count_interval_freq
    from dataSaveFunctions import plot_histogram
    from statisticFunctions import chi_square_test

    if args is None:
        args = {
            "type": None,  # Type of the changing parameter
            "show": False,  # Show plots in the IDE
            "hide_messages": False,
        }

    total_data = run_simulation(parameters, args, file_name, graph_path)

    for run in total_data.keys():
        [bins, observed, normal_exp, uniform_exp, title] = total_data[run]

        observed_freq = count_interval_freq(observed, bins)
        normal_freq = count_interval_freq(normal_exp, bins)
        uniform_freq = count_interval_freq(uniform_exp, bins)

        chi_normal = chi_square_test(observed_freq, normal_freq)
        chi_uniform = chi_square_test(observed_freq, uniform_freq)

        print(
            f"\n{title}\n"
            f"Normal Distribution: "
            f"statistic: {chi_normal[0]}, p: {chi_normal[1]}\n"
            f"Uniform Distribution: "
            f"statistic: {chi_uniform[0]}, p: {chi_uniform[1]}"
        )


if __name__ == '__main__':
    import os
    from time import time
    from utility import parameter_create
    os.system('cls')

    # Parameters
    save_args = {
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
        "USAGE_PROBABILITY": 0.00,
        "MAX_CYCLE": 100,
    }

    base_param_cycle = {
        "SOCK_COUNT": 50,
        "USAGE_PROBABILITY": 0.22,
        "MAX_CYCLE": 10,
    }

    start = time()
    print("Increasing SOCK COUNT")
    save_args["type"] = "SOCK_COUNT"
    param_sock_count = parameter_create("SOCK_COUNT", base_param_sock_count, 6, 20)
    main(args=save_args, parameters=param_sock_count, file_name="increased_sock_count", graph_path="graphs/sock_count/")
    print(f"Time for the sock count simulation: {time() - start:.2f} seconds\n\n")

    start = time()
    print("Increasing USAGE_PROBABILITY")
    save_args["type"] = "USAGE_PROBABILITY"
    param_prob = parameter_create("USAGE_PROBABILITY", base_param_prob, 6, 0.2)
    main(args=save_args, parameters=param_prob, file_name="increased_usage_probability",
         graph_path="graphs/usage_probability/")
    print(f"Time for the usage probability simulation: {time() - start:.2f} seconds\n\n")
    
    start = time()
    print("Increasing MAX_CYCLE")
    save_args["type"] = "MAX_CYCLE"
    param_cycle = parameter_create("MAX_CYCLE", base_param_cycle, 6, 40)
    main(args=save_args, parameters=param_cycle, file_name="increased_cycle", graph_path="graphs/cycle/")
    print(f"Time for the max cycle simulation: {time() - start:.2f} seconds\n\n")
