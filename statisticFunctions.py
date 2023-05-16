def normal_dist_expected(observed: list, bins: list):
    import statistics
    from scipy.stats import norm
    from math import ceil

    total = len(observed)
    bounds = bins[1:-1]
    mean = statistics.mean(observed)
    stDev = statistics.stdev(observed)
    if stDev == 0:
        return observed
    r = norm(loc=mean, scale=stDev)

    expected = list()
    prob = list()

    prob.append(r.cdf(bounds[0]))
    for i in range(0, len(bounds) - 1):
        prob.append(
            r.cdf(bounds[i + 1]) - r.cdf(bounds[i])
        )
    prob.append(1 - r.cdf(bounds[-1]))

    for i in range(0, len(prob)):
        p = prob[i]
        v = (bins[i + 1] + bins[i]) / 2
        expected += [v for _ in range(ceil(total * p))]

    return expected


def uniform_dist_expected(observed: list, bins: list):
    from math import ceil

    expected = list()
    total = len(observed)
    p = max(observed) - min(observed)
    for i in range(1, len(bins)):
        width = bins[i] - bins[i - 1]
        v = (bins[i] + bins[i - 1]) / 2
        expected += [v for _ in range(ceil(total * width / p))]

    return expected