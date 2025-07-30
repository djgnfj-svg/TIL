def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1

        a = array[i:j]
        a.sort()
        answer.append(a[k])
    print(answer)
    return answer