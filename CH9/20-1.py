# https://leetcode.com/problems/valid-parentheses/
# 48ms 13.9MB
class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        parenthesis = [[")", "("], ["}", "{"], ["]", "["]]
        s, stack = list(s), []
        stack.append(s.pop())
        while s:
            stack.append(s.pop())
            print(stack[-2:])
            if stack[-2:] in parenthesis:
                stack.pop()
                stack.pop()
        if len(stack) == 0:
            return True
        return False