from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # First approach 
        # char_count = Counter(s)
        # for char in t:
        #     char_count[char] -= 1
        #     if char_count[char] < 0:
        #         return False
        # return True
        
        # Second method
        return Counter(s) == Counter(t)