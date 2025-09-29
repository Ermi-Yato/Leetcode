class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = list(s.split())[-1]
        return len(temp)
