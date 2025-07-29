def solution(priorities, location):
    answer = 0
    temp_p = []
    for i, p in enumerate(priorities):
        temp_p.append([p, i])

    count = 1
    while True:
        o = False
        a = temp_p.pop(0)
        for i, tp in enumerate(temp_p):
            if a[0] < tp[0]:
                temp_p.append(a)
                o = True
                break
        if o:
            continue
        else:
            if a[1] == location:
                return count
            count += 1  
            # 여기서 현재값을 내보내는방법
    return answer