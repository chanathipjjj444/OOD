inp1, inp2 = input("Enter str1,str2: ").split(",")

def isomorph(a, b):
    if [a.index(x) for x in a] == [b.index(y) for y in b]:
        print(f"{a} and {b} are Isomorphic")
    else:
        print(f"{a} and {b} are not Isomorphic")

isomorph(inp1, inp2)

