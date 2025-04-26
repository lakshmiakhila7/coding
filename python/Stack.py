class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack)==0:
            return "stack is empty"
        return self.stack.pop()
    def display(self):
        if len(self.stack)==0:
            return "stack is empty"
        else:
            for i in reversed(self.stack):
                print(i)
s=stack()
s.push(10)
s.push(20)
s.pop()
s.display()

        
