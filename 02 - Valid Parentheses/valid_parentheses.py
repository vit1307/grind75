class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, x in enumerate(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                while len(stack) != 0:
                    tmp = stack.pop()
                    if (tmp == '(' and s[i] == ')') or (tmp == '[' and s[i] == ']') or (tmp == '{' and s[i] == '}'):
                        break
                    else:
                        return False  

        return True if len(stack) == 0 else False   
