class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for key, value in enumerate(nums):
            if value in hash_table and (key - hash_table[value]) <= k:
                return True
            hash_table[value] = key
        return False




        