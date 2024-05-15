# 채점 결과
# 정확성: 92.3
# 합계: 92.3 / 100.0
import math

def to_list(str):
    return [str[i:i + 2].lower() for i in range(len(str) - 1) if str[i:i + 2].isalpha()]

def solution(str1, str2):
    str1_list = to_list(str1)
    str2_list = to_list(str2)
    
    dup_list = list()
    
    for val in str1_list:
        if val in str2_list:
            dup_list.append(val)
            str2_list.remove(val)
    
    if len(str1_list) + len(str2_list) > 0:
        answer = len(dup_list) / (len(str1_list) + len(str2_list))

        return math.floor(answer * 65536)
    else:
        return 65536