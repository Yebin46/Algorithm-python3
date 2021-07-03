def solution(array, commands):
    answer = []
    for content in commands:    
        b = sorted(array[(content[0]-1):content[1]])
        answer.append(b[content[2]-1])
    return answer