
class Queue:
    def __init__(self, real):
        self.insertlist = real
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        self.items.pop(0)
    
    def isEmty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def operate(self):
        for i in self.insertlist:
            if i[0] == "E":
                self.items.append(i[1])
                print(len(self.items))
            else:
                try:
                    print(f"{self.items[0]} {self.items.index(self.items[0])}")
                    self.deQueue()
                except:
                    print(-1)

        if len(self.items) > 0:
            for i in range(len(self.items)):
                print(self.items[i], end= " ")
        else:
            print("Empty")


a = input("Enter Input : ").split(",")
b = [i.split(" ") for i in a]

real = Queue(b)
real.operate()
