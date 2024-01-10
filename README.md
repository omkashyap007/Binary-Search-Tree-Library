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

### Create Binary Search Tree from Sorted list.
You have to provide a sorted list which you will paas in the `createBSTFromSortedList` , the function will return a root of the Binary Search Tree created from the list .

```python

l = [11, 14, 36, 64, 69, 71, 83, 83] # sorted list.

root = createBSTFromSortedList(l)
print(root)

Output :

Sorted List : [11, 14, 36, 64, 69, 71, 83, 83]
        64
     __/  \__        
   14        71      
  /  \      /  \     
11    36  69    83   
                  \  
                   83

```
### Create Binary Search Tree With given Height .

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

## InOrder , PreOrder , PostOrder , LevelOrder Traversals .
There are two methods for traversals , one is class based which is specific to class and another is global method for bst.

```python
in_order = bst.inOrder()    # class method
in_order = inOrder(bst)     # global method
print(f"In Order :  {in_order}")

pre_order = bst.preOrder()    # class method
pre_order = preOrder(bst)     # global method
print(f"Pre Order :  {pre_order}")

post_order = bst.postOrder()    # class method
post_order = postOrder(bst)     # global method
print(f"Post Order :  {post_order}")

level_order = bst.levelOrder()    # class method
level_order = levelOrder(bst)     # global method
print(f"Level Order :  {level_order}")
```

```
Output :
In Order :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Pre Order :  [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]  
Post Order :  [1, 3, 2, 5, 7, 6, 4, 9, 11, 10, 13, 15, 14, 12, 8] 
Level Order :  [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
```

### List Level Order Traversal
This function gives the list  of all the levels of bst .

```
level_order_list = bst.levelOrderList()
level_order_list = levelOrderList(bst)
print(level_order_list)
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

Output :
              8
       ______/ \_____
      4              12
   __/ \_         __/  \__
  2      6      10        14
 / \    / \    /  \      /  \
1   3  5   7  9    11  13    15
```

### Printing the Binary Search Tree Horizontally Flipped .

You cannot use the print function , you have to use `printBTree()` with inverted parameter to be True

```python
printBTree(bst , inverted = True)

Output :

1   3  5   7  9    11  13    15
 \ /    \ /    \  /      \  /  
  2      6      10        14   
   ¯¯\ /¯         ¯¯\  /¯¯     
      4              12        
       ¯¯¯¯¯¯\ /¯¯¯¯¯
              8

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
### Delete Node in BST
Gives and new node with delete bst and also deletes from the actual one.
```python
new_bst = deleteNodeInBST(bst , 6)
print(new_bst)

Output :
           8
     _____/ \_____
    4             12
   / \         __/  \__
  2   5      10        14
 / \   \    /  \      /  \
1   3   7  9    11  13    15
```

### Distance of Node From Root
```python
distance = findDistanceFromRoot(bst , 7)
print(distance)

Output :
3
```

### Binary Search Tree to Doubly Linked List

```python
doubly_linked_list = bstToDLL(bst)
print(doubly_linked_list)

Output :
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15
```

### Linked List Enumeration
The function `enumerateLinkedList(doubly_linked_list)` is used to enumerate through the linked list . It gives three items in the tuple of list that is (index , node , node_data)
```python
new_bst = createBSTWithHeight(2)
# created new bst with height of 2 .
doubly_linked_list = bstToDLL(new_bst)
for index , node , data in enumerateLinkedList(doubly_linked_list) :
    print(f"index : {index} , node : {node} , node data : {data}")

Output :
index : 0 , node : LinkedListNode(data = 1 , prev = . , next = 2) , node data : 1
index : 1 , node : LinkedListNode(data = 2 , prev = 1 , next = 3) , node data : 2
index : 2 , node : LinkedListNode(data = 3 , prev = 2 , next = .) , node data : 3
```
### Serialization and Deserialization Of Binary Search Tree.

The library has `BSTSerializer` class which is used for Binary Tree Serialization and DeSerialization . 

There are two functions in the class `serialize()` which returns a string of serialied binary serach tree and `deSerialize()` which returns the root of the deSerialized Binary Search Tree .
```python

serializer = BSTSerializer()
serialized_string = serializer.serialize(bst)
print(f" Serialized BST String  : {serialized_string}") # serialized string
deserialized_bst = serializer.deSerialize(serialized_string) # root of the binary tree.

print(f"Deserialized Binary Search Tree ")
print(deserialized_bst)

Output :

Serialized BST String  : 8.4.2.1.N.N.3.N.N.6.5.N.N.7.N.N.12.10.9.N.N.11.N.N.14.13.N.N.15.N

Deserialized Binary Search Tree
              8
       ______/ \_____
      4              12
   __/ \_         __/  \__
  2      6      10        14
 / \    / \    /  \      /  \
1   3  5   7  9    11  13    15
```


There are more functions in the library to work with .

`isBST(root)` : The function checks whether the given tree is BST or not .
`bstSum` : The function gives the sum of all the values of the Binary Search Tree .
`diameterOfBST` : The function gives the biggest path of the tree or the diameter of the tree . 
`kThSmallestElement` : The function gives the kth smallest element in the bst .
`kThLargetElement` : The function gives the kth largest element in the bst. 
`findMinInBST` : The function gives the smallest node in BST.
`findMaxInBST` : The function gives the largest node in BST.
```python
is_bst = isBST(bst)
print(f"Is Bst : {is_bst}")
bst_sum = bstSum(bst)
print(bst)
print(f"Sum of nodes of the Binary Search Tree : {bst_sum}")

diameter_of_bst = diameterOfBST(bst)
print(f"Diameter of Binary Search Tree: {diameter_of_bst}")

kth_smallest = kThSmallestNode(bst , 6)
print(f"k'th smallest node in Binary Search Tree :\n{kth_smallest}")

kth_largest = kThLargestNode(bst , 4)
print(f"k'th largest node in Binary Search Tree: \n{kth_largest}")

min_element = findMinInBST(bst)
print(f"Minimum value in BST : \n{min_element}")

max_element = findMaxInBST(bst)
print(f"Maximum value in BST : \n{max_element}")
```

```python
Output :

Is Bst : True

Sum of nodes of the Binary Search Tree : 496

Diameter of Binary Search Tree: 8

k'th smallest node in Binary Search Tree :
  6
 / \
5   7

k'th largest node in Binary Search Tree:  
        28
     __/  \__
   26        30
  /  \      /  \
25    27  29    31

Minimum value in BST : 
1
Maximum value in BST : 
15

```