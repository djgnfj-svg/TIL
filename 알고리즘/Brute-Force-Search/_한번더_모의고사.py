def solution(answers):
    answer = []
    o = "12345"
    t = "21232425"
    s = "3311224455"
    
    for i, c in enumerate([o,t,s],1):
        k=0
        for j, a in enumerate(answers):
            #print(type(a))
            #print(type(c))
            if int(c[j%len(c)]) == a:
                k += 1
        answer.append(k)
    
    m = max(answer)
    x=[]
    for i, a in enumerate(answer,1):
        if m == a:
            x.append(i)
        
    return x