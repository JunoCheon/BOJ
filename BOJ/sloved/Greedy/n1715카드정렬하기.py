# https://www.acmicpc.net/problem/1715
import sys
n = int(input())
cards = sorted([int(input()) for _ in range(n)],key = lambda x: -x)
cards = [34, 7, 6, 5, 5, 4, 3, 2, 1, 1]

##############################
result = 0
for i in range(n-1):
    print(cards,result)
    
    tmp = cards.pop()
    cards[-1] += tmp
    result += cards[-1]
    cards.sort(key = lambda x: -x)
    
print(result)

for i in range(n-1):
    print(cards,result)
    
    
    cards[n-i-2] += cards.pop()
    result += cards[n-i-2]
    cards.sort(key = lambda x: -x)
print(result)


result = 0
for i in range(n-1):
    tmp = cards.pop(cards.index(min(cards)))
    result += tmp+min(cards)
    
    cards[cards.index(min(cards))] += tmp
    
print(result)
###O(N)이라서 실패
################################
##### HEAP 구현#################
###############################
import sys
import heapq
n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]

result = 0
heapq.heapify(cards)
while len(cards)>1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards,a+b)
    result += a+b
print(result)