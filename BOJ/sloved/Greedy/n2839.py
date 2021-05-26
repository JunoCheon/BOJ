N = int(input())
min=1667
for i in range(1,1667):
    for j in range(i+1):
        if(N == (j*3 + (i-j)*5)):
            if(min>i):min=i
if(min==1667):print(-1)
else:print(min)   
