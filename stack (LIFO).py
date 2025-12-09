class Stack:
    def __init__(self):
        self.stack = []
        self.numofitems = 0

# checcking the stack is empty
    def isEmpty(self):
        return self.stack == []
    
#pushing element
    def push(self,data):
        self.stack.insert(self.numofitems, data)
        self.numofitems += 1 #increment index
        return '{} pushed to stack'.format(data)
    #deleting the emement 

    def pop(self):
        self.numofitems -= 1
        data =self.stack.pop(self.numofitems)
        return '{} pop to stack',format(data)
    
    def stacksize(self):
        return len(self.stack)
    
#testing

if __name__ == '__main__' :
    s=Stack()
    print(s.push(1))
    print(s.push(2))
    print(s.push(3))
    print(s.push(4))
    print(s.push(5))



    print(s.pop())
    print(s.pop())
    print(s.pop())

    print('size of stack', s.stacksize())