class Node:
    def __init__(self,data,pointer = 'Null'):
        self.data = data
        self.next = pointer

class LinkedList:
    def __init__(self,n):
        """
        n: size of linkedlist
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
                curr = Node(None,'Null')
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
            previous.next = new_node
        elif position.lower() == 'h':
            '''
                Insert at head node
            '''
            
            self.head_node = Node(data,self.head_node)
            
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
                self.last_node.next = Node(data,'Null')
                self.last_node = self.last_node.next
            else:
                self.last_node = Node(data)
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
        if position == 1:
            self.head_node = next_node
        self.length-=1
    
    def reverse(self):
        a = None
        b = None
        l = self.find_length()
        previous = None
        for i in range(l-1):
            a = self.head_node
            b = a.next
            self.head_node = b
            a.next = b.next
            b.next = a
            for _ in range(i+1,l-1):
                previous = b
                b = a.next
                c = b.next
                b.next = a
                previous.next = b
                a.next = c            
    
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