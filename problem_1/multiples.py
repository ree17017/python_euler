def multiples_of_3_or_5(number) -> int:
    """sum of all the multiples of 3 or 5 below a given number."""
    sums = []
    i = number - 1

    while i > 0:
        if i % 3 == 0:
            sums.append(i)
        i = i - 1

    i = number - 1
    while i > 0:
        if i % 5 == 0:
            sums.append(i)
        i = i - 1

    total = 0
    for sum_in in sums:
        total = total + sum_in

    return total
