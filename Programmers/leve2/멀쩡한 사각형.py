# # https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3
# from math import gcd
# import math
# def gcd(x, y):
#    # y가 0이 될 때까지 반복
#    while y:
#        # y를 x에 대입
#        # x를 y로 나눈 나머지를 y에 대입
#        x, y = y, x % y
#    return x
# gcd(8,12)
# [8/4,12/4]

# def solution(w,h):
#     def gcd(x, y):
#         # y가 0이 될 때까지 반복
#         while y:
#             # y를 x에 대입
#             # x를 y로 나눈 나머지를 y에 대입
#             x, y = y, x % y
#         return x
    
    
#     if w==h:
#         return w*(w-1)
    
#     if w>h: return solution(h,w)
    
#     c = int(gcd(w,h))
#     w = int(w/c)
#     h = int(h/c)
#     answer = 0

#     for j in range(h):
#         if (w*j/h)%1:
            
#             answer[j-1][int((w*j/h)//1)] = 0
#             answer[j][int(w*j/h)//1] = 0
            
            
#     answer = sum([x.count(0) for x in answer])
    
#     return (w*h)*(c**2)-answer * c
    
# print(solution(8,12))  


# import math
# def solution(w,h):
#     if w==h:
#         return w*(w-1)
#     if w>h:
#         return solution(h,w)
#     a = 0
#     for i in range(1,w):
#         a += math.ceil(h*(i-1)/w) - 
        
        

import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))