def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()

    for idx in range(len(A)):
        answer += A[idx] * B[-(idx + 1)]

    return answer