n = int(input())

Words = sorted([input() for _ in range(n)],
        key = lambda x : len(x),reverse=True)
def tmp(Words, i, j):
    #i번째 인풋 ex)'ABC'
    #j번째 알파벳 'A',...
    l = len(Words[i])
    output = []
    for k in range(l):
        if(Words[i][k]==j): output.append(l-1-k)
    result = 0
    for p in output:
        result += pow(10,p)
    return result


result = [0]*26
table = list(map(chr,list(range(65,65+26))))
for i in range(len(Words)):
    for j in range(26):
        result[j] += tmp(Words,i,table[j])
result2 = 0
for i in range(10):
    result2 += (9-i)*result.pop(result.index(max(result)))

print(result2)
