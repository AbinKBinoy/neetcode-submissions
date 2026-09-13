class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs:
                # c is a closing bracket
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                # c is an opening bracket
                stack.append(c)

        return not stack