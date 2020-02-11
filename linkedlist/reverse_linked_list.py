class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = next_node = head
        previous = None
        while next_node:
            next_node = next_node.next
            curr.next = previous
            previous = curr
            curr = next_node

        return previous
