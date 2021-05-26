n = int(input())
rope = [0]*n
for i in range(n):
    rope[i] = int(input())
    
# rope.sort(key = lambda x : -x)
# Max=0
# len_r = len(rope)+1
# while (len_r > len(rope)):
#     len_r = len(rope)
#     for i in range(len_r+1):
#         if(i==(len_r)):
#             weight = min(rope)*len_r
#         else:
#             weight = min(rope[0:i]+rope[i+1:]) *(len_r-1)
#         if Max < weight:
#             Max = weight
#             index = i
#     rope = rope[0:index]+rope[index+1:]

# print(Max)

rope.sort(reverse=True)

answer = []

for i in range(n):
    answer.append(rope[i]*(i+1))

print(max(answer))