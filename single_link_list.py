## Insert in the beginning of linked list

## class to construct a node
class node:
	def __init__(self,data = None, next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return ""

## class to implement single link list
class SLL:
	def __init__(self):
		self.low = None
		self.hi = None
	def insert(self,data):
		#when nothing in the list
		if self.low == None:
			self.low = node(data,None)
			self.hi = self.low
		#when one element in linked list
		elif self.hi == self.low:
			self.low = node(data,None)
			self.low.next = self.hi 
		#else add new elements
		else:
			new = node(data,None)
			new.next = self.low
			self.low = new 
	def __str__(self):
		if self.low !=None:	
			curr = self.low
			disp = str(curr.data)+'\n'
			while curr.next!=None:
				curr = curr.next
				disp += str(curr.data)
				try: 
					if curr.next !=None: disp+='\n'
				except: pass
			return disp 
		return ""
	def clear(self):
		self.__init__()

## test run or above code
# create an instance of the SLL class
a = SLL()         

# enter length of SLL
for i in xrange(input()):
    # insert to SLL
    a.insert(input())
print '\n'
# display the SLL
print a

'''
Test input
5
1
2
3
4
5

Test output

5
4
3
2
1
'''
