class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # if nums contains only one element, return itself
        if len(nums) == 1:
            return nums
            
        element_count = Counter(nums)
        topKelements = element_count.most_common(k)
        result = []
        for elements in topKelements:
            result.append(elements[0])
        return result
