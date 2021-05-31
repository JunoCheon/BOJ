# https://programmers.co.kr/learn/courses/30/lessons/12973

s = 'aabbaabbaaaa'
text = [chr(i)*2 for i in range(97,97+26)]
def solution(s):
    if len(s)%2 == 1:
        return 0
    tmp = []
    i=0
    while i < len(s):    
        if not tmp:
            tmp.append(s[i])
        elif tmp[-1]==s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])
        i += 1
    
    if tmp:
        return 0
    else:
        return 1
    
s = "a"*1000000    
solution(s)

