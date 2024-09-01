from collections import deque

def check_add(now_word, check_word):
    same_cnt = 0

    for i in range(len(now_word)):
        if now_word[i] == check_word[i]:
            same_cnt += 1
    if same_cnt == len(now_word)-1:
        return 1
    else:
        return 0
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words: # 변환불가 (없음)
        return answer
    
    queue = deque([(begin, 0, [begin])])
    
    while queue:
        word, cnt, visited = queue.popleft() # word: 현재 단어 (바꾸려고 시도하려는 애)
        # 단어가 원하는 단어인가?
        if word == target:
            answer = cnt
            break
        
        # 바꿀 수 있는 단어를 추가
        for w in words: # w: 단어  set에 있는 단어 중 하나
            ## 이 단어를 위에서 방문했나?
            if w in visited:
                continue
            ## 이 단어가 1개만 다른가?
            if check_add(word, w): # 바꾸기 가능
                queue.append((w, cnt+1, visited +[w] ))
            

    return answer
