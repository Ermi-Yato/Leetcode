class Solution:
    def isHappy(self, n: int) -> bool:
        # to track visited numbers after performing the operation
        visited = set()

        while n != 1 and n not in visited:
            # add n to the set
            visited.add(n)
            res = 0
            # extract the digits and add the square of each digit
            while n > 0:
                digit = n % 10
                res += digit**2
                n //= 10
            n = res
            res = 0
        return n == 1
        