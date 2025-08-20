# from functools import reduce
# from operator import xor
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x  = Counter(nums)
        for item in list(x.items()):
            if item[1] == 1:
                return item[0]
     
        #  return reduce(xor, nums)