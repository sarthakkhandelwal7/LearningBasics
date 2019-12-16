from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        if len(self.visited)-1 <= vertex1 or len(self.visited) <= vertex2:
            self.visited.append(False)

    def dfs(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=" ")
        for i in self.graph[vertex]:
            if self.visited[i] is False:
                self.dfs(i)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 7)
    g.add_edge(2, 4)
    g.add_edge(7, 5)
    g.add_edge(7, 3)
    g.add_edge(3, 3)
    g.add_edge(5, 6)
    g.add_edge(6, 6)
    g.add_edge(4, 6)
    g.dfs(1)

