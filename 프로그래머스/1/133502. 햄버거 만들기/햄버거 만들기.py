def solution(ingredient):
    answer = 0
    stack = list()
    
    for idx, val in enumerate(ingredient):
        stack.append(val)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
        
    return answer

# def solution(ingredient):
#     answer = 0
#     ingredient_str = ''.join(list(map(lambda x : str(x), ingredient)))
    
#     while True:
#         if '1231' in ingredient_str:
#             ingredient_str = ingredient_str.replace('1231', '')
#             answer += 1
#         else:
#             break
        
#     return answer