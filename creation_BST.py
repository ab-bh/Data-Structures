## class for node creation
class Node(object):
	def __init__(self,data = None):
		self.left = None
		self.right = None
		self.data = data
	def __str__(self):
		return str(self.data)


## the Binary Search Tree class
class BST(object):
	def __init__(self):
		self.root = None

	def insert(self,val):
		if self.root == None:
			self.root = Node(val)
		else:
			root = self.root
			while True:
				if val<root.data:
					if not root.left:
						root.left = Node(val);break
					else:
						root = root.left
				else:
					if not root.right:
						root.right = Node(val);break
					else:
						root = root.right

	def traverse(self): ## level order traversals 
		nodes = []
		nodes.append(self.root)
		print "BST representation"
		while nodes:
			current = nodes.pop(0)
			print current.data,
			if current.left:
				nodes.append(current.left)
			if current.right:
				nodes.append(current.right)
	
	def clear(self):
		print "\n\nre-initializing\n"
		self.__init__()

## creating an instance for the BST
bst = BST()
for tc in xrange(input("enter the number of values: ")):
	val = input("val: ")
	bst.insert(val)

## printing the BST
bst.traverse()

## reinitializing it
bst.clear()

'''
enter the number of values: 7
val: 5
val: 4
val: 6
val: 3
val: 8
val: 1
val: 7
BST representation
5 4 6 3 8 1 7 

re-initializing

'''