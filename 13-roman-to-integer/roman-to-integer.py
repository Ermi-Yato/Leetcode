class Solution:
    def romanToInt(self, s: str) -> int:
        roman_Integer = {
        'I': 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
        integerValue = 0
        for i, j in zip(s, s[1:]):
            if roman_Integer[i] < roman_Integer[j]:
                integerValue -= roman_Integer[i]
            else:
                integerValue += roman_Integer[i]

        return integerValue + roman_Integer[s[-1]]


        