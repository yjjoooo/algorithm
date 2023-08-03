def solution(triangle):
    for h in range(1, len(triangle)):
        for w in range(len(triangle[h])):
            if w == 0:
                triangle[h][w] += triangle[h - 1][w]
            elif w == h:
                triangle[h][w] += triangle[h - 1][w - 1]
            else:
                value = max([triangle[h - 1][w - 1], triangle[h - 1][w]])
                triangle[h][w] += value
    
    answer = max(triangle[-1])
    
    return answer