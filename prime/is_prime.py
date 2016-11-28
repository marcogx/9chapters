def is_prime(n):
    if n <= 1:
        return False
    for i in xrange(2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True
