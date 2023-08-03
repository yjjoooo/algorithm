def solution(n, s):
    if n <= 1:
        return [s]
    
    if s < n:
        return [-1]

    answer = list()
    
    element = s // n
    remainder = s % n
    
    for _ in range(n):
        answer.append(element)
        
    for i in range(1, remainder + 1):
        answer[-i] += 1
    
    return answer