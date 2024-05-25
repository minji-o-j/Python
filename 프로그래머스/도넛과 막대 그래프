# 2024 KAKAO WINTER INTERNSHIP - 도넛과 막대 그래프

def solution(edges):
    answer = []
    
    # 일단 노드 개수를 모두 저장한다..
    node_all = set([])
    node_0 = {}
    node_1 = {}
    
    for i,j in edges:
        node_all.add(i)
        node_all.add(j)
        
        try:    node_0[i] +=1
        except: node_0[i] = 1
        try:    node_1[j] +=1
        except: node_1[j] = 1

    
    # 정점 찾기
    """
    [0]인 요소가 2개 이상 인 것 중, [1]이 2개 이상이 아닌 것
    """
    check_0_over2 = set([])
    check_1_over2 = set([])
    
    for i in node_0:
        if node_0[i]>=2:
            check_0_over2.add(i)
    for i in node_1:
        if node_1[i]>=2:
            check_1_over2.add(i)
            
    vertex = list(check_0_over2 - check_1_over2)[0]

    # 8자 그래프 찾기
    """
    정점인 것을 제외하고 [0]인 요소가 2개 이상인 것 개수
    """
    graph_8 = len(check_0_over2)-1

    # 막대모양 그래프
    """
    노드가 존재하지만 거기서 시작하는 노드가 있지 않는 것의 개수
    """
    graph_stick = len(node_all - set(node_0))
    
    
    # 도넛그래프
    """
    루트 노드 진출개수 - 8자 - 막대
    """
    graph_doughnut = node_0[vertex] - graph_8 - graph_stick

    # 순서대로 저장
    answer.append(vertex)
    answer.append(graph_doughnut)
    answer.append(graph_stick)
    answer.append(graph_8)
    
    return answer
