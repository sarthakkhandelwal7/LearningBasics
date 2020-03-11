class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_match(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True

            elif not t1 or not t2:
                return False

            if t1.val == t2.val:
                if is_match(t1.left, t2.left) and is_match(t1.right, t2.right):
                    return True
                else:
                    return False

        if is_match(s, t):
            return True
        if not s:
            return False

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    # Tree 1
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.right = TreeNode(5)
    #root1.left.right.left = TreeNode(0)

    # Tree 2
    root2 = TreeNode(4)
    root2.left = TreeNode(1)
    root2.right = TreeNode(2)

    print(Solution().isSubtree(root1, root2))