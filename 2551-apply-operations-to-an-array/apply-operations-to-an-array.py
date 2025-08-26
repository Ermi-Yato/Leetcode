class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        output = [0]*n # we fill the array with zero and later override
        index = 0 # to control the index of the output
        for i in range(n):
            if nums[i]!=0:
                output[index] = nums[i]
                index += 1
        return output