# https://www.acmicpc.net/problem/4796

i=1
while True:
    l,p,v = map(int,input().split())
    if sum([l,p,v])==0:
        break
    result = (v//p)*l
    result += min((v%p),l)
    print("Case %d: %d" %(i,result))
    i += 1