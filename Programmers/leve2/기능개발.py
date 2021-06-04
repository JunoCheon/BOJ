# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    import math
    answer = []
    # progresses = [95, 90, 99, 99, 80, 99]; speeds=	[1, 1, 1, 1, 1, 1]
    # progresses = [93, 30, 55];speeds=	[1, 30, 5]
    days = [math.ceil((100-x[0])/x[1]) for x in zip(progresses,speeds)]
    now = 0
    
    for day in days:
        if day <= now:
            answer[-1] += 1
        else: 
            answer.append(1)
            now = day
    
    return answer
    
    