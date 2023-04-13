def wash_pairs(sock_count: int, probability_of_usage: float, max_cycle: int):
    from random import random
    from utility import re_pair

    sock_ages = dict.fromkeys(list(range(1, sock_count + 1)), 0)
    pairs = [[i, i + 1] for i in range(1, sock_count + 1, 2)]

    for cycle in range(max_cycle):
        selection = []
        for pair_idx in range(len(pairs) - 1, -1, -1):
            # Check if the pair will be used
            prob = random()
            if prob < probability_of_usage:
                selected = pairs.pop(pair_idx)  # Remove the selected pair for re-pairing
                selection += selected  # Add selected to "washing machine"

                # "Washed" socks get older
                for sock in selected:
                    sock_ages[sock] += 1

        # Pair each sock randomly again and to rest
        pairs += re_pair(selection)

    return sock_ages


def wash_singles(sock_count: int, probability_of_usage: float, max_cycle: int):
    from random import random, randint

    sock_ages = dict.fromkeys(list(range(1, sock_count + 1)), 0)

    for cycle in range(max_cycle):
        selection = []
        for sock_idx in range(1, sock_count+1):
            # Check if the sock will be used
            prob = random()
            if prob < probability_of_usage:
                selection.append(sock_idx)  # Add selected to "washing machine"

                # "Washed" socks get older
                sock_ages[sock_idx] += 1
        while len(selection) % 2 != 0:
            selected = randint(1, sock_count)
            if selected in selection:
                continue
            prob = random()
            if prob < probability_of_usage:
                selection.append(selected)  # Add selected to "washing machine"
    return sock_ages
