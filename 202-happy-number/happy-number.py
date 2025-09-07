class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            res = 0
            while n > 0:
                digit = n % 10
                res += digit**2
                n //= 10
            n = res
            res = 0
        return n == 1
        