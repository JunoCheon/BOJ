# https://programmers.co.kr/learn/courses/30/lessons/72413
# #sample1
# n=6
# s=4
# a=6
# b=2
# fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# #sample2
# n=7
# s=3
# a=4
# b=1
# fares =[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# answer = 0


    
######################################
###########정확성100,효율성0##########
######################################
def howmuch(start,n):
    cost = [1000000 for _ in range(n)]
    cost[start-1]=0
    trace = [start-1]
    k=start-1
    while True:
        
        if len(cost)==len(trace):
            break
        for i in range(n):
            if graph[trace[-1]][i]>0:
                cost[i] = min(cost[i],graph[trace[-1]][i] + cost[trace[-1]])
        
        tmp_k = sorted([list(enumerate(cost))[i] for i in range(n) if i not in trace],key = lambda x:x[1])[0][0]
        if tmp_k==k:
            break
        k=tmp_k
        trace.append(k)
    
    return cost
def solution(n, s, a, b, fares):
    global graph
    graph =[[0 for _ in range(n)] for _ in range(n)]
    for i in fares:
        graph[i[0]-1][i[1]-1] = i[2]
        graph[i[1]-1][i[0]-1] = i[2]            
    
    answer = 100000001
    for i in range(n):
        cost1 = howmuch(s,n)
        cost2 = howmuch(i,n)
        answer = min(answer,cost1[i-1]+cost2[a-1] +cost2[b-1])

    return answer
  
  
  
#########################################
#######두번째 효율성 해결..##############
#########################################

from heapq import heappush, heappop

INF = int(1e9)
def dijkstra(graph, src):
    pq = [[0, src]]
    dist = [INF for _ in range(len(graph))]
    dist[src] = 0
    while pq:
        w, x = heappop(pq)
        if dist[x] < w:
            continue
        for y, cost in graph[x]:
            cost += w
            if cost < dist[y]:
                dist[y] = cost
                heappush(pq, [cost, y])
    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    ans = INF
    for src, dst, cost in fares:
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))
    for k in range(1, n + 1):
        dist_k = dijkstra(graph, k)
        ans = min(ans, dist_k[s] + dist_k[a] + dist_k[b])
    return ans