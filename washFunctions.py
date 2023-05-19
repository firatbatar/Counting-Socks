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

