class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heapify(self,curr_index,parent_index):
        while((parent_index>=0) and (self.heap[curr_index]>self.heap[parent_index])):
            t = self.heap[curr_index]
            self.heap[curr_index] = self.heap[parent_index]
            self.heap[parent_index] = t
            curr_index = parent_index
            parent_index = int((curr_index-1)/2)
    
    def insert(self,data):
        self.heap.append(data)
        curr_index = len(self.heap)-1
        parent_index = int((curr_index-1)/2)
        self.heapify(curr_index,parent_index)
    
    def parent(self,index, p = 'p'):
        """
            Return parent node of the given node
            p: It is used for not printing error message in selete function
        """
        if len(self.heap)-1>index:
            return self.heap[int((index-1)/2)]
        else:
            if p.lower() == 'p':
                print("Enter Correct index")
    
    def left(self,index, p = 'p'):
        """
            Return left node of the given node
            p: It is used for not printing error message in selete function
        """
        try:
            return self.heap[2*index+1]
        except:
            if p.lower() == 'p':
                print("Enter Correct index")
            else:
                return 'n'
    
    def right(self,index, p = 'p'):
        """
            Return right node of the given node
            p: It is used for not printing error message in selete function
        """
        try:
            return self.heap[2*index+2]
        except:
            if p.lower() == 'p':
                print("Enter Correct index")
            else:
                return 'n' 
    
    def delete(self,index):
        last_index = len(self.heap)-1
        s = self.heap[index]
        self.heap[index] = self.heap[last_index]
        self.heap[last_index] = s
        self.heap.pop()
        while(self.left(index,'n') != 'n'):
            try:
                                
                if self.left(index)>self.right(index,'n') and self.left(index,'n')>self.heap[index]:
                    s = self.heap[index]
                    self.heap[index] = self.heap[2*index+1]
                    self.heap[2*index+1] = s
                    index = 2*index+1

                    
                elif self.right(index,'n')>self.heap[index]:
                    s = self.heap[index]
                    self.heap[index] = self.heap[2*index+2]
                    self.heap[2*index+2] = s
                    index = 2*index+2
                else:
                    break

            except:
                if self.left(index,'n')>self.heap[index]:
                    s = self.heap[index]
                    self.heap[index] = self.heap[2*index+1]
                    self.heap[2*index+1] = s
                break
            
maxheap = MaxHeap()