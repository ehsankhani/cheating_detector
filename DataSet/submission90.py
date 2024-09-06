def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_vertex in graph[start] - visited:
        dfs(graph, next_vertex, visited)

def main():
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print("DFS starting from vertex A:")
    dfs(graph, 'A')

if __name__ == "__main__":
    main()
