# Python
class Queue(object):
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []
    
    def enqueue(self, data):
        self.items.insert(0, data)
        return '{} added to queue'.format(data)
    
    def dequeue(self):
        return self.items.pop()
    
    def sizequeue(self):
        return '{} size of queue'.format(len(self.items))

if __name__ == '__main__':
    q = Queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))

    print('pop',q.dequeue())
    print('pop',q.dequeue())