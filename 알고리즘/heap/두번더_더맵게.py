import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        r = f + s*2
        heapq.heappush(scoville, r)
        answer += 1
    return answer