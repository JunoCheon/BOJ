#https://www.acmicpc.net/problem/13305


# import sys
# n = int(sys.stdin.readline())
# road = sys.stdin.readline().split()
# city = sys.stdin.readline().split()

n = int(input())
road = list(map(int,input().split()))
city  = list(map(int,input().split()))

result = 0
minval = city[0]
for i in range(n-1):
    if minval>city[i]:
        minval = city[i]
    result += minval*road[i]
print(result)