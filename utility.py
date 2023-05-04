def re_pair(socks: list):
    from random import randint

    pairs = []

    for _ in range(len(socks)//2):
        idx1 = randint(0, len(socks) - 1)
        sock1 = socks.pop(idx1)

        idx2 = randint(0, len(socks) - 1)
        sock2 = socks.pop(idx2)

        pairs.append([sock1, sock2])

    return pairs


def count_values(dictionary: dict):
    new_dict = dict()
    for value in dictionary.values():
        if value in new_dict:
            new_dict[value] += 1
        else:
            new_dict[value] = 1

    return new_dict


def parameter_create(rule: str, start: dict, size: int, step: float = 1):
    parameters = dict()
    if rule == "constant":
        for i in range(1, size + 1):
            parameters[f"P{i}"] = start.copy()

    elif rule == "SOCK_COUNT":
        step = int(step)
        if step % 2 == 1:
            step -= 1
            print(f"Sock count can't be odd, increase step is changed to {step - 1}")
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["SOCK_COUNT"] += step * (i - 1)
            parameters[f"P{i}"] = new_param

    elif rule == "USAGE_PROBABILITY":
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["USAGE_PROBABILITY"] += step * (i - 1)
            parameters[f"P{i}"] = new_param

    elif rule == "MAX_CYCLE":
        step = int(step)
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["MAX_CYCLE"] += step * (i - 1)
            parameters[f"P{i}"] = new_param

    return parameters


def select_pairs(sock_count: int, usage_probability: float, max_cycle: int, run: int):
    from time import time
    from washFunctions import wash_pairs

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

    start_time = time()

    # Get the age of the socks
    sock_ages = wash_singles(sock_count, usage_probability, max_cycle)

    # Convert it to number of socks with a certain age
    age_count = count_values(sock_ages)

    print(f"The simulation of 'selecting singles'#{run} was successfully executed in {time() - start_time:.3f} seconds!"
          f"\nIt simulated {sock_count} sock(s) with a probability of usage"
          f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).")

    return [sock_ages, age_count]
