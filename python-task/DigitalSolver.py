def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    print("Evens: ", evens)
    print("Odds: ", odds)
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]
