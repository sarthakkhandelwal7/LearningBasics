class Node:
    def __init__(self,data,previous = 'Null',next_n = 'Null'):
        self.data = data
        self.next = next_n
        self.previous = previous
class DoublyLinkedList:
    def __init__(self,n):
        """
            n: size of linkedlist
            length: Number of node present in linked list
        """
        self.n = n
        self.head_node = 'Null'
        self.last_node = None
        self.length = 0
    
    def create_linklist(self):
        self.head_node = Node(None,'Null')
        curr = self.head_node
        for i in range(0,self.n):
            curr.data = input('Enter data:')
            previous = curr
            
            # To prevent the generation of extra node since head node is generated outside the loop
            if i <(self.n-1): 
                curr = Node(None,previous)
                previous.next = curr
            else:
                self.last_node = curr
    
    def insert_node(self,position,data):
        if type(position) is int:
            #Insert node in between
            
            curr = self.head_node
            previous = None
                        
            for _ in range(position-1):
                previous = curr
                curr = curr.next
            new_node = Node(data,curr)
            curr.previous = new_node
            previous.next = new_node
            new_node.previous = previous
        elif position.lower() == 'h':
            '''
                Insert node at head node
            '''
            
            self.head_node = Node(data,'Null',self.head_node)
            if self.head_node.next is not 'Null':
                self.head_node.next.previous = self.head_node
            
            if self.last_node == None or self.last_node == 'Null':
                curr = self.head_node
                previous = None
                while curr !='Null':
                    previous = curr
                    curr = curr.next
                self.last_node = previous
        elif position.lower() == 'e':
            
            #Insert at last node
            if self.last_node:
                self.last_node.next = Node(data,self.last_node)
                self.last_node = self.last_node.next
            else:
                self.last_node = Node(data,self.head_node)
                self.head_node.next = self.last_node
        
        self.length+=1
    
    def delete_node(self,position):
        i=1
        previous = self.head_node
        curr = self.head_node
        next_node = curr.next
        while i<position:
            i+=1
            previous = curr
            curr = next_node
            next_node = curr.next
        previous.next = next_node
        new_node.previous = previous
        if position == 1:
            self.head_node = next_node
            self.head_node.previous = 'Null'
        self.length-=1
    
    def find_length(self):
        self.length=0
        curr_node = self.head_node.next
        while curr_node != 'Null':
            self.length+=1
            curr_node = curr_node.next
        self.length+=1
        return self.length
    
    def __str__(self):
        st = ''
        curr = self.head_node
        while curr !='Null':
            st+=f'{curr.data}-->'
            curr = curr.next
        return st[:len(st)-3]