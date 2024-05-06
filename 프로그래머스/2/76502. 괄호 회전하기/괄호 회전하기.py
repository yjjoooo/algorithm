def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        stack = list()
        
        for bracket in s:
            if len(stack) < 1:
                stack.append(bracket)
                continue
                
            if stack[-1] == '(' and bracket == ')':
                stack.pop()
            elif stack[-1] == '{' and bracket == '}':
                stack.pop()
            elif stack[-1] == '[' and bracket == ']':
                stack.pop()
            else:
                stack.append(bracket)
        
        if len(stack) == 0:
            answer += 1
        
        s = s[1:] + s[0]
    
    return answer

# 채점 결과
# 정확성: 28.6
# 합계: 28.6 / 100.0
# def solution(s):
#     answer = 0
    
#     for _ in range(len(s)):
#         if len(s.replace('()', '').replace('{}', '').replace('[]', '')) == 0:
#             answer += 1
        
#         s = s[1:] + s[0]
    
#     return answer