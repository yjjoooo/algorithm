# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(ingredient):
    answer = 0
    stack = list()
    
    for val in ingredient:
        stack.append(val)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
        
    return answer

# 채점 결과
# 정확성: 38.9
# 합계: 38.9 / 100.0
# def solution(ingredient):
#     answer = 0
#     ingredient_str = ''.join(list(map(lambda x : str(x), ingredient)))
    
#     while '1231' in ingredient_str:
#         ingredient_str = ingredient_str.replace('1231', '')
#         answer += 1
        
#     return answer