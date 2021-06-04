# https://www.acmicpc.net/problem/15954


import sys
import math
from decimal import *
 
fastinput = lambda: sys.stdin.readline().rstrip()
 
n, K = map(int, fastinput().split())
 
preference = list(map(int, fastinput().split()))

def std(list):
    result = 0
    m = sum(list)/len(list)
    for i in list:
        result+= (i-m)**2
    return math.sqrt(result/len(list))
result = 999999
for i in range(K,n+1):
    for j in range(n-i+1):
        result = min(result,std(preference[j:j+i]))
        
print(result)