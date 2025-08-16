from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common()[0][0]
        n = len(nums)
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1
        
            if countMap[num] > n / 2:
                return num
        return -1
            