# Tree Node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


# Print's Linked List
def prt(head):
    st = ''
    curr = head
    while curr:
        st += f'{curr.val}-->'
        curr = curr.next
    print(st[:len(st)-3])


class ListOfDepth:
    def __init__(self):
        self.list_head = []

    def create(self, root, j=0):
        if root:
            if j >= len(self.list_head):
                head = tail = ListNode(root.val)
                self.list_head.append([head, tail])
            else:
                new = ListNode(root.val)
                self.list_head[j][1].next = new
                self.list_head[j][1] = new
            self.create(root.left, j + 1)
            self.create(root.right, j + 1)


if __name__ == '__main__':
    root_node = Node(10)
    root_node.left = Node(11)
    root_node.left.left = Node(7)
    root_node.right = Node(9)
    root_node.left.right = Node(12)
    root_node.right.left = Node(15)
    root_node.right.right = Node(8)
    listofdepth = ListOfDepth()
    listofdepth.create(root_node)

    for i in listofdepth.list_head:
        prt(i[0])
