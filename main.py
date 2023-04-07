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


def main(pairs=True, singles=True):
    from openpyxl import Workbook
    from time import time
    from dataFunctions import save_data

    # File constants
    FILE_PATH = "data/"
    FILE_END = "-raw_data.xlsx"

    # Parameters
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

    if pairs:
        # Get the age count for selecting pairs
        age_count = select_pairs(SOCK_COUNT, USAGE_PROBABILITY, MAX_CYCLE)

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

        print(f"\nThe data of 'selecting pair' was saved to '{FILE_PATH}selecting_pairs{FILE_END}'.")

    if singles:
        pass


if __name__ == '__main__':
    main(singles=False)
