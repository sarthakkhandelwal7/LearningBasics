# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def level_order(root: TreeNode):
        if not root:
            return []
        queue = deque()
        levels = []
        level = 0
        queue.append(root)
        while queue:
            levels.append([])
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels


if __name__ == '__main__':
    root_node = TreeNode(10)
    root_node.left = TreeNode(11)
    root_node.left.left = TreeNode(7)
    root_node.right = TreeNode(9)
    root_node.left.right = TreeNode(12)
    root_node.right.left = TreeNode(15)
    root_node.right.right = TreeNode(8)
    print(Solution().level_order(root_node))
