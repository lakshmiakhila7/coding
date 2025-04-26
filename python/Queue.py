class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue)==0:
            return "queue is empty"
        else:
            return self.queue.pop(0)
    def display(self):
        if len(self.queue)==0:
            return "queue is empty"
        for i in self.queue:
            print(i)
q=queue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.display()
