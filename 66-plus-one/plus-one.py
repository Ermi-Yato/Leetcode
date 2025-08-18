class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ""
        for digit in digits:
            number_str += str(digit)

        incremented_number = int(number_str) + 1
        incremented_str = str(incremented_number)
        incremented_digits = [int(i) for i in incremented_str]

        return incremented_digits
