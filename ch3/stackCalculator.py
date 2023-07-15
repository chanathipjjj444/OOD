class StackCalc:
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
    
    def run(self, st):
        ops = "+-*/"
        extras = ["DUP", "POP", "PSH"]
        self.s = StackCalc()
        for i in st:
            try:
                if i not in ops and i not in extras:
                    int(i)
            except:
                print(f"Invalid instruction: {i}")
                quit()
            if i in ops:
                opr1 = str(self.s.pop())
                opr2 = str(self.s.pop())
                self.s.push(int(eval(opr1+i+opr2)))          
            elif i in extras:
                if i == "DUP":
                    to_push = self.s.items[-1]
                    self.s.push(to_push)

                elif i == "POP":
                    self.s.pop()

                elif i == "PSH":
                    pass
            else:
                self.s.push(i)

    def getValue(self):
        if len(self.s.items) == 0:
            return 0
        return self.s.pop()

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
