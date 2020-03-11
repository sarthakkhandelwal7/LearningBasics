from collections import defaultdict


class Solution:
    def findOrder(self, num_courses: int, pre_requisites: List[List[int]]) -> List[int]:
        parent = defaultdict(list)
        child = defaultdict(list)
        for i, j in pre_requisites:
            parent[i].append(j)
            child[j].append(i)
        order = [i for i in range(num_courses) if not parent[i]]
        for i in order:
            if parent[i]:
                return []

            for j in child[i]:
                parent[j].remove(i)
                if not parent[j]:
                    order.append(j)
        return order if len(order) == num_courses else []


if __name__ == '__main__':
    Solution().findOrder(6, [[1, 0], [2, 0], [1, 4], [3, 1], [3, 2], [1, 5], [5, 2]])