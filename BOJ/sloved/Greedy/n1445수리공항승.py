# https://www.acmicpc.net/problem/1449

import sys

n,l = map(int, input().split())

ind = list(map(int,input().split()))
ind.sort()
if l==1:
    print(n)
else:
    cnt =1
    now = ind.pop(0)

    while ind:
        # 다음 ind[0]가 지금 테이프로 커버 가능하면 
        # pop만 하고 끝
        if ind[0] - now <= l-1:
            ind.pop(0) 
        # 다음 ind[0]가 멀다면 새로운 테이프 쓰기+pop+now업데이트
        else:
            now = ind.pop(0)
            cnt += 1 
    print(cnt)
    