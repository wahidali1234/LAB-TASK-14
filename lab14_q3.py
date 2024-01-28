class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def depth_first_search(self, start):
        visited = set()
        self.dfs(start, visited)



sample_graph = Graph()
sample_graph.add_edge(0, 1)
sample_graph.add_edge(0, 2)
sample_graph.add_edge(1, 2)
sample_graph.add_edge(2, 0)
sample_graph.add_edge(2, 3)
sample_graph.add_edge(3, 3)


print("DFS traversal starting from node 2:")
sample_graph.depth_first_search(2)
