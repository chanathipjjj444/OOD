class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self.size = 0
        
    def __str__(self) -> str:
        p, emtl = self.head, []
        while p.next is not None:
            emtl.append(str(p.next.data))
            p = p.next
        emtl = "->".join(emtl)
        return emtl

    def __len__(self):
        return self.size

    def append(self,data):
        node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def insert(self, i:int,data):
        # print("index = " + i + " and " + "data = " + data)
        node = Node(data)
        cur = self.head
        for _ in range(i):
            if cur.next is not None:
                cur = cur.next
        node.next = cur.next
        cur.next = node
        self.size += 1

inp = input("Enter Input : ").split(",")
for item in inp:
    item = item.split()


def solver(data):
    l1 = LinkedList()
    new_data = []
    initial = data.pop(0).split()
    for i in data:
        new_data.append(i.strip())
    data = new_data
    
    if len(initial) == 0 :
        print("List is empty")
    else:
        for i in initial:
            l1.append(i)
        print(f"link list : {l1}")

    for i in data:
        i = i.split(":")
        if int(i[0]) > l1.size or int(i[0]) < 0:
            print("Data cannot be added")
            if len(l1) == 0:
                print("List is empty")
            else:
                print(f"link list : {l1}")
        else:
            print(f"index = {i[0]} and data = {i[1]}")
            l1.insert(int(i[0]),int(i[1]))
            print(f"link list : {l1}")
            
        
        

solver(inp)