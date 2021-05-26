# https://programmers.co.kr/learn/courses/30/lessons/64061

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

board2 = [[board[i][j] for i in range(len(board))] for j in range(len(board))]


def move(array, basket):
    for i in range(len(array)):
        if array[i]!=0:
            basket.append(array[i])
            array[i]=0
            return array, basket
    return array, basket

def check(basket,answer):
    if len(basket)>1:
        if basket[-1] == basket[-2]:
            basket = basket[:-2]
            answer += 2
    return basket, answer
basket = []
answer = 0
for i in moves:
    board2[i-1], basket = move(board2[i-1],basket)
    basket, answer = check(basket,answer)