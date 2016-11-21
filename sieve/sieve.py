try:
    range = xrange
except:
    pass


def sieve(n):
    marked = set()
    primes = []
    for i in range(2, n + 1):
        if i in marked:
            continue
        primes.append(i)
        p = 2
        while True:
            x = i * p
            if x > n:
                break
            if x not in marked:
                marked.add(x)
            p += 1

    return primes
