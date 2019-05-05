class Queue:
    def __init__(self):
        self.que = list()
        self.index = 0
        self.length = 0
        self.first_in_que = None
    def en_queue(self,data):
        while self.index !=0:
            self.que[self.index] = self.que[self.index - 1]
            self.index-=1    
        if self.length != 0:   
            self.que[self.index] = data            
            self.que.append(self.first_in_que)
            self.length = len(self.que)
            self.index = self.length - 1
            first_in_que = self.que[self.length - 1]
        else:
            self.que.append(data)
            self.length = len(self.que)
            self.first_in_que = self.que[0]
    def de_queue(self):
        self.que.pop()
        self.length = len(self.que)
        self.index = self.length - 1
        self.first_in_que = self.que[self.index]
    def __str__(self):
        st = ''
        for i in self.que:
            st = st+' '+str(i)            
        return st