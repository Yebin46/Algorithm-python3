"""
깊이 우선 탐색 풀이
"""

def find_network(n, computers, computer, visit):
    visit[computer] = 1
    for candidate in range(n):
        if candidate != computer and computers[computer][candidate]:
            if not visit[candidate]:
                find_network(n, computers, candidate, visit)

def solution(n, computers):
    answer = 0
    visit = [0] * n # 노드 방문 여부
    for computer in range(n):
        if not visit[computer]: # 방문하지 않은 노드만 탐색
            find_network(n, computers, computer, visit)
            answer += 1 # 모두 탐색하고 나온 경우 == 하나의 네트워크
    return answer
