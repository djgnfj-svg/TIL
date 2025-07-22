def solution(nums):
    answer = 0
    A = set()
    for num in nums:
        A.add(num)
    
    # 이부분에서 원래는 math.ceil(len(A)/(len(nums)/2)) 이렇게 한 실수가 있었음
    # 생각해보면 간단했음 종류가 길이보다 많으면 그냥 길이 리턴하면 정답이였음
    if len(A) > len(nums)/2:
        answer = len(nums)/2
        
    else :
        answer = len(A)    
    
    return answer