# eq = input().split('-')

# if(eq[0]==''):
#     eq.pop(0)
#     result=0
#     if(eq!=[]):
#         for i in eq:
#             result -= eval(i)
# else:
#     result = eval(eq.pop(0))
#     if(eq!=[]):
#         for i in eq:
#             result -= eval(i)
# print(result)


arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i) 
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j) 
print(s)
