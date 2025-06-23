class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashTable = {}
        result = majority = 0
        
        for n in nums:
            hashTable[n] = 1 + hashTable.get(n, 0)
            if hashTable[n] > majority:
                result = n
                majority = hashTable[n]
        
        return result