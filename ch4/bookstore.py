class Queue:
    def __init__(self, real):
        self.cashier1 = []
        self.cashier2 = []
        self.items = real

        self.sec = 0

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self, i):
        return i.pop(0)
    
    def isEmty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
user = input("Enter Input : ").split("/")
pre_add = user[1].split(",")


have = user[0].split(" ")
to_add = [i.split(" ") for i in pre_add]

have = Queue(have)
to_add = Queue(to_add)

for i in to_add.items:
    if i[0] == "E":
        have.enQueue(i[1])
    else:
        have.deQueue(have.items)
if len(set(have.items)) == len(have.items):
    print("NO Duplicate")
else:
    print("Duplicate")