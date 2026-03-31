class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "({["
        close = ")}]"

        for c in s:
            if c in open:
                stack.append(c)
            elif c in close:
                if len(stack) != 0:
                    b = stack.pop(len(stack) - 1)
                    if c == ')' and b != '(':
                        return False
                    elif c == ']' and b != '[':
                        return False
                    elif c == '}' and b != '{':
                        return False
                else:
                    return False
        
        return len(stack) == 0