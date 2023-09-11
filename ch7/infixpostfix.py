class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def postfix_to_tree(self, postfix):
        operand = "+-*/"
        emt = []
        
        for i in postfix:
            if i.isalpha():
                new_node = Node(i)
                emt.append(new_node)
            
            elif i in operand:
                head_node = Node(i)
                head_node.right = emt.pop()
                head_node.left = emt.pop()
                emt.append(head_node)
                
        return emt.pop()
    
    def inOrder(self, root):
        operand = "+-*/"
        if root is not None:
            if root.data in operand:
                print('(', end='')
            self.inOrder(root.left)
            print(root, end = "")
            self.inOrder(root.right)
            if root.data in operand:
                print(')', end='')
    
    def preOrder(self, root):

        if root is not None:
            

            print(root, end = "")
            self.preOrder(root.left)
            self.preOrder(root.right)



T = BST()

inp = [a for a in input("Enter Postfix : ")]
Ans_tree = T.postfix_to_tree(inp)

print("Tree :")
T.printTree(Ans_tree)
print("--------------------------------------------------")

print("Infix : ", end="")
T.inOrder(Ans_tree)
print()

print("Prefix : ", end="")
T.preOrder(Ans_tree)
print()
