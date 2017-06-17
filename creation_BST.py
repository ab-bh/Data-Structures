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
			print "root!"
			self.root = Node(val)
		else:
			root = self.root
			while True:
				if val<root.data:
					if not root.left:
						print "left",
						root.left = Node(val);break
					else:
						print "left",
						root = root.left
				else:
					if not root.right:
						print "right",
						root.right = Node(val);break
					else:
						print "right",
						root = root.right
	def insert_recursive(self,root,val):
		if root == None:
			return Node(val)
		else:
			if val<root.data:
				node = self.insert_recursive(root.left, val)
				root.left  = node
			else:
				node = self.insert_recursive(root.right, val)
				root.right  = node


	def traverse(self): ## level order traversals 
		nodes = []
		nodes.append(self.root)
		print "\nBST representation"
		while nodes:
			current = nodes.pop(0)
			print current.data,
			if current.left:
				nodes.append(current.left)
			if current.right:
				nodes.append(current.right)

	def find_max(self):
		if self.root is None:
			return None
		else:
			current = self.root
			while True:
				if current.right is not None:
					current = current.right
				else:
					break
			return current.data

	def find_min(self):
		if self.root is None:
			return None
		else:
			current = self.root
			while True:
				if current.left is not None:
					current = current.left
				else:
					break
			return current.data
	
	def clear(self):
		print "\n\nre-initializing\n"
		self.__init__()

## creating an instance for the BST
bst = BST()
root = None
for tc in xrange(input("enter the number of values: ")):
	val = input("\nval: ")
	## for iterative approach
	print "the node insertion path(from root): ",
	bst.insert(val)
## printing the BST
bst.traverse()

print "\n"

## displaying the max of the BST
print "max: ",bst.find_max()

## displaying the min of the BST
print "min: ",bst.find_min()

## reinitializing it
bst.clear()




'''
enter the number of values: 7

val: 5
the node insertion path(from root):  root!

val: 4
the node insertion path(from root):  left 
val: 6
the node insertion path(from root):  right 
val: 1
the node insertion path(from root):  left left 
val: 7
the node insertion path(from root):  right right 
val: 3
the node insertion path(from root):  left left right 
val: 8
the node insertion path(from root):  right right right 
BST representation
5 4 6 1 7 3 8 

max: 8
min: 1

re-initializing


'''
