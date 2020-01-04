class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 1


class BinaryTree:
    def insert_node(self, root: TreeNode, val: int):
        root.size += 1
        if root.val < val:
            if root.right:
                self.insert_node(root.right)
            else:
                root.right = TreeNode(val)

        else:
            if root.left:
                self.insert_node(root.left)
            else:
                root.left = TreeNode(val)

    @staticmethod
    def delete(root: TreeNode, pos: str):
        if pos == 'right':
            node = root.right

        else:
            node = root.left

        if node.left is None and node.right is None:
            if pos == 'right':
                root.right = None
            else:
                root.left = None

        elif node.right is None:
            node = node.left
            while node.right.right is not None:
                node.size -= 1
                node = node.right
            node.size -= 1

        else:
            node = node.right
            while node.left.left is not None:
                node.size -= 1
                node = node.left
            node.size -= 1

    def delete_node(self, root: TreeNode, val: int):
        # Assuming node to be deleted is valid node
        root.size -= 1
        if root.val < val:
            if root.right.val == val:
                delete(root, 'right')
            else:
                self.delete_node(root.right)

        else:
            if root.left.val == val:
                delete(root, 'left')
            else:
                self.delete_node(root.left)

    def random_node(self):