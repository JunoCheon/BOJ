# https://www.acmicpc.net/problem/2437

n = int(input())
chu = sorted(list(map(int,input().split())))

target = 1

for i in chu:
    if target<i:
        break
    target +=i
    
print(target)