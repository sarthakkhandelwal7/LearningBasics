class Solution:
    def __init__(self):
        self.all_paths = []

    def allPathsSourceTarget(self, graph):

        def helper(graph, vertex, path):
            path.append(vertex)
            if vertex == len(graph) - 1:
                return path[:]
            for i in graph[vertex]:
                temp = helper(graph, i, path[:])
                if temp and temp[-1] == len(graph)-1:
                    self.all_paths.append(temp)
        helper(graph, 0, [])
        return self.all_paths


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
