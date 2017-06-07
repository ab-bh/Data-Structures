#contributors: Huzaifa Faruqui, Abhishek Bhatt

## class to make a node 
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
 
## class to implement linked list
class SLL:
    def __init__(self):
        self.lo = None
        self.hi = None
        self.count = 0
 
 
    ## function to implement the required task
    def insert_at_pos(self, data, pos):
 
        ## if no node in the linked list (then make one)
        if self.lo ==None: 
            self.lo = Node(data,None)
            self.hi = self.lo 
        else:
            # insert at beginning (position = 0)
            if pos == 0:                            
                new = Node(data,None)
                new.next = self.lo
                self.lo = new
            # insert at end (psition > linkedlist length)
            elif pos==self.count:                        
                new = Node(data,None)
                self.hi.next = new
            # insert in position between 0 and linked list length
            else:                                   
                temp, p = self.lo, 0
                while p<pos-1:
                    p+=1
                    temp = temp.next
                new = Node(data,None)
                new.next = temp.next
                temp.next = new
        self.count += 1       
 
 
    def Delete(self, position):
 
        if position==0:
            self.lo = self.lo.next 
 
        elif position==self.count-1:
            temp = self.lo
            while temp.next.next!=None:
                temp = temp.next
            temp.next = None
 
        else:
            temp, p =self.lo, 0
            while p<position-1:  
                temp = temp.next
                p+=1
 
            temp.next = temp.next.next  
 
        self.count -= 1
               
    # display the linked list
    def __str__(self):                              
        if self.lo!=None:
            curr = self.lo
            to_show=str(curr.data)+'->'
            while curr.next != None:
                curr = curr.next
                to_show+=str(curr.data)+ '->'
            return to_show[:len(to_show)-2]
        return ''
    def clear(self):
        self.__init__()
 
a = SLL()
 
a.insert_at_pos(1,1)
a.insert_at_pos(2,0)
a.insert_at_pos(3,0)
a.insert_at_pos(5,2)
print a
a.Delete(3)
print a
