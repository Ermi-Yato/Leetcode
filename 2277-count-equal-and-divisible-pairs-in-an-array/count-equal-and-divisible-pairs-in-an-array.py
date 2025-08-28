class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        indicesGroup = defaultdict(list)
        for i, num in enumerate(nums):
            indicesGroup[num].append(i)

        for indices in indicesGroup.values():
            for i in range(len(indices)):
                for j in range(i+1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count