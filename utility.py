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


def parameter_create(rule: str, start: dict, size: int, step: int = 1):
    parameters = dict()
    if rule == "constant":
        for i in range(1, size + 1):
            parameters[f"P{i}"] = start.copy()
    elif rule == "SOCK_COUNT":
        if step % 2 == 1:
            step -= 1
            print(f"Sock count can't be odd increase step is changed to {step - 1}")
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["SOCK_COUNT"] += step * (i - 1)
            parameters[f"P{i}"] = new_param
    elif rule == "USAGE_PROBABILITY":
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["USAGE_PROBABILITY"] -= step * (i - 1)
            parameters[f"P{i}"] = new_param
    elif rule == "MAX_CYCLE":
        for i in range(1, size + 1):
            new_param = start.copy()
            new_param["MAX_CYCLE"] -= step * (i - 1)
            parameters[f"P{i}"] = new_param

    return parameters
