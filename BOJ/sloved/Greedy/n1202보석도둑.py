# https://www.acmicpc.net/problem/1202

n,k = map(int,input().split())
jew = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

bag.sort()

i=2
for i in bag:
    tmp = sorted([x for x in jew if x[0]<=i], key = lambda x: x[1])
    while tmp:
        k = tmp.pop()
        
    