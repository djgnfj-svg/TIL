def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0])
    t = arr[0]
    for a in arr[1:]:
        if t == a:
            continue
        else:
            answer.append(a)
            t = a
    return answer