# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def find_lowest_common_ancestor(self, node: 'TreeNode', a: 'TreeNode', b: 'TreeNode') -> 'TreeNode':
        def helper(curr: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            if curr is None:
                return False
            left = helper(curr.left, p, q)
            right = helper(curr.right, p, q)
            mid = curr == p or curr == q
            if left + right + mid >= 2:
                self.ans = curr
            return left or right or mid
        helper(node, a, b)
        return self.ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    print(Solution().find_lowest_common_ancestor(root, root.right.left, root.right.right.right).val)
