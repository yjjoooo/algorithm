import re

def solution(babbling):
    babbles = ['aya', 'ye', 'woo', 'ma']
    answer_list = list()
    
    for babble in babbling:
        result = True
        for b in babbles:
            if b + b in babble:
                result = False
                break
        
        if result:
            babble = re.sub('|'.join(babbles), '', babble)
        
        answer_list.append(babble)
        
    return len([val for val in answer_list if val == ''])

# 채점 결과
# 정확성: 60.0
# 합계: 60.0 / 100.0
# def solution(babbling):
#     babbles = ['aya', 'ye', 'woo', 'ma']
#     answer_list = list()
    
#     for babble in babbling:
#         result = True
#         for b in babbles:
#             if b + b in babble:
#                 result = False
#                 break
        
#         if result:
#             for b in babbles:
#                 babble = babble.replace(b, '')
        
#         answer_list.append(babble)
        
#     return len([val for val in answer_list if val == ''])

# 채점 결과
# 정확성: 55.0
# 합계: 55.0 / 100.0
# def solution(babbling):
#     babbles = ['aya', 'ye', 'woo', 'ma']
#     answer_list = list()
    
#     for babble in babbling:
#         for b in babbles:
#             if b + b not in babble:
#                 babble = babble.replace(b, '')
        
#         answer_list.append(babble)
    
#     return len([val for val in answer_list if val == ''])