# https://www.acmicpc.net/problem/1543

s = input()
word = input()

cnt = 0
    
while s.find(word) != -1:
    ind = s.find(word)

    s = s[ind+len(word):]
    cnt += 1
print(cnt)