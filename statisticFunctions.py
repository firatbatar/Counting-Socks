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

    expected.sort()
    expected_mean = statistics.mean(expected)
    while len(observed) > len(expected):
        expected.append(expected_mean)

    i = j = -1
    while len(observed) < len(expected):
        j *= -1
        expected.pop(i + j)

    return expected


def uniform_dist_expected(observed: list, bins: list):
    import statistics
    from math import ceil

    expected = list()
    total = len(observed)
    if max(observed) - min(observed) == 0:
        return observed.copy()

    interval_count = len(bins) - 1
    count = total / interval_count
    for i in range(1, len(bins)):
        v = (bins[i] + bins[i - 1]) / 2
        expected += [v for _ in range(round(count))]

    expected.sort()
    expected_mean = statistics.mean(expected)
    while len(observed) > len(expected):
        expected.append(expected_mean)

    i = j = -1
    while len(observed) < len(expected):
        j *= -1
        expected.pop(i + j)

    return expected


def chi_square_test(observed_freq: list, expected_freq: list):
    from scipy.stats import chisquare
    from numpy import seterr
    seterr(divide="ignore", invalid="ignore")

    chi = chisquare(f_obs=observed_freq, f_exp=expected_freq)

    return chi
