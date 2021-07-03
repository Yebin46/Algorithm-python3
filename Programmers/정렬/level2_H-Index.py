def solution(citations):
    answer = 0
    temp = 0
    paper_num = len(citations)
    
    for h in range(paper_num+1):
        over_list = list(filter(lambda x: citations[x]>=h, range(paper_num)))
        if len(over_list) >= h and h >= temp:
            temp = h        
    answer = temp
    
    if paper_num == 1: return 1
    return answer