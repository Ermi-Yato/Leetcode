from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        frequentItem = count.most_common()
        return frequentItem[0][0]