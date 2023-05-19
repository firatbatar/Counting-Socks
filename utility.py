def count_interval_freq(data: list, intervals: list):
    data.sort()

    n, m = len(data), len(intervals)
    count = [0] * (m - 1)

    low = 0
    ptr = 0

    while ptr < n:
        i = data[ptr]
        if intervals[low] <= i <= intervals[low + 1]:
            count[low] += 1
            ptr += 1
        elif i >= intervals[low]:
            if low == len(intervals) - 1:
                break
            low += 1

    return count


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
            if new_param["USAGE_PROBABILITY"] > 1:
                new_param["USAGE_PROBABILITY"] = 1
            new_param["USAGE_PROBABILITY"] = round(new_param["USAGE_PROBABILITY"], 2)
            parameters[f"P{i}"] = new_param

    elif rule == "MAX_CYCLE":
        step = int(step)
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["MAX_CYCLE"] += step * (i - 1)
            parameters[f"P{i}"] = new_param

    return parameters


def select_pairs(sock_count: int, usage_probability: float, max_cycle: int, run: int, hide_messages: bool = False):
    from washFunctions import wash_pairs

    # Get the age of the socks
    sock_ages = wash_pairs(sock_count, usage_probability, max_cycle)

    if not hide_messages:
        print(f"The simulation of 'selecting pair' #{run} was successfully executed!"
              f"\nIt simulated {sock_count} sock(s) with a probability of usage"
              f" {usage_probability * 100}% per pair for {max_cycle} cycle(s).\n")

    return sock_ages
