def solution(park, routes):
    answer = []
    for h, H in enumerate(park):
        for w, W in enumerate(H):
            if W == 'S':
                answer.append(h)
                answer.append(w)
    
    park_h = len(park) - 1
    park_w = len(park[0]) - 1
    
    for route in routes:
        op = route[0]
        n = int(route[-1])
        
        if op == 'N':
            temp = answer[0] - n
            if temp >= 0 and temp <= park_h and 'X' not in [park[answer[0] - i][answer[1]] for i in range(1, n + 1)]:
                    answer[0] = temp
        elif op == 'S':
            temp = answer[0] + n
            if temp >= 0 and temp <= park_h and 'X' not in [park[answer[0] + i][answer[1]] for i in range(1, n + 1)]:
                    answer[0] = temp
        elif op == 'W':            
            temp = answer[1] - n
            if temp >= 0 and temp <= park_w and 'X' not in [park[answer[0]][answer[1] - i] for i in range(1, n + 1)]:
                    answer[1] = temp
        elif op == 'E':            
            temp = answer[1] + n
            if temp >= 0 and temp <= park_w and 'X' not in [park[answer[0]][answer[1] + i] for i in range(1, n + 1)]:
                    answer[1] = temp
    
    return answer