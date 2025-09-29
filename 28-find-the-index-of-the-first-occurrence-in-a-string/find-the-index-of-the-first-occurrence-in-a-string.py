class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # we check if needle is in haystack. return its index
        if needle in haystack:
            return haystack.index(needle)
        return -1