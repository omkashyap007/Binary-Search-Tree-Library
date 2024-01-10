class NotBinarySearchTreeObjectOrNone(Exception):
    def __init__(self):
        super().__init__(self)
        self.message = "The Object is not BinarySearchTree object or its not None"