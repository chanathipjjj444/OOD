inp = [int(i) for i in input('Enter tree: ').split()]

def to_left(num):
    return 2*num + 1 

def to_right(num):
    return 2*num + 2

def find_path(tree, index):
    if index >= len(tree):
        return []
    
    max_left = find_path(tree, to_left(index))
    max_right = find_path(tree, to_right(index))

    if sum(max_left) > sum(max_right):
        return [tree[index]] + max_left
    else:
        return [tree[index]] + max_right
    
print(f"Maximum path: {find_path(inp, 0)}")
