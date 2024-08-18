from collections import deque
def solution(n, wires):
    """
    bfs 혹은 dfs로 n의 하위 항목에 몇개의 노드가 있는지 센다
    """
    tree_queue = deque(wires)
    # make tree
    tree = dict([])
    while tree_queue:
        # start
        w = tree_queue.popleft()
        if len(tree)==0:
            tree[w[0]]=set([w[1]])
            tree[w[1]]=set([])
            
        else:
            # 노드 존재 확인
            if w[0] in tree:
                tree[w[0]].add(w[1])
                tree[w[1]]=set([])

            elif w[1] in tree:
                tree[w[1]].add(w[0])
                tree[w[0]]=set([])
            else:
                tree_queue.append(w)
                
    count_node = []
    for k in tree: # 각 노드 아래 몇개의 노드가 있나 세기
        # dfs (연습용, bfs로해도됨)
        stack = [k]
        visited = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            stack+=(tree[node]-set(visited))
            
        count_node.append(abs(len(visited)-(n-len(visited)))) # len(visited): 자기 자신 포함 노드 개수
                
        """
        #bfs
        node_queue = deque([k])
        visited = []
        while node_queue:
            node = node_queue.popleft()
            if node not in visited:
                visited.append(node)
            node_queue+=(tree[node]-set(visited))
            
        count_node.append(abs(len(visited)-(n-len(visited)))) # len(visited): 자기 자신 포함 노드 개수
        """
    
    return min(count_node)
