class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, size, MaxCollision) -> None:
        self.table = [None] * size
        self.size = size
        self.max = MaxCollision
        self.n = 1
    
    def display(self):
        for i in range(len(self.table)):
            print(f"#{i + 1}	{self.table[i]}")
        print("---------------------------")

    def find_index(self, data: Data):
        # print(data.key)
        index = sum((ord(char) for char in data.key)) % self.size

        return index

    def hashing(self, data: Data):
        index = self.find_index(data)
        temp = index
        n = 1
        count  = 1
        
        
        while self.table[temp] is not None:
            
            print(f"collision number {n} at {temp}")
            temp = (index + (n*n)) % self.size
            
            if count == self.max:
                print("Max of collisionChain")
                self.display()
                return
            n += 1
            count +=1 
            
        if self.table[temp] is None:
            self.table[temp] = data
            
        self.display()
            
        
    def table_full(self):
        if None in self.table:
            return False
        return True
    
print(" ***** Fun with hashing *****")

inp , data = input("Enter Input : ").split('/')

data = data.split(",")
table_size , max_collision = inp.split()
table_size, max_collision = int(table_size), int(max_collision)

h = hash(table_size, max_collision)

for i in data:
    key, val = i.split()
    j = Data(key, val)
    if h.table_full():
        print("This table is full !!!!!!")
        quit()
    h.hashing(j)
