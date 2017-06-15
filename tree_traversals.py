def preOrder(node,len_tree,tree):
	if node > len_tree:
		return
	print tree[node],
	preOrder(2*node, len_tree, tree)
	preOrder(2*node+1, len_tree, tree)

def postOrder(node,len_tree,tree):
	if node > len_tree:
		return 
	postOrder(2*node, len_tree, tree)
	postOrder(2*node+1, len_tree, tree)
	print tree[node],

def inOrder(node,len_tree,tree):
	if node > len_tree:
		return 
	inOrder(2*node, len_tree, tree)
	print tree[node],
	inOrder(2*node+1, len_tree, tree)


## make a example tree to demonstrate the working 
tree = map(int,raw_input().split())
len_tree = len(tree)

## using the 1 indexing 
tree = [-1]+tree

## calling the tree traversal function
print "\npreOrder: ",preOrder(1, len_tree, tree)

print "\npostOrder: ",postOrder(1, len_tree, tree)

print "\ninOrder: ",inOrder(1, len_tree, tree)

'''
input:

1 2 3 4 5 

output

preOrder:  1 2 4 5 3 

postOrder:  4 5 2 3 1 

inOrder:  4 2 5 1 3 

'''