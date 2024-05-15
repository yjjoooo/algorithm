
def solution(data, ext, val_ext, sort_by):
    answer = list()
    ext_map = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3
    }
    
    answer = [d for d in data if d[ext_map[ext]] < val_ext]
    
    answer.sort(key = lambda x : x[ext_map[sort_by]])
    
    return answer