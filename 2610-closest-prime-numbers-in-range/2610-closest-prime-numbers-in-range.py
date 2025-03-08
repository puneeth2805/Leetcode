class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = max(right, 2)  
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False 

        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        primes = [num for num in range(left, right + 1) if is_prime[num]]
        if len(primes)<2:
            return [-1,-1]
        
        min_gap=float('inf')
        result=[-1,-1]
        for i in range(1,len(primes)):
            gap=primes[i]-primes[i-1]
            if gap<min_gap:
                min_gap=gap
                result=[primes[i-1],primes[i]]
        return result
                    