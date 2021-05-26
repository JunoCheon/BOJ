N,K = input().split()
N,K = int(N),int(K)

index = K-1
l = list(range(1,N+1))
result = []

while True:
    result.append(l.pop(index))
    if not l:
        break
    index = (index+K-1)%len(l)

print('<'+', '.join(map(str, result))+'>')