class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = [1 for _ in range(n + 1)]
        primes[0] = 0
        primes[1] = 0
        for i in range(2, ceil(sqrt(n))):
            for j in range(i**2, n + 1, i):
                primes[j] = 0
        return sum(primes) - primes[-1]