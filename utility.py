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
