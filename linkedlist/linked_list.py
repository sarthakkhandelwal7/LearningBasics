class Node:
    def __init__(self,data,pointer):
        self.data = data
        self.pointer = pointer
class LinkedList:
    def __init__(self,n):
        self.n = n
        self.head_node = Node(None,'Null')
        self.last_node = None
        self.length = None
    def create_linklist(self):
        curr = self.head_node
        for i in range(1,self.n+1):
            curr.data = input('Enter data:')
            previous = curr
            if i <self.n: 
                curr = Node(None,'Null')
                previous.pointer = curr
            else:
                self.last_node = curr
    def __str__(self):
        st = 'Your data in link list'
        curr = self.head_node
        while curr !='Null':
            st+=f'\n{curr.data}'
            curr = curr.pointer 
        return st
    def insert_node(self,n,data,position = 0):
        if n == 1:
            '''
                Insert at head node
            '''
            new_node = Node(data,self.head_node)
            self.head_node = new_node
        elif n == 2:
            #Insert at last node
            new_node = Node(data,'Null')
            self.last_node.pointer = new_node
        else:
            #Insert node in between
            curr_next = None
            curr = self.head_node
            for _ in range(position-2):
                curr = curr.pointer
                curr_next = curr.pointer
            new_node = Node(data,curr_next)
            curr.pointer = new_node
    def delete_node(self,position):
        i=1
        previous = self.head_node
        curr = self.head_node
        next_node = curr.pointer
        while i<position:
            i+=1
            previous = curr
            curr = next_node
            next_node = curr.pointer
        previous.pointer = next_node
        if position == 1:
            self.head_node = next_node
    def reverse(self):
        a = None
        b = None
        l = self.find_length()
        previous = None
        for i in range(l-1):
            a = self.head_node
            b = a.pointer
            self.head_node = b
            a.pointer = b.pointer
            b.pointer = a
            for _ in range(i+1,l-1):
                previous = b
                b = a.pointer
                c = b.pointer
                b.pointer = a
                previous.pointer = b
                a.pointer = c
                
    def find_length(self):
        self.length=0
        curr_node = self.head_node.pointer
        while curr_node != 'Null':
            self.length+=1
            curr_node = curr_node.pointer
        self.length+=1
        return self.length
n = int(input('Enter length of Linked list:'))
ll = LinkedList(n)
ll.create_linklist()
