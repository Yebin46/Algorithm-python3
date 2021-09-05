import re

def check_edge_point(text):
    if len(text) == 1 and text[0] == '.':
        return ''
    if text[0] == '.':
        text = text[1:]
    if text[-1] == '.':
        text = text[:-1]
    return text
        
def solution(new_id):
    answer = ''
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    
    # step 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # step 4
    new_id = check_edge_point(new_id)

    # step 5
    if not new_id:
        new_id = 'a'
    
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = check_edge_point(new_id)
    
    # step 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    answer=new_id
    return answer