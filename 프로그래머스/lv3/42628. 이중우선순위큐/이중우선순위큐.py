def solution(operations):
    queue = []
    for element in operations:
        job = element.split(' ')[0]
        value = int(element.split(' ')[1])
        
        if job == 'I':
            queue.append(value)
        else:
            if len(queue) == 0:
                continue
            
            if value == 1:
                queue.remove(max(queue))
            elif value == -1:
                queue.remove(min(queue))
            else:
                print('Error')
    
    if len(queue) == 0:
        answer = [0, 0]
    else:
        answer = [max(queue), min(queue)]
    
    return answer