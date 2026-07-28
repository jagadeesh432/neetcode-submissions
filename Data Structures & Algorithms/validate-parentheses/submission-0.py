class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { ")" : "(", "}" : "{", "]" : "[" }
        
        for each in s:
            if each in brackets:
                if stack and stack[-1] == brackets[each]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(each)
        
        return True if not stack else False
            