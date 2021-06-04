# https://www.acmicpc.net/problem/1439

import sys

s = list(sys.stdin.readline())
s = s[:-1]

# s=list('000000')
stack = [s.pop(0)]
while s:
    tmp = [s.pop(0)]
    if stack[-1:] != tmp:
        stack.append(tmp[0])
        
print(min(stack.count('0'),stack.count('1')))