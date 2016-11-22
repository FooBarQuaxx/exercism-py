def sum_of_multiples(n, numbers):
    multiples = [x for x in range(1, n) if any([x % num == 0 for num in numbers if num != 0])]
    return sum(multiples)
