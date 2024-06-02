def solution(survey, choices):
    answer_dict = {
        'RT' : 0,
        'CF' : 0,
        'JM' : 0,
        'AN' : 0
    }
    
    for idx, s in enumerate(survey):
        if s[0] in ['R', 'C', 'J', 'A']:
            answer_dict[s] += (choices[idx] - 4)
        else:
            answer_dict[s[::-1]] -= (choices[idx] - 4)
     
    answer = ''.join([key[0] if val <= 0 else key[1] for key, val in answer_dict.items()])
    
    return answer