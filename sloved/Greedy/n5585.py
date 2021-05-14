a = 1000-int(input())
coins = [1,5,10,50,100,500]
i=5
n = 0
while(a!=0):
    k = a//coins[i]
    if(k):
       a = a - k * coins[i]
       n += k
    i -= 1
print(n)