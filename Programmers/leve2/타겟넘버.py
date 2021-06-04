# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    
    
    def dfs(num,level):
        nonlocal answer
        
        if level == len(numbers):
            if num==target:
                answer+=1
            return
        if level == 0:
            dfs(-num,level+1)
            dfs(num,level+1)
        else:
            dfs(num+numbers[level],level+1)
            dfs(num-numbers[level],level+1)
            
    
    dfs(numbers[0],0)        
    return answer

solution([1,1,1,1,1,1,1,1],4)