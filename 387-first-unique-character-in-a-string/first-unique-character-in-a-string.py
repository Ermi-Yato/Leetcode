from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        # Iterate over the characters in the string with their indices
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        return -1
        