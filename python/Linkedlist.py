class example:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def append(self,name,age):
        new_node=example(name,age)
        if self.head is None:
            self.head=new_node
        else:
            curent=self.head
            while curent.next:
                curent=curent.next
            curent.next=new_node
    def append_at_the_beg(self,name,age):
        new_node=example(name,age)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        curent=self.head
        while curent:
            print(curent.name,curent.age,end="->")
            curent=curent.next
        print("None")
obj=Linkedlist()
obj.append("akhila",20)
obj.append_at_the_beg("akki",23)
obj.append("hassi",10)
obj.display()
        
            
