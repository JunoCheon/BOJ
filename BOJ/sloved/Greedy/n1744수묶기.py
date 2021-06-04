# https://www.acmicpc.net/problem/1744
import sys
import heapq

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

# nums = [-1,2,1,3]
minus = [x for x in nums if x<0]
plus = [x for x in nums if x>1]
zero = 0 in nums
one = nums.count(1)
result = 0
heapq._heapify_max(plus)
while len(plus)>1:
    a = heapq._heappop_max(plus)
    b = heapq._heappop_max(plus)
    result += a*b
heapq.heapify(minus)
while len(minus)>1:
    a = heapq.heappop(minus)
    b = heapq.heappop(minus)
    result += a*b
if minus and zero:
    minus =[]
print(result+sum(minus+plus)+one)

