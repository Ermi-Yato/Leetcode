class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # temp = list(s.split())[-1]
        # return len(temp)
        count = 0
        lastWord = False
        for char in reversed(s):
            if char == " " and lastWord:
                break
            if char != " ":
                lastWord = True
                count += 1
        return count
