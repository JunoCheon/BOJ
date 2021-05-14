n =int(input())
a = [0]*n
for i in range(n):
    a[i] = list(map(int, input().split()))

a1 = sorted(a,key = lambda x : (x[1],x[0]))

count = 0
EndTime = 0
for i,j in a:
    if i >= EndTime:
        count += 1
        EndTime = j
print(count)