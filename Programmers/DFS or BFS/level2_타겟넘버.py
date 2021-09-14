'''
깊이 우선 탐색 풀이
'''

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers): # 트리 끝에 도달했을 때
        if sum(numbers) == target: # 다 더한 값이 target과 같으면 answer += 1
            return 1
        else: # 다르면 더하지 않음
            return 0
    else: # 트리 끝에 도달하지 않았다면
        answer += dfs(numbers, target, depth+1) # 다음 숫자를 더해서 트리 깊이를 +1
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1) # 다음 숫자를 빼서 트리 깊이를 +1
        return answer

def solution(numbers, target):
    return dfs(numbers, target, 0)