from collections import defaultdict

def solution(participant, completion):
    
    part_dict = defaultdict(int)
    for person in participant:
        part_dict[person] += 1
    
    for comp in completion:
        part_dict[comp] -= 1
            
    return [key for key, value in part_dict.items() if value == 1].pop()