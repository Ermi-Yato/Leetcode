class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            res = 0
            for digit in str(n):
                digit = int(digit)
                res += digit * digit
            n = res
            res = 0
        return n == 1
        