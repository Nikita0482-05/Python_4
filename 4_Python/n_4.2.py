def prime_numbers():
    num = 2
    while True:
        is_prime = True
        for divider in range(2, int(num ** 0.5) + 1):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

print("Простые числа:")
primes = prime_numbers()
for _ in range(10):
    print(next(primes))