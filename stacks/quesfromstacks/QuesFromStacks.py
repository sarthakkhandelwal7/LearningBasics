from stacks import  Stacks
class QuesBystacks:
    def __init__(self,size,stack1,stack2):
        self.size = size
        self.stack1 = stack1
        self.stack2 = stack2
    def creat_que(self):
        for i in range(self.size):
            stack1.push(int(input('Please enter data:')))
        for i in range(self.size):
            stack1.pop(True)
            stack2.push(stack1.cell_data)
size = int(input('Enter size of que'))
stack1 = Stacks(size)
stack2 = Stacks(size)
que = QuesBystacks(size,stack1,stack2)
que.creat_que()
print(stack2)