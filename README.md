# BSTq

BSTq is a comprehensive Python library dedicated to Binary Search Trees (BSTs). Designed to work with BSTs, this library offers a wide array of functions and utilities, rather than basic functions to work with binary search trees effortlessly. 

This library has lots of functions which can be used to minimize your efforts for Binary Search Trees .
## Install
```
pip install bstq
```

## Usage
```
from bstq import *
```

### Creating Binary Search Tree

The following class is used to create a BinarySearchTree and instanciate a tree object with root value  of 10 .
```python

class BinarySearchTree:
    def __init__(self , data , left = None, right = None) :
        self.data = data
        self.left = left
        self.right = right
        
root = BinarySearchTree(10)
```
Let's start with a binary tree .
You can use `createBSTWithHeight` function to create BST with given height.

```
bst = createBSTWithHeight(4)
print(bst)
```
```
Output :
              8
       ______/ \_____
      4              12
   __/ \_         __/  \__
  2      6      10        14
 / \    / \    /  \      /  \
1   3  5   7  9    11  13    15

```

## Inorder Traversal 
There are two methods for traversals , one is class based which is specific to class and another is global method for bst.

```python
in_order = bst.inOrder()    # class method
in_order = inOrder(bst)     # global method

print(in_order)
```

```
Output :
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```
Similarly we have `preOrder` , `postOrder` , `levelOrder` traversals .

### List Level Order Traversal
This function gives the list of all the levels of bst .

```
level_order_list = bst.levelOrderList()
```

```
Output :
[[8], [4, 12], [2, 6, 10, 14], [1, 3, 5, 7, 9, 11, 13, 15]]
```

### Search in bst
```python
node = searchInBST(bst , 6)
node = bst.searchInBST(6)
print(node)

Ouput :
  6
 / \
5   7
```

### Height of bst

```python
h = bst.height()
h = height(bst)

Output :
4
```

### Printing Binary Tree
You'll get the most prettiest display of Binary Search Tree .
```
printBTree(bst) # global function
print(bst)      # you can also use print function directly .

              8
       ______/ \_____
      4              12
   __/ \_         __/  \__
  2      6      10        14
 / \    / \    /  \      /  \
1   3  5   7  9    11  13    15
```

### Invert BST
Invertes the binary search tree to its mirror image .
```python
inverted_tree = invertBST(bst)
print(inverted_tree)

                 8
          ______/ \______
        12               4
     __/  \__         __/ \_
   14        10      6      2
  /  \      /  \    / \    / \
15    13  11    9  7   5  3   1
```
### Top View of BST
```python
top_view = topViewOfBST(bst)
print(top_view)

Output :
[1, 2, 4, 8, 12, 14, 15]
```