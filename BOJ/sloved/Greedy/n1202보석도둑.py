# https://www.acmicpc.net/problem/1202
import sys
import heapq
n,k = map(int,input().split())
jew = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

bag.sort()
jew.sort(key = lambda x : -x[1])

jew = [[2, 99], [1, 65], [5, 23]]
bag = [2,10]
################
result = 0
for i in range(len(bag)):
    j=0
    while j < len(jew):
        if bag[i]>= jew[j][0]:
            bag[i] -= jew[j][0]
            result += jew[j][1]
            jew.pop(j)
            j = 0
        j += 1
        
print(result)
###############
heapq.heapify(jew)
tmp_jew = []
for i in bag:
    
    while jew and jew[0][0]<=i:
        heapq.heappush(tmp_jew,heapq.pop(jew)[1])




#############################
# https://www.acmicpc.net/problem/1202

n,k = map(int,input().split())
jew = []
heapq.heappush(jew,[map(int,sys.stdin.readline().split()) for _ in range(n)])
bag = [int(input()) for _ in range(k)]
bag.sort()


jew = [[2, 99], [1, 65], [5, 23]]
bag = [2,10]

tmp_jew = []
result = 0




#############최종
import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []

for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])  # Max heap
        heapq.heappop(jewelryList)

    if temp:
        result += heapq.heappop(temp)
    elif not jewelryList:
        break

print(-result)