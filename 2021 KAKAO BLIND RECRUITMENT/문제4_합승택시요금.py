import math
from heapq import heappush, heappop


def dijkstra(n, graph, s):
    D = [math.inf for _ in range(n)] # start 기준의 거리 행렬
    D[s] = 0 # 자기 자신 0

    queue = []
    heappush(queue, [D[s], s]) # 요금과 지점을 함께 큐에 넣어줌
    while queue:
        current_dist, current_dest = heappop(queue) # 힙에서 가장 작은 항목을 pop
        if D[current_dest] >= current_dist: # s에서 current_dest로 가는 요금이 이미 저장된 요금보다 적을 때만 진행
            for i in range(n):
                new_dist = current_dist + graph[current_dest][i]
                if new_dist < D[i]: # current_dest를 거쳐 i 지점으로 가는 거리가 이미 저장된 요금보다 작으면 갱신
                    D[i] = new_dist
                    heappush(queue, [new_dist, i])
    return D


def solution(n, s, a, b, fares):
    answer = math.inf

    # convert to index
    s -= 1
    a -= 1
    b -= 1

    graph = [[math.inf for _ in range(n)] for _ in range(n)]
    for node_1, node_2, fare in fares:
        graph[node_1 - 1][node_2 - 1] = fare
        graph[node_2 - 1][node_1 - 1] = fare

    # 모든 노드(지점)에 대해 다익스트라 수행
    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))

    for node in range(n):
        answer = min(answer, min_graph[s][node] + min_graph[node][a] + min_graph[node][b])

    return answer