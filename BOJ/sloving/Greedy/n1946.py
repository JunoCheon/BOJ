#https://www.acmicpc.net/problem/1946

# def isok(score):
#     l = len(score)
#     for i in range(l):
#         tmp = score[:i]+score[i+1:]
        
#         for j in tmp:
#             if(score[i][0]>j[0] and score[i][1]>j[1]):
#                 return False
#     return True  

import sys

import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    score = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)],
                   key=lambda x:x[0])

    # score.sort(key = lambda x: (x[0],x[1]),reverse=True)
    # j=0
    # while(not isok(score)):
    #     del score[j]
    #     j +=1
    
    # print(len(score))

    p = n+1
    ans = 0
    for s,e in score:
        if p >e:
            ans+=1
            p = e
    print(ans)