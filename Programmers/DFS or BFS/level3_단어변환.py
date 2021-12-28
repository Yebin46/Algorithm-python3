answer = 0
def solution(begin, target, words):
    if target not in words: # target 단어가 words에 없는 경우 변환 불가
        return 0

    dfs(begin, target, 0, words)
    return answer

def change(start_word, end_word):
    for apb in range(len(start_word)): # 한 글자만 다른 경우가 있으면 True
        if start_word[:apb]+start_word[apb+1:] == end_word[:apb]+end_word[apb+1:]:
            return True
    return False

def dfs(begin, target, depth, words):
    global answer
    # print(words)
    if begin == target:
        answer = depth
        return
    else:
        if len(words) == 0:
            return

        for word_idx in range(len(words)):
            if change(begin, words[word_idx]):
                word = words[:word_idx] + words[word_idx+1:]
                dfs(words[word_idx], target, depth+1, word)
