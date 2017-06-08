class Node:
	def __init__(self,data = None, next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return ""

class SLL:
	def __init__(self):
		self.low = None
		self.hi = None
	def insert(self,data):
		#when nothing in the list
		if self.low == None:
			self.low = Node(data,None)
			self.hi = self.low
		#when one element in linked list
		elif self.hi == self.low:
			self.hi = Node(data,None)
			self.low.next = self.hi 
		#else add new elements
		else:
			new = Node(data,None)
			self.hi.next = new
			self.hi = new
	
	# reversing of list

	def reverse(self):
		prev = None 
		curr = self.low
		while curr!=None:
			next_ = curr.next
			curr.next = prev
			prev = curr
			curr = next_
		self.low = prev
	
	def __str__(self):
		if self.low !=None:	
			curr = self.low
			disp = str(curr.data)+' '
			while curr.next!=None:
				curr = curr.next
				disp += str(curr.data)+' '
				try: 
					if curr.next ==None: disp+='\n'
				except: pass
			return disp 
		return ""
	def clear(self):
		self.__init__()

a = SLL()
a.insert(1)
a.insert(2)
a.insert(3)
print "sll: ",a
a.reverse()
print "reversed sll: ",a
a.clear()


'''
test output

sll: 1 2 3

reversed sll: 3 2 1 

'''