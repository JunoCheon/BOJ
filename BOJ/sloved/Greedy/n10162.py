t = int(input())
if t%10==0:
    print(t//300,
    (t-(t//300)*300)//60,
    ((t-(t//300)*300-((t-(t//300)*300)//60)*60)//10))
else:
    print(-1)