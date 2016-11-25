class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self,value):
        self.next=value
        
class linkedlist:
        def __init__(self):
            self.head=None
        def insert(self, value):
            new_node = Node(value)
            new_node.set_next(self.head)
            self.head = new_node
                
        def size(self):
            current=self.head
            count=0
            while current:
                count+=1
                current=current.get_next()
            return count
        def search(self,value):
            current=self.head
            count=0
            found=False
            while current:
                if current.data==value:
                    found=True
                    return {'Found at position':count,'found':found}
                else:
                    current=current.get_next()
            if found==False:
                return('No such value in the node')
            
        def delete(self,value):
            current=self.head
            count=0
            found=False
            while current and found is False:
                if current.get_data()==value:
                    found=True
                else:
                    previous=current
                    current=current.get_next()
            if current is None:
                return "data is not in list"
            if previous is None:
                self.head=current.get_next()
            else:
                previous.set_next(current.get_next())
        def contents(self):
            current=self.head
            while current:
               print(current.get_data())
               current=current.get_next()
