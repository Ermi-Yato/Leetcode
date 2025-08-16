from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common()[0][0]
        n = len(nums)
        countMap = defaultdict(int)

    # Traverse the list and count occurrences using the hash map
        for num in nums:
            countMap[num] += 1
        
        # Check if current element count exceeds n / 2
            if countMap[num] > n / 2:
                return num

        # If no majority element is found, return -1
        return -1
            