import numpy as np

x,y,a0,a1,n = input().split()
def An(x,y,a0,a1):
    A = np.array([int(a0[0]),int(a1[0]),
                int(a0[1]),int(a1[1])]).reshape(2,2)
    X = np.array([int(x),int(y)]).reshape(-1,1)
    s = np.matmul(A,X).sum()
    if(s<10):
        s = '0'+str(s)
    return(str(s))

i=0
while True:
    if i==n:
        break
    a = a1
    a1 = An(x,y,a0,a1)
    a0 = a
    i+=1