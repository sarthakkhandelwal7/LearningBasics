class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validity(root, lower = float('-inf'), upper = float('inf')):
            if not root:
                return True
            if root.val < lower or root.val > upper:
                return False
            if not validity(root.left, lower, root.val):
                return False
            if not validity(root.right, root.val, upper):
                return False
            return True
        return validity(root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(4)
    root.right.right.left.right = TreeNode(4)
    print(Solution().isValidBST(root))
