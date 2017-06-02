class node:
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
			self.low = node(data,None)
			self.hi = self.low
		#when one element in linked list
		elif self.hi == self.low:
			self.hi = node(data,None)
			self.low.next = self.hi 
		#else add new elements
		else:
			new = node(data,None)
			self.hi.next = new
			self.hi = new
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

t = input()
for i in xrange(t):
    n = input()
    if n==0:continue
    a = SLL()
    ls = map(int,raw_input().split())
    for i in ls:
        a.insert(i)
    print a
    a.clear()
'''
test input

2
0
2
1 2 
3
1 2 3 

test output

1
2
1
2
3

'''
    
    
