# https://programmers.co.kr/learn/courses/30/lessons/60057
s = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
def solution(s):
    l = len(s)
    
    result = len(s)
    
    for i in range(1,(l//2)+1):
        if s[:i] == s[i:2*i] or i==1:
            
            ind = 0
            tmp =""
            tmp_result = 0
            double = 1
            while ind < len(s):
                
                if not tmp:
                    tmp += s[ind:ind+i]
                    tmp_result += i
                    ind += i
                elif tmp[-i:] == s[ind:ind+i]:
                    while tmp[-i:]==s[ind+i*double:ind+i*(double+1)]:
                        double += 1
                    ind += i*double
                    
                    if not double == 1:
                        tmp_result += len(str(double))
                else:
                    tmp += s[ind:ind+i]
                    tmp_result += min(i,len(s)-ind)
                    ind += i
            result = min(result,tmp_result)
        else:     
            pass
    return result

solution(s)