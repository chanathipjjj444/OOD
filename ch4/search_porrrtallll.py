class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    

    def __getitem__(self, i:int):
        return self.items[i]

inp = input("Enter width, height, and room: ").split()

max_x = int(inp[0])
max_y = int(inp[1])
map = inp[2].split(",")
print(map)

def add_pos(map):
    axis = Queue()
    for line in map:
        line = line.split()
        print(line)
        for item in line:
            if item == "_":
                axis.enQueue([line.index(item), map.index(line)])


def walk(map,add_pos:Queue):
    pass


add_pos(map)