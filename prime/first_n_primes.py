def first_n_primes(n):
    if n <= 1:
        return [2]

    res = [2]
    for i in xrange(2, n ** 2):
        for prime in res:
            if i % prime == 0:
                break
            if prime > i ** 0.5:
                res.append(i)
                break
        if len(res) == n:
            return res

    if len(res) < n:
        return first_n_primes(2 * n)


def main():
    print first_n_primes(26)


if __name__ == '__main__':
    main()