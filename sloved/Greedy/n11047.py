n,k = map(int, input().split())
a=[0]*n


for i in range(n):
    a[i] = int(input())


coin=0
while(k!=0):
    coin += k//a[i]
    k = k - a[i]*(k//a[i])
    i-=1
print(coin)