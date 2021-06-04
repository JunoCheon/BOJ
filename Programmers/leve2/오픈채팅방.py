# https://programmers.co.kr/learn/courses/30/lessons/42888

record  =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    
def solution(record):
    answer = []
    member_dict = {}
    for st in record:
        st = st.split()
        if st[0]=='Enter':
            member_dict[st[1]]= st[2]
            answer.append([st[1],'님이 들어왔습니다.'])
        elif st[0] == 'Leave':
            answer.append([st[1],'님이 나갔습니다.'])
        else:
            member_dict[st[1]] = st[2]
        
    answer = [member_dict[x[0]]+x[1] for x in answer]
    return answer
    

solution(record)
