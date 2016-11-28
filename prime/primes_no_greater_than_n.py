def primes_no_greater_than_value(val):
    if val <= 1:
        return []

    res = [2]
    for i in xrange(2, val + 1):
        for prime in res:
            if i % prime == 0:
                break
            if prime > i ** 0.5:
                res.append(i)
                break

    return res


def main():
    print primes_no_greater_than_value(26)
    print primes_no_greater_than_value(50)


if __name__ == '__main__':
    main()