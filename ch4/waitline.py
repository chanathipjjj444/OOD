class Cashier:
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
    






a = input("Enter people and time : ").split(" ")
time = int(a[1])
b = [i for i in a[0]]
queue = Cashier(b)
while queue.sec < time:
    queue.sec += 1
    # print(f"checkmod {queue.sec - 9}")
    if (queue.sec - 1) % 3 == 0 and (queue.sec - 1) > 0:
        queue.deQueue(queue.cashier1)
    if (queue.sec) >= 10 and (queue.sec) % 2 == 0:
        queue.deQueue(queue.cashier2)
    if len(queue.items) > 0:
        if len(queue.cashier1) < 5:
            queue.cashier1.append(queue.deQueue(queue.items))
        else:
            queue.cashier2.append(queue.deQueue(queue.items))
    print(f"{queue.sec} {queue.items} {queue.cashier1} {queue.cashier2}")