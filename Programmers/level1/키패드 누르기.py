def solution(numbers, hand):
    for i in range(len(numbers)):
        if numbers[i]== 0:
            numbers[i]=11
    points = [10,12]
    result = ""
    
    def move(hands, num,result,points):
        if hands=='left':
            points[0] = num
            result +="L"
        else:
            points[1] = num
            result += "R"
        return result, points
    def to_mat(a):
        return [(a-1)//3+1,(a-1)%3+1]


    def dist(hands,num):
    
        if hands=='left':
            k=0
        else: k=1
    
        return abs(to_mat(points[k])[0]-to_mat(num)[0])+abs(to_mat(points[k])[1]-to_mat(num)[1])

    for a in numbers:
    
        if a in [1,4,7]:
            result, points = move('left',a,result,points)
        elif a in [3,6,9]:
            result, points = move('right',a,result,points)
        else:
            if dist('right',a) > dist('left',a):
                #왼손이 가까움
                result, points = move('left',a,result,points)
            elif dist('right',a) == dist('left',a):
                #거리가 같음
                if hand=='right':
                    result, points = move('right',a,result,points)
                else:
                    result, points = move('left',a,result,points)   
            else:
                #오른손이 가까움
                result, points = move('right',a,result,points)
    return result

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')