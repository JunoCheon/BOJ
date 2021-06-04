# https://programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    import heapq
    answer = 0
    
    import heapq
    heapq.heapify(scoville)
    while scoville[0]<K:
        a = heapq.heappop(scoville)
        if not scoville:
            return -1
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        answer += 1
        
    return answer