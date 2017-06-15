## For a binary search tree calculating height

class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height_(root):
    if root == None:return 0
    else:
        max_left_subtree_height = height_(root.left)      
        max_right_subtree_height = height_(root.right)
        max_height = max(max_left_subtree_height, max_right_subtree_height)+1
        return max_height

## height of the first node is 0 not 1
def height(root):
    depth  = height_(root)
    return (depth-1)

tree = BinarySearchTree()
t = int(raw_input())

for _ in xrange(t):
    x = int(raw_input())
    tree.create(x)

print height(tree.root)


'''
input:
5                   1
1                    \
2                     2
3                      \
4                       3
5                        \
                          4
                           \
                            5


output:
4

'''
