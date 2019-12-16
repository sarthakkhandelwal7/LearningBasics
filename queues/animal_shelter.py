class ListNode:
    def __init__(self, family, name):
        self.family = family
        self.name = name
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, family, name):
        if self.head is None:
            self.head = self.tail = ListNode(family, name)
        else:
            self.tail.next = ListNode(family, name)
            self.tail = self.tail.next

    def dequeue_any(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            return temp
        else:
            return None

    def dequeue_dog(self):
        node = self.head
        try:
            while node.next.family != 'Dog':
                node = node.next
        except:
            return 'No dog availabe'
        temp = node.next
        node.next = node.next.next
        return temp

    def dequeue_cat(self):
        node = self.head
        try:
            while node.next.family != 'Cat':
                node = node.next
        except:
            return 'No cat availabe'
        temp = node.next
        node.next = node.next.next
        return temp


if __name__ == '__main__':
    animalshelter = AnimalShelter()
    animalshelter.enqueue('Dog', 'runner')
    animalshelter.enqueue('cat', 'jack')
    print(animalshelter.dequeue_any().family)
    print(animalshelter.dequeue_any().family)
    animalshelter.enqueue('cat', 'jack')
    print(animalshelter.dequeue_dog())
