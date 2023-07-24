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
    
    # def __str__(self) -> str:
    #     return self.items

    def __getitem__(self, i:int):
        return self.items[i]

inp = input("Enter width, height, and room: ")

trig = False
for i in inp:
    if i == "F":
        trig = True

if trig == False:
    print("Invalid map input.12")
    exit()

inp = inp.split()

max_x = int(inp[0])
max_y = int(inp[1])
print("max x",max_x,"max_y", max_y)

map = inp[2].split(",")

if len(map) != max_y:
    print("Invalid map input.")
    exit()   
for i in map:
    if len(i) != max_x:
        print("Invalid map input.")
        exit()

def check_list(map):
    axis = Queue()
    start = Queue()
    for line in map:
        for c, letter in enumerate(line):
            if letter == "_":
                axis.enQueue((c,map.index(line)))
            if letter == "F":
                start.enQueue((c,map.index(line)))
            c += 1
    return axis , start


def walk(map,check_list:Queue):
    axis, start = check_list(map)
    if axis.isEmpty():
        print("Cannot reach the exit portal.")
        exit()
    went = Queue()
    distance = [(-1, 0), (0,1), (1,0), (0,-1)]
    print("axis", axis.items)
    while not axis.isEmpty():
        # print(start.items)
        print("Queue: ", start.items)
        dq = start.deQueue()
        y1 ,x1 = dq[0], dq[1]

        for x2, y2 in distance:
            (new_x, new_y) = (x1 + x2 , y1 + y2)
            # print(new_x,new_y)
            if 0 <= new_x < max_y and 0 < new_y <= max_x and map[new_x][new_y] == "_" and (new_y, new_x) not in went:
                start.enQueue((new_y, new_x))
                went.enQueue((new_y,new_x))
            if 0 <= new_x < max_y and 0 < new_y <= max_x and map[new_x][new_y] == "O" and (new_y, new_x) not in went:
                print("Found the exit portal.")
                exit()




walk(map, check_list)


