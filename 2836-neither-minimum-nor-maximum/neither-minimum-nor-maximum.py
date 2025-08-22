class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        min = nums[0]
        max = nums[-1]
        if len(nums) <= 2:
            return -1
        return nums[1]
        