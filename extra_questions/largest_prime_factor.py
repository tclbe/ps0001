# What is the largest prime factor of 600851475143?

n = 600851475143

primes = [2]
curr_prime = primes[-1]


def next_prime(primes: list):
    n = primes[-1]
    if n == 2:
        primes.append(3)
        return 3

    n += 2

    while True:
        for p in primes:
            if n % p == 0:
                # if n is divisible by p, it is not prime (by definition)
                n += 2
                break
            if p > n**0.5:
                # if p > sqrt(n), then it is prime,
                # because we checked all possible prime factors smaller than p already.
                primes.append(n)
                return n
        else:
            primes.append(n)
            return n


# Ensure that it works as expected
print(next_prime(primes))
print(next_prime(primes))
print(next_prime(primes))
print(next_prime(primes))
print(next_prime(primes))

primes = [2]
curr_prime = primes[-1]

while n > curr_prime:
    if n % curr_prime == 0:
        n //= curr_prime
        print(f"{n * curr_prime} / {curr_prime} = {n}")
    else:
        curr_prime = next_prime(primes)
