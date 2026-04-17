class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(" : ")", "{" : "}", "[" : "]"}

        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack:
                    return False

                if ch == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
        
        