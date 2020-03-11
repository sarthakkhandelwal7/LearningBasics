class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        previous = None
        next = curr = head
        count = 0
        node = curr
        while node and count < k:
            node = node.next
            count += 1
        if count != k:
            return head

        # Reversing k-nodes
        while count:
            next = next.next
            curr.next = previous
            previous = curr
            curr = next
            count -= 1
        head.next = self.reverseKGroup(curr, k)
        return previous
