class Node:
    def __init__(self,value,n=None):
        self.data=value
        self.next_node=n
        self.previous_node=None
    def get_next(self):
        return self.next_node
    def get_previous(self):
        return self.previous_node
    def get_data(self):
        return self.data
    def set_next(self,value):
        self.next_node=value
    def set_previous(self,value):
        self.previous_node=value



class Doublylinkedlist:
    def __init__(self):
        self.head=None
        
    def insert(self,value):
        new_node=Node(value,self.head)
        if self.head:
            self.head.set_previous(new_node)
        self.head=new_node
        
    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.get_next()
        return count

    def remove(self,value):
        current=self.head
        while current:
            if current.get_data()==value:
                next_node=current.get_next()
                previous_node=current.get_previous()
                if next_node:
                    next_node.set_previous(previous_node)
                if previous_node:
                    previous_node.set_next(next_node)
                else:
                    self.head=current
                return True
            else:
                current=current.get_next()
        return ('Data not in the List')
    
    def find(self,value):
        current=self.head
        while current:
            if current.get_data==value:
                return('The data is present')
            else:
                current=current.get_next()
        return ('Data not in the list')
    def contents(self):
        current=self.head
        while current:
               print(current.get_data())
               current=current.get_next()
