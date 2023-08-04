def solution(s):
    s = [int(x) for x in s.split(' ')]
    answer = '{} {}'.format(min(s), max(s))
    return answer