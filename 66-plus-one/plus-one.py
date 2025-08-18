class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ""
        for num in digits:
            digit += str(num)
        digit = int(digit) + 1
        digit = str(digit)
        listDigit = [int(i) for i in digit]
        return listDigit