class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    

def postFixeval(st):
    ops = "+-*/"
    s = Stack()

    for i in st:
        if i not in ops:
            s.push(i)

        else:
            opr2 = str(s.pop())
            opr1 = str(s.pop())
            s.push(eval(opr1+i+opr2))

    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))