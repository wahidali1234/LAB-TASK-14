from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

    def shortest_path(self, start, end):
        if start == end:
            return [start]

        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)

        while queue:
            current_node, path = queue.popleft()

            if current_node == end:
                return path

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

        return None

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("BFS traversal starting from node 2:")
graph.bfs(2)

start_node = 0
end_node = 3
shortest_path = graph.shortest_path(start_node, end_node)

if shortest_path:
    print(f"\nShortest path from node {start_node} to node {end_node}: {shortest_path}")
else:
    print(f"\nNo path from node {start_node} to node {end_node}")
