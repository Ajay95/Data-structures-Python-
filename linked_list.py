class Node():
    def __init__(self,new_node,data):
        self.data=data
        self.next=new_node
    def get_next(self):
        return self.next
    def get_value(self):
        return self.data
    def set_next(self,node):
        self.next=node
class linked():
    def __init__(self):
        self.head=None
        self.count=0
    def insert(self,data):
        new_node=Node(self.head,data)
        self.head=new_node
        self.count+=1
    def show(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print('number of nodes {}'.format(self.count))    
    def delete(self,data):
        current=self.head
        previous=None
        while current:
            if current.data==data:
                if previous:
                    previous.set_next(current.next)
                else:
                    self.head=current.next
                self.count-=1
                return('Removed {} from the list'.format(data))
            else:
                previous=current
                current=current.next
        return "No such data"
    
            
    
