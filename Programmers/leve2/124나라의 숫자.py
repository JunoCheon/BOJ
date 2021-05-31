# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    
    def samjin(x):
        T = '124'
        q,r = divmod(x-1,3)
        if q==0:
            return T[r]
        else:
            return samjin(q) + T[r]
    return samjin(n)

