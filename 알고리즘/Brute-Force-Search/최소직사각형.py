def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for s in sizes:
        s.sort()
        if w < s[0]:
            w = s[0]
        if h < s[1]:
            h = s[1]           
            
    return w*h