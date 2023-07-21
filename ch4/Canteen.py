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





a = input("Enter Input : ").split(",")
