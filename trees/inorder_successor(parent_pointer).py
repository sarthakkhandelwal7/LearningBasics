class TreeNode:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
        self.parent = None


def find_min_node(node):
    while node.left:
        node = node.left
    return node


def find_inorder_successor(node):
    if node.right:
        node = find_min_node(node.right)
    else:
        while node:
            node = node.parent
            if node.parent.left is node:
                node = node.parent
                break
    return node


def insert(node, data):
    # 1) If tree is empty then return a new singly node
    if node is None:
        return TreeNode(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

            # return  the unchanged node pointer
        return node


if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    root = insert(root, 8)
    root = insert(root, 22)
    root = insert(root, 4)
    root = insert(root, 12)
    root = insert(root, 10)
    root = insert(root, 14)
    node = root.left.right.right
    successor = find_inorder_successor(node)
    print(successor.data if successor else successor)
