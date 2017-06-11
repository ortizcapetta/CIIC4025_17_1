from binarytree import Node, setup, tree, pprint, inspect, convert
from collections import Counter
import random

my_null = None


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = None


    def color_node(self, color):
        self.color = color

    def inspect(self):
        return inspect(self)

setup(
    node_init_func=lambda v: Node(v),
    node_class=Node,
    null_value=my_null,
    value_attr='value',
    left_attr='left',
    right_attr='right'

)



def TreeSearch(k,v): #TreeSearch algorithm as discussed in class

    if v.right == None and v.left == None:
        return v
    if k == v.value:
        return v
    elif k < v.value:
        if(v.left!=None):
            return TreeSearch(k,v.left)
        else:
            return v
    else:
        if(v.right!=None):
            return TreeSearch(k,v.right)
        else:
            return v


def insert(k,v):   # insertion algorithm for BST as discussed in class
    w = TreeSearch(k,v)
    if(w.value > k):
        w.left = Node(k)
    else:
        w.right = Node(k)


def height(v):  # determine height of a node
    if v is None:
        return -1
    return max(height(v.left), height(v.right)) + 1


def maxdepth(root, depth=-1): #maximum depth of the tree
    if root is None:
        return depth
    return max(maxdepth(root.left, depth+1),maxdepth(root.right, depth+1))
# note: max depth should be the same as the height of the root


def isAVL(root):  # verifies if the BST is AVL
    if root is None:
        return True
    left = height(root.left)
    right = height(root.right)
    if abs(left-right) >1:
        return False;
    else:
        return isAVL(root.left) and isAVL(root.right)

def color_black(node):
    if node is not None:
        node.color_node('Black')
        color_children(node.left,node.right)

def color_red(node):
    node.color_node('Red')
    color_children(node.left,node.right)

def color_children(l,r):
    if height(l) < height (r) or height(l) %2!=0:
        color_black(l)
    else:
        color_red(l)
    if height(r) < height(l) or height(r)%2 != 0:
        color_black(r)
    else:
        color_red(r)



def isRedBlack(root):
    if blackheight(root)>0:
        return True
    else:
        return False


def blackheight(root):
    if root is None:
        return 1
    lbh = blackheight(root.left)
    if(lbh ==0):
        return lbh
    rbh = blackheight(root.right)
    if(rbh==0):
        return rbh
    if(rbh != lbh):
        return 0
    else:
        return lbh + isBlack(root)

def isBlack(node):
    if node.color == 'Black':
        return 1
    else:
        return 0


rand_arr = random.sample(range(100), 16)
print(rand_arr)
root = Node(rand_arr[0])
for x in rand_arr[1:16]:
    insert(x, root)
pprint(root)
print(root.inspect())
print(isAVL(root))
list = [87, 43, 44, 42, 23, 90, 24, 82, 76, 91, 71, 27, 89, 0, 48]
my_tree = Node(31)
for x in list[0:15]:
    insert(x, my_tree)
pprint(my_tree)
print("Height",height(my_tree))
print("Max Depth", maxdepth(my_tree))
print("Is AVL?", isAVL(my_tree))
color_black(my_tree)
print("Black height, if valid?", blackheight(my_tree))

height_dis = []
AVL_dis = []
RB_dis = []
for x in range(1000, 1500, 10):
    arr = []
    for y in range(0, x):
        rand = random.sample(range(1500), x)
        arr.append(rand)
    bin_tree = Node(arr[0])
    for z in arr[0:x - 1]:
        insert(z, bin_tree)
    color_black(bin_tree)
    RB_dis.append(isRedBlack(bin_tree))
    AVL_dis.append(isAVL(bin_tree))
    height_dis.append(height(bin_tree))

    height_count = Counter(height_dis)
    AVL_count = Counter(AVL_dis)
    RB_count = Counter(RB_dis)
    print("calculations with ",x, " nodes")
    print('Distribution of heights:')
    print(height_count)
    print('isAVL: ')
    print(AVL_count)
    print('isRB: ')
    print(RB_count)
print("done")




