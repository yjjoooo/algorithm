def solution(s):
    stack = list()
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            else:
                bracket = stack.pop()
                if bracket == ')':
                    return False
    
    if len(stack) > 0:
        return False
    else:
        return True
