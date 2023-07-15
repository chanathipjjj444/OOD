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

    def ManageStack(self):
        a = input("Enter Input : ").split(",")
        b = []
        for i in a:
            b.append(i.split(" "))

        self.stack = []


        for i in b:
            if i[0] == "A":
                self.stack.append(int(i[1]))
                print(f"Add = {i[1]}")


            if i[0] == "P":
                if len(self.stack) != 0:
                    print("Pop =",self.stack.pop())
                else:
                    print("-1")



            if i[0] == "D" or i[0] =="LD" or i[0] == "MD":
                if len(self.stack) == 0:
                    print("-1")
                self.app = []
            



            if i[0] == "D":
                while len(self.stack):
                    if int(self.stack[-1]) == int(i[1]):
                        print(f"Delete = {i[1]}")
                        self.stack.pop()
                    else:
                        self.app.append(int(self.stack.pop()))
                self.app.reverse()
                self.stack = [int(i) for i in self.app]
                self.app = []
                

            if i[0] == "LD":
                while len(self.stack):
                    if int(self.stack[-1]) < int(i[1]):
                        print(f"Delete = {self.stack[-1]} Because {self.stack[-1]} is less than {i[1]}")
                        self.stack.pop()
                    else:
                        self.app.append(int(self.stack.pop()))
                self.app.reverse()
                self.stack = [int(i) for i in self.app]
                self.app = []

            if i[0] == "MD":
                while len(self.stack):
                    if int(self.stack[-1]) > int(i[1]):
                        print(f"Delete = {self.stack[-1]} Because {self.stack[-1]} is more than {i[-1]}")
                        self.stack.pop()
                    else:
                        self.app.append(int(self.stack.pop()))
                self.app.reverse()
                self.stack = [int(i) for i in self.app]
                self.app = []
        
        print(f"Value in Stack = {self.stack}")
            
c = Stack()
c.ManageStack()