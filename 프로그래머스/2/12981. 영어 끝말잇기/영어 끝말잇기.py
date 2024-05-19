import math

def solution(n, words):
    answer = [0, 0]
    stack = [words[0]]
    
    for idx, word in enumerate(words[1:]):        
        if stack[-1][-1] != word[0] or word in stack:
            answer = [(len(stack) + 1) % n if (len(stack) + 1) % n != 0 else n, math.ceil((len(stack) + 1) / n)]
            break
        else:
            stack.append(word)
    
    return answer