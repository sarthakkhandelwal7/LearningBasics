from doubly_linked_list import DoublyLinkedList
class HashWithChaining:
    def __init__(self,size):
        self.size = size
        self.hash_table = ['']*size
    
    def insert(self,key):
        index = int(key*self.size)
        
        if type(self.hash_table[index]) is not str:
            self.hash_table[index].insert_node('e',key)
            
        else:
            self.hash_table[index] = DoublyLinkedList(0)
            self.hash_table[index].insert_node('h',key)
    
    def delete(self,key):
        index = int(key*self.size)
        if type(self.hash_table[index]) is not str:
            curr = self.hash_table[index].head_node
            previous = None

            if curr.data == key:
                if curr.next == 'Null':
                    self.hash_table[index] = curr.next
                else:
                    self.hash_table[index].head_node = curr.next

            else:
                while (curr != 'Null'):
                    if curr.data == key:
                        previous.next = curr.next
                    previous = curr
                    curr = curr.next
    def __str__(self):
        st = ''
        subst = ''
        for i in range(self.size):
            if type(self.hash_table[i]) is not str:
                curr = self.hash_table[i].head_node
                st+=f'{i}-->'
                while curr !='Null':
                    subst+=f'{curr.data}-->'
                    curr = curr.next
                st+=(subst[:len(subst)-3]+'\n')
                subst = ''
            else:
                st+=(f'{i}'+'\n')
        return st