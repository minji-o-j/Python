from itertools import product
def solution(info, query):
    """
    info: 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열
    query: [언어] and [직군] and [경력] and [소울푸드] [점수]
    """
    
    # info table
    """
    info를 저장한다
    """
    info_dict = dict([])
    for i in info:
        splited = i.split() # 	['java', 'backend', 'junior', 'pizza', '150']
        items = [['-', splited[0]],['-', splited[1]],['-', splited[2]],['-', splited[3]]]
        producted_items = list(product(*items)) #*을 붙여야함

        for pi in producted_items:
            try:
                info_dict[''.join(pi)].append(int(splited[-1]))# 점수 저장
            except:
                info_dict[''.join(pi)] = [int(splited[-1])]
    
    # list 정렬
    for id in info_dict:
        info_dict[id].sort()
    
    # query 처리
    query_keys = []
    for q in query:
        splited = q.split()
        score = splited[-1]
        keys = splited[0]+splited[2]+splited[4]+splited[6]
        query_keys.append((keys, int(score)))
        
    # 정답 찾기                                             
    answer = []
    for qk in query_keys:
        try:
            finded_list = info_dict[qk[0]]
            
        except KeyError:
            answer.append(0)
            continue
        
            
        # 이분탐색
        start = 0
        info_len = len(finded_list)
        end = info_len

        while start<end:
            mid = (start+end)//2
            mid_score = finded_list[mid]
            if qk[1] > mid_score: # target > mid score
                start = mid+1
            else:
                end = mid

        answer.append(info_len-start) # len(finded_list[start:])) # 리스트 슬라이싱: 시간복잡도 오래걸림
        
    return answer
