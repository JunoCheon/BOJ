# https://www.acmicpc.net/problem/1789

n = int(input())
pos = 1 
res = 0
while True:
    res += pos
    if res > n:
        print(pos-1) 
        break 
    elif res == n:
        print(pos)
        break
    pos += 1
