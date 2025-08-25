class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        validPairs = ["()", "[]", "{}"]
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack)==0 or (stack.pop() + char) not in validPairs: 
                    return False

        return len(stack) == 0