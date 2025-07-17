def solution(participant, completion):
    answer = ''
    count_dict = {}
    
    for p in participant:
        count_dict[p] = count_dict.get(p, 0) + 1
    
    for c in completion:
        count_dict[c] -= 1
        
    for i in count_dict.keys():
        if count_dict[i] == 1:
            answer = i
    return answer