
a = ["__###","##_###","##__##","###__O"]
def find(a):
    for item in a:
        if "F" in item:
            axis = [item.index("F"), a.index(item)]
            return axis
    return "error"
        
print(find(a))
