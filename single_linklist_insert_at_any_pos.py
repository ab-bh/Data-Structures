## insert node at any position in Linked list

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
	
	## function to implement the required task
	def insert_at_pos(self,data, pos):
		
		## if no node in the linked list (then make one)
		if self.lo ==None: 
			self.lo = Node(data,None)
			self.hi = self.lo 
		else:
			count=0
			temp = self.lo

			# get the length of the linked list
			while temp!=None:						
			    count+=1
			    temp = temp.next
			
			# insert at beginning (position = 0)
			if pos == 0:							
			    new = Node(data,None)
			    new.next = self.lo
			    self.lo = new
			# insert at end (psition >= linkedlist length)
			elif pos>=count:						
			    temp = self.lo 
			    while temp.next!=None:
			        temp = temp.next
			    new = Node(data,None)
			    temp.next = new
			# insert in position between 0 and linked list length
			else:									
				temp,p = self.lo,0
				while temp.next!=None and p<pos-1:
				    p+=1
				    temp = temp.next
				new =Node(data,None)
				new.next = temp.next
				temp.next = new
	# display the linked list
	def __str__(self):								
		if self.lo!=None:
			curr = self.lo
			to_show=str(curr.data)+'->'
			while curr.next!= None:
				curr = curr.next
				to_show+=str(curr.data)+ '->'
			return to_show[:len(to_show)-2]
		return ''
	def clear(self):
		self.__init__()


## test run for the above code
a = SLL()

a.insert_at_pos(1,5)
a.insert_at_pos(2,0)
a.insert_at_pos(3,0)
a.insert_at_pos(4,1)
print a


'''
Output:

3->4->2->1

'''