class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Solution:

    @staticmethod
    def isBalanced(root) -> bool:
        def check_hight(root):
            if root is None:
                return 0
            left = check_hight(root.left)
            right = check_hight(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return check_hight(root) != -1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(4)
    root.right.right.left.right = TreeNode(4)
    print(Solution().isBalanced(root))
