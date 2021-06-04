# https://www.acmicpc.net/problem/1080
import sys

n, m = map(int,sys.stdin.readline().split())
A=[]
for i in range(n):
    tmp = list(sys.stdin.readline())
    A.append(tmp[:m])
B=[]
for i in range(n):
    tmp = list(sys.stdin.readline())
    B.append(tmp[:m])

# example
# n,m=3,4   
# A = [['0', '0', '0', '0'], ['0', '0', '1', '0'], ['0', '0', '0', '0']]
# B = [['1', '0', '0', '1'], ['1', '0', '1', '1'], ['1', '0', '0', '1']]


if (A.count('1') + B.count('1'))%2 == 1:
    print(-1)
else:
    count = 0
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j]!=B[i][j]:
                count += 1
                for p in range(3):
                    for q in range(3):
                        # if eval(A[i+p][j+q]):
                        #     A[i+p][j+q] = '0'
                        # else:
                        #     A[i+p][j+q] = '1'
                        #간단하게 만들기
                        A[i+p][j+q] = str(1 - eval(A[i+p][j+q]))
    if A==B:
        print(count)
    else:
        print(-1)
        
