import networkx as nx
def solution2(n, edge):
    answer = 0
    graph = nx.Graph()

    graph.add_edges_from(edge)

    # 노드 1에서 각 노드까지 최단 경로 길이 계산
    distance = nx.single_source_dijkstra_path_length(graph,1)
    
    max_distance = max(distance.values())
    farthest_nodes = [node for node, distance in distance.items() if distance == max_distance]

    answer = len(farthest_nodes)
    return answer

def solution(n,edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    while queue:
        i= queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] +1
    print("distances=",distances)
    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer

    
if __name__ == "__main__":
    print("main")
    n=6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    val = solution(n,vertex)