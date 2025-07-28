def solution(clothes):
    answer = 1
    a = {}
    for c in clothes:
        a[c[1]] = a.get(c[1],1) + 1  
    for b in a.values():
        answer *= b
    return answer - 1