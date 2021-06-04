# https://programmers.co.kr/learn/courses/30/lessons/60057
s = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
def solution(s):
    l = len(s)
    
    result = len(s)
    
    for i in range(1,(l//2)+1):
        if s[:i] == s[i:2*i] or i==1:
            
            checkind = 0
            ind = i
            numcnt = 0
            length = 0
            while ind < len(s):
                ind = checkind
                
                if s[ind:ind+i] == s[checkind:checkind+i]:
                    numcnt += 1
                    ind += i
                    
                elif s[ind:ind+i] != s[checkind:checkind+i]:
                    
                    
                    tmp += s[ind:ind+i]
                    tmp_result += min(i,len(s)-ind)
                    ind += i
            result = min(result,tmp_result)
        else:     
            pass
    return result

solution(s)