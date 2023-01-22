class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve_of_num(n):
            primes = [True] * (n+1)
            primes[0] = primes[1] = False
            for i in range(2, int(n**0.5) + 1):
                if primes[i]:
                    for j in range(i*i, n+1, i):
                        primes[j] = False
            return primes
        
        primes = sieve_of_num(right)
        min_diff = float('inf')
        ans = [-1, -1]
        for i in range(left, right+1):
            if primes[i]:
                for j in range(i+1, right+1):
                    if primes[j]:
                        diff = j - i
                        if diff < min_diff:
                            min_diff = diff
                            ans = [i, j]
                        break
        return ans if min_diff != float('inf') else [-1, -1]