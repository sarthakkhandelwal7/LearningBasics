# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def preorder_traversal(root: Node):
        stack = list()
        preorder = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                preorder.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return preorder


if __name__ == '__main__':
    root_node = Node(10)
    root_node.left = Node(11)
    root_node.left.left = Node(7)
    root_node.right = Node(9)
    root_node.left.right = Node(12)
    root_node.right.left = Node(15)
    root_node.right.right = Node(8)
    print(Solution().preorder_traversal(root_node))
