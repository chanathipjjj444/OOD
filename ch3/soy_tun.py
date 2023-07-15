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



print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
s = s.split(",")
new = [int(i) for i in s if int(i) != 0]
stack = Stack(new)


if o == "arrive":
    if len(new) == m:
        print(f"car {n} cannot arrive : Soi Full")
        
    elif n in new:
        print(f"car {n} already in soi")
    else:
        print(f"car {n} arrive! : Add Car {n}")
        stack.push(n)


if o == "depart":
    if len(new) == 0:
        print(f"car {n} cannot depart : Soi Empty")

    elif n not in new:
        print(f"car {n} cannot depart : Dont Have Car {n}")

    else:
        app = []
        while len(stack.items):
            if stack.items[-1] == n:
                print(f"car {n} depart ! : Car {n} was remove")
                stack.items.pop()
            else:
                app.append(stack.items.pop())
        app.reverse()
        stack.items.extend(app)
        
print(stack.items)
    
