class Node:
    def __init__(self, data) -> None:
        self.data =data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self.text = []
        
    def _insert(self, root, data):
        if root is None:
            # print("*")
            return Node(data)

        if data > root.data:
            root.right = self._insert(root.right, data)
            self.text.append("R")
            
        elif data < root.data:
            root.left = self._insert(root.left, data)
            self.text.append("L")
        return root
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

        self.text.reverse()       
        print("".join(self.text), end="")
        self.text = []
        print("*")
        return self.root
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)