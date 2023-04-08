def primes(left, right):
    left = left if left != 1 else 2
    for n in range(left, right + 1):
        if all(n % i != 0 for i in range(2, n // 2 + 1)):
            yield n

generator = primes(1, 15)

print(*generator)
# 2 3 5 7 11 13

generator = primes(6, 36)

print(next(generator))
print(next(generator))
# 7
# 11