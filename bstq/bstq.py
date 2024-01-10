import random
from collections import deque
from collections import deque
import functools as fn

class NotBinarySearchTreeObjectOrNone(Exception):
    def __init__(self):
        super().__init__(self)
        self.message = "The Object is not BinarySearchTree object or its not None"

def inOrder(node):
    """
    Returns the InOrder traversal of the binary tree .
    Take root as an input for the traversal

    eg : 
    in_order = inOrder(root)
    """
    root = node
    stack = []
    in_order = []
    while root or stack :
        if root :
            stack.append(root)
            root = root.left
        else :
            root = stack.pop()
            in_order.append(root.data)
            root = root.right
    del root
    del stack
    return in_order

def postOrder(self):
    """
    Returns the PostOrder traversal of the binary tree .
    Take root as an input for the traversal

    eg : 
    post_order = postOrder(root)
    """
    root = self
    stack = []
    post_order = []
    while stack or root :
        if root :
            stack.append((root , 1))
            root = root.left
        else :
            root , times = stack.pop()
            if times == 1 :
                stack.append((root , 2))
                root = root.right
            if times == 2 :
                post_order.append(root.data)
                root = None
    del stack
    del root
    return post_order

def preOrder(self):
    """
    Returns the PreOrder traversal of the binary tree .
    Take root as an input for the traversal

    eg : 
    pre_order = preOrder(root)
    """
    root = self
    stack = []
    pre_order = []
    while stack or root :
        if root : 
            pre_order.append(root.data)
            stack.append(root)
            root = root.left
        else :
            root = stack.pop().right
    del root
    del stack
    return pre_order

def height( root):
    """
    Returns the height of the binary tree . Finds out the maximum height from each side and get the largest height of the tree .
    
    takes root as an input 

    eg :
    tree_height = height(root)
    """
    if not root or (not root.right and not root.left):
        return 0
    return 1 + max(height(root.left), height(root.right))

def fillMatrix( matrix, root, r, c, height):
    if not root:
        return
    matrix[r][c] = str(root.data)
    fillMatrix(
        matrix, root.left, r + 1, c - 2 ** (height - r - 1), height
    )
    fillMatrix(
        matrix, root.right, r + 1, c + 2 ** (height - r - 1), height
    )

def getTreeMatrix( root):
    """
    Returns a matrix representing the binary tree .

    takes root as an input 

    eg :
    matrix = getTreeMatrix(root)
    """
    h = height(root)
    ROWS = h + 1
    COLS = 2**ROWS - 1
    matrix = [["" for _ in range(COLS)] for _ in range(ROWS)]
    r = 0
    c = (COLS - 1) // 2
    fillMatrix(matrix, root, r, c, h)
    return matrix

def printBTree(node, nodeInfo=None, inverted=False , isTop=True):
   """
   Prints the binary tree in form of a binary tree .

   takes root as input 

   eg : printBTree(root)

   reference : https://stackoverflow.com/a/49844237
   """
   nodeInfo = lambda node : (str(node.data) , node.left , node.right)   
   stringValue, leftNode, rightNode = nodeInfo(node)
   stringValueWidth  = len(stringValue)
   leftTextBlock     = [] if not leftNode else printBTree(leftNode,nodeInfo,inverted,False)
   rightTextBlock    = [] if not rightNode else printBTree(rightNode,nodeInfo,inverted,False)
   commonLines       = min(len(leftTextBlock),len(rightTextBlock))
   subLevelLines     = max(len(rightTextBlock),len(leftTextBlock))
   leftSubLines      = leftTextBlock  + [""] *  (subLevelLines - len(leftTextBlock))
   rightSubLines     = rightTextBlock + [""] *  (subLevelLines - len(rightTextBlock))
   leftLineWidths    = [ len(line) for line in leftSubLines  ]                            
   rightLineIndents  = [ len(line)-len(line.lstrip(" ")) for line in rightSubLines ]
   firstLeftWidth    = (leftLineWidths   + [0])[0]  
   firstRightIndent  = (rightLineIndents + [0])[0]
   linkSpacing       = min(stringValueWidth, 2 - stringValueWidth % 2)
   leftLinkBar       = 1 if leftNode  else 0
   rightLinkBar      = 1 if rightNode else 0
   minLinkWidth      = leftLinkBar + linkSpacing + rightLinkBar
   valueOffset       = (stringValueWidth - linkSpacing) //2
   minSpacing        = 2
   rightNodePosition = fn.reduce(lambda r,i: max(r,i[0] + minSpacing + firstRightIndent - i[1]), \
                                 zip(leftLineWidths,rightLineIndents[0:commonLines]), \
                                 firstLeftWidth + minLinkWidth)
   linkExtraWidth    = max(0, rightNodePosition - firstLeftWidth - minLinkWidth )
   rightLinkExtra    = linkExtraWidth // 2
   leftLinkExtra     = linkExtraWidth - rightLinkExtra
   valueIndent       = max(0, firstLeftWidth + leftLinkExtra + leftLinkBar - valueOffset)
   valueLine         = " " * max(0,valueIndent) + stringValue
   slash             = "\\" if inverted else  "/"
   backslash         = "/" if inverted else  "\\"
   uLine             = "¯" if inverted else  "_"
   leftLink          = "" if not leftNode else ( " " * firstLeftWidth + uLine * leftLinkExtra + slash)
   rightLinkOffset   = linkSpacing + valueOffset * (1 - leftLinkBar)
   rightLink         = "" if not rightNode else ( " " * rightLinkOffset + backslash + uLine * rightLinkExtra )
   linkLine          = leftLink + rightLink
   leftIndentWidth   = max(0,firstRightIndent - rightNodePosition) 
   leftIndent        = " " * leftIndentWidth
   indentedLeftLines = [ (leftIndent if line else "") + line for line in leftSubLines ]
   mergeOffsets      = [ len(line) for line in indentedLeftLines ]
   mergeOffsets      = [ leftIndentWidth + rightNodePosition - firstRightIndent - w for w in mergeOffsets ]
   mergeOffsets      = [ p if rightSubLines[i] else 0 for i,p in enumerate(mergeOffsets) ]
   mergedSubLines    = zip(range(len(mergeOffsets)), mergeOffsets, indentedLeftLines)
   mergedSubLines    = [ (i,p,line + (" " * max(0,p)) )       for i,p,line in mergedSubLines ]
   mergedSubLines    = [ line + rightSubLines[i][max(0,-p):]  for i,p,line in mergedSubLines ]
   treeLines = [leftIndent + valueLine] + ( [] if not linkLine else [leftIndent + linkLine] ) + mergedSubLines
   # invert final result if requested
   treeLines = reversed(treeLines) if inverted and isTop else treeLines

   # return intermediate tree lines or print final result
   if isTop :return "\n".join(treeLines)
   else     : return treeLines
   
def isBST(root):
    """
    Return boolean telling that is it a binary tree .

    takes binary tree root as an input 

    isBinarySearchTree = isBST(root)
    """
    stack = []
    inOrderList = []
    while root or stack :
        if root :
            stack.append(root)
            root = root.left
        else :
            root = stack.pop()
            if inOrderList:
                if inOrderList[-1] >= root.data :
                    return False
            inOrderList.append(root.data)
            root = root.right
    return True

def invertBST(root):
    """
    Returns a node which represents the inverted form of the binary tree

    takes root as an input 

    eg :
    inverted_bst = invertBST(root)
    """
    if not root :
        return root
    root.left , root.right = root.right , root.left
    invertBST(root.left)
    invertBST(root.right)
    return root

def bstSum(root):
    """
    Returns the sum of the binary search tree

    takes root as an input 

    eg :
    bst_sum = bstSum(root)
    """
    if not root :
        return  0
    val = root.data + bstSum(root.left) + bstSum(root.right)
    return val

def searchInBST(root , data):
    """
    Returns the node which you want to search , if the node is not present it returns None

    takes root and value which you want to search as an input

    eg :
    node_found = serachInBST(root , data = 10)
    """
    if not root :
        return None
    if root.data == data :
        return root
    elif root.data > data :
        return  searchInBST(root.left , data)
    else :
        return searchInBST(root.right , data)
    return None

def diameterOfBST(root):
    """
    Returns the maximum length of the diameter of the tree .

    takes root as input 

    eg : 
    diameter = diameterOfBST(root)
    """
    answer = [0]
    dBST(root , answer )
    return answer[0]

def dBST(root , answer):
    if not root :
        return 0
    if not root.left and not root.right :
        return 0
    left = 0
    if root.left :
        left = 1 + dBST(root.left , answer )
    right = 0
    if root.right :
        right = 1 + dBST(root.right , answer)
    answer[0] = max(left+right , answer[0])
    return max(left , right)

def topViewOfBST(root):
    """
    Returns the list which represents top view of the binary search tree.

    takes root as an input

    eg :
    top_view = topViewOfBST(root)
    """
    if not root :
        return []
    queue = deque([(root , 0)])
    hash_map = {0 : root.data}
    while queue :
        node , distance  = queue.popleft()
        if node.left :
            dist = distance-1
            if dist not in hash_map :
                hash_map[dist] = node.left.data
            queue.append((node.left , dist))
        if node.right :
            dist = distance + 1
            if dist not in hash_map : 
                hash_map[dist] = node.right.data
            queue.append((node.right , dist))
    values = list(zip(hash_map.keys() , hash_map.values()))
    values.sort(key = lambda x : x[0] )
    return [i[1] for i in values]

def getRightMostNode(root):
    while root.right :
        root = root.right
    return root

def getNewTreeAfterDeletion(left_subtree , right_subtree):
    right_most_of_left = getRightMostNode(left_subtree)
    right_most_of_left.right = right_subtree
    return left_subtree

def getUpdatedTree(node):
    if not node.left and not node.right :
        return None
    elif node.left and node.right :
        return getNewTreeAfterDeletion(node.left ,  node.right)
    else :
        return node.left if node.left else node.right

def deleteNodeInBST(root , key):
    """
    Returns a new refernce node after deleting the node with the provided key .

    takes root and the key of the node you want to delete .

    eg :
    new_node = deleteNodeInBST(root , key)
    """
    if not root :
        return None
    changed = False
    if root.data == key :
        root = getUpdatedTree(root)
        changed = True
    node = root
    while node and not changed:
        if node.left and node.left.data == key :
            node.left = getUpdatedTree(node.left)
            break
        if node.right and node.right.data ==  key :
            node.right = getUpdatedTree(node.right)
            break
        if node.data > key :
            node = node.left
        else :
            node = node.right
    return root

def levelOrder(root):
    """
    Returns a list of values which represent the level order traversal of the binary search tree .

    takes root as the input for the traversal

    eg :
    level_order = levelOrder(root)
    """
    queue = deque([root])
    level_order = []
    while queue :
        node = queue.popleft()
        level_order.append(node.data)
        queue.append(node.left) if node.left else None
        queue.append(node.right) if node.right else None
    del queue
    return level_order

def levelOrderList(root):
    """
    Returns a list of list of each level in the binary serach tree .

    takes root as an input

    eg :
    level_order_list = levelOrderList(root)
    """
    queue = deque([root])
    level_order_list = []
    while queue :
        temp_queue = []
        level_list = []
        for node in queue :
            level_list.append(node.data)
            temp_queue.append(node.left) if node.left else None
            temp_queue.append(node.right) if node.right else None
        queue = temp_queue
        level_order_list.append(level_list)
        del level_list
    return level_order_list

def findDistanceFromRoot(root , value) :
    """
    Returns the distance of the node from the root node if the node is found else returns -1.

    takes root and a value of the node you want to find the distance for

    eg :
    dist = findDistanceFromRoot(root , value)
    """
    if not root : 
        return -1
    distance = -1
    if root.data == value :
        return distance + 1
    else : 
        distance = findDistanceFromRoot(root.left , value)
        if distance >= 0 :
            return distance + 1
        else : 
            distance =  findDistanceFromRoot(root.right, value)
            if distance >= 0 : 
                return distance + 1
    return distance

class LinkedListNode(object):
    def __init__(self , data , next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"""LinkedListNode(data = {self.data} , prev = {self.prev.data if self.prev else "."} , next = {self.next.data if self.next else "."})"""
    
    def __repr__(self):
        return f"""LinkedListNode(data = {self.data} , prev = {self.prev.data if self.prev else "."} , next = {self.next.data if self.next else "."})"""

def enumerateLinkedList(ll ,  start = 0):
    """
    Custom Enumerate function which gives (index , node , node_data) at each iteration of the linked list .

    takes linked_list for the traversal and an optional argument start which tells the start index , default value is 0 .

    eg :
    enumerated_list = enumearteLinkedList(doubly_linked_list)

    output :
    [(0 , LinkedListNode(data = 10 , next = 11 , prev = 9) , 10) , .... ]
    """
    head = ll.head
    while head :
        yield (start , head , head.data)
        start += 1
        head = head.next

class LinkedList(object):
    """
    This is the Linked List object in which the tree will be converted to .
    """

    def __init__(self ,  data = None ):
        self.head = None
        self.tail = None
        self.length = 0
        if data != None: 
            node = LinkedListNode(data)
            self.head = node
            self.tail = node
            self.length += 1

    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next

    def __len__(self):
        return self.length
    
    def __str__(self):
        a = self.__iter__()
        l = [str(i.data) for i in a]
        return " -> ".join(l)

    def addAtTail(self , data):
        node = LinkedListNode(data)
        if not self.head :
            self.head = node
            self.tail = node
            self.length += 1
        else :
            tail = self.tail
            tail.next = node
            self.tail = node
            self.tail.prev = tail
            self.length += 1
        
    def createFromList(self ,  l):
        if not l :
            return
        node = LinkedListNode(l[0])
        self.head = node
        self.tail = node
        for i in range(1 , len(l)):
            self.addAtTail(l[i])

    def printList(self):
        head = self.head
        while head :
            print(f"{head.prev.data if head.prev else ''} : {head.data} : {head.next.data if head.next else ''}")
            head = head.next

def bstToDLL(root):
    """
    Creates a Doubly Linked List from the InOrder traversal of the binary tree root .

    takes root as an input 

    eg :
    doubly_linked_list = bstToDLL(root)
    """
    in_order = inOrder(root)
    l = LinkedList()
    l.createFromList(in_order)
    return l

def kThSmallestNode(root , k):
    stack = []
    n = 0
    while stack or root :
        if root :
            stack.append(root)
            root = root.left
        else :
            root = stack.pop()
            n += 1
            if n == k :
                return root
            root = root.right
    return None

def kThLargestNode(root , k):
    stack = []
    n = 0
    while stack or root :
        if root :
            stack.append(root)
            root = root.right
        else :
            root = stack.pop()
            n += 1
            if n == k :
                return root
            root = root.left
    return None
#--------------------------------------------------------------------------------
def isBSTObjectOrNone(node):
    """
    Returns a boolean which tells that the current object is BinarySearchTree object or None or not .

    takes root as the input 

    isNode = isBSTObjectOrNone(root)
    """
    if isinstance(node , BinarySearchTree) or node == None :
        return True
    return False

def createNotBinarySearchTreeOrNoneExceptionForLeftNode(node):
    e = NotBinarySearchTreeObjectOrNone()
    e.add_note("The Left Object you passed is not BinarySearchTree object or its not None")
    return e

def createNotBinarySearchTreeOrNoneExceptionForRightNode(node):
    e = NotBinarySearchTreeObjectOrNone()
    e.add_note("The Right Object you passed is not BinarySearchTree object or its not None")
    return e

def raiseException(exception) :
    raise exception

def bstFromSortedList(l , left , right):
    if left > right:
        return None
    mid = (left + right)//2 
    root = BinarySearchTree(l[mid])
    root.left = bstFromSortedList(l , left , mid -1)
    root.right = bstFromSortedList(l , mid+1 , right)
    return root

def createBSTFromSortedList(l):
    """
    Returns the root of the tree which has been created from the sorted list .

    The user (you) have to provide a sorted list . 
    
    takes sorted list l as an input 

    eg :
    root = createBSTFromSortedList(l)
    """
    a = l.copy()
    if len(a) == 0 :
        return None
    root = bstFromSortedList(a , 0 , len(a)-1)
    return root

def createBSTWithHeight(height = 3):
    """
    Returns a Binary tree root of given height .

    takes height as an input , default value is 3 .

    eg : 
    root = createBSTWithHeight(5)
    """
    l = [i for i in range(1 , 2**height)]
    root = createBSTFromSortedList(l)
    return root

def findMinInBST(root):
    """
    Return the node with the minimum value in the tree .

    takes root as an input 

    eg :
    node = findMinInBST(root)
    """
    while root :
        if root.left :
            root = root.left
        else :
            break
    return root

def findMaxInBST(root):
    """
    Returns the node with the maximum value in the Binary tree .

    takes root as an input

    node = findMaxInBST(root)
    """
    while root :
        if root.right :
            root = root.right
        else :
            break
    return root

class BSTSerializer:
    """
    This class is used to serialize and deserialize the binary tree .
    serializeBST(root) and deserializeBST(string) are two functions which are used to serialize and deserialize the binary tree .

    The serializeBST function serializes the binary tree into a pre_order traversal string representing the string .

    In PreOrder traversal root comes first then the left node then the right node .

    pre order = (root , left , right)

    to serialize and deserialize use the following function .

    # for serialization 
    
    serializer = BSTSerializer()
    serialized_tree_string = serializer.serializeBST(root)

    # for deserialization

    serializer = BSTSerializer()
    tree_from_string = serializer.deSerializeBST(string)

    """
    def serialize(self , root):
        """
        Returns a string of serialized binary tree .

        takes root as the input for the serialization

        eg :
        serializer = BSTSerializer()
        serialized_string = serializer.serializeBST(root)
        """
        stack = []
        serialize_pre_order = []
        while root or stack :
            if root :
                serialize_pre_order.append(str(root.data))
                stack.append(root)
                root = root.left
            else : 
                root = stack.pop()
                serialize_pre_order.append("N")
                root = root.right
        serialize_pre_order = ".".join(serialize_pre_order)
        return serialize_pre_order
    
    def createRoot(self , l):
        if self.index >= len(l) or l[self.index] == "N" :
            self.index += 1
            return None
        root = BinarySearchTree(int(l[self.index]))
        self.index += 1
        root.left = self.createRoot(l)
        root.right = self.createRoot(l)
        return root
    
    def deSerialize(self , string):
        """
        Returns the binary tree root of the serialized string .

        takes string as the input for the serialization

        eg :
        serializer = BSTSerializer()
        serialized_string = serializer.deSerializeBST(string)
        """
        l = string.split(".")
        self.index = 0
        root = self.createRoot(l)
        self.index = 0
        return root

class BinarySearchTree:
    """
    Creates a Binary Search Tree object , takes a value for the instanciation .

    takes a node value for the instanciation .

    eg :
    root = BinarySearchTree(10)
    """

    def __init__(self , data , left = None, right = None) :
        self.data = data
        if not isBSTObjectOrNone(left):
            e = createNotBinarySearchTreeOrNoneExceptionForLeftNode(left)
            raise e
        self.left = left
        if not isBSTObjectOrNone(right):
            e = createNotBinarySearchTreeOrNoneExceptionForRightNode(right)
            raise e
        self.right = right

    def insertNode(self , data) :
        if self.data == data :
            return
        elif self.data > data :
            if self.left == None :
                self.left = BinarySearchTree(data)
            else :
                self.left.insertNode(data)
        else:
            if self.right == None :
                self.right = BinarySearchTree(data)
            else :
                self.right.insertNode(data)
        return
    
    def inOrder(self):
        return inOrder(self)

    def postOrder(self):
        return postOrder(self)

    def preOrder(self):
        return preOrder(self)

    def levelOrder(self):
        return levelOrder(self)
    
    def levelOrderList(self):
        return levelOrderList(self)

    def searchInBST(self , data):
        return searchInBST(self , data)

    def height(self):
        return height(self)

    def __str__(self , inverted = False):
        return printBTree(self , inverted = inverted)

# a = BinarySearchTree(50)
# a.left = BinarySearchTree(8)
# a.right = BinarySearchTree(12)
# a.left.left = BinarySearchTree(6)
# a.left.right = BinarySearchTree(9)
# a.right.left = BinarySearchTree(11)
# a.right.right = BinarySearchTree(13)
# in_order = a.inOrder()
# print(in_order)
# post_order = a.postOrder()
# print(post_order)
# pre_order = a.preOrder()
# print(pre_order)
# l = [i+1 for i in range(63)]
# node = bstFromSortedList(l)
# print(node)
# print()
# print(bstSum(node))
# print(node.inOrder())
# print(node.levelOrder())
# node.left = BinarySearchTree(10000)
# for i in node.levelOrderList():
#     print(i)
# print(isBST(node))
# print(node)
# invertBST(node)
# print(node)
node = createBSTWithHeight(5)
# print(node)
# the_min = findMinInBST(node)
# print(the_min)
# print(node)
# s = Serialization()
# ser = s.serializeBST(node)
# print(ser)
# deser = s.deSerializeBST(ser)
# print(deser)
# print(deser.search(100))
# print(diameterOfBST(deser))
# print(topViewOfBST(deser))
# node = deleteNodeInBST(node , 8)
# print(node)
# dist = findDistanceFromRoot(node , 10)
# print(dist)
# dll = bstToDLL(node)
# for index , node , data in enumerateLinkedList(dll):
#     print(index)
#     print(node.prev if node.prev else "ille")
# print(node)
# print(kThSmallestNode(node , 10))
# print(kThLargetElement(node , 5))
