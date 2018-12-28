class Stacks:
    def __init__(self,size):
        self.sta = [None]*size
        self.start_pointer = 0
        self.end_pointer = 0
        self.space = size
        self.size = size
        self.cell_data = None 
    def push(self,data):
        if self.space:
            self.sta[self.size - self.space] = data  
            self.end_pointer =  self.size - self.space
            self.space-=1
        else:
            print('Stack is full')
    def pop(self,resp):
        if self.space<self.size:
            if resp:
                self.cell_data = self.sta[self.end_pointer] 
            self.sta[self.end_pointer] = None
            self.end_pointer-=1
            self.space+=1
            if self.space==self.size:
                self.end_pointer+=1
                
        else:
            print('Stack is empty nothing to pop')
    def __str__(self):
        i = self.end_pointer
        st = ''
        while i>=0:
            st+='{}\n'.format(self.sta[i])
            i-=1

        return st
