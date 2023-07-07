print("*** New Range ***")
inp = input("Enter Input : ").split()

if len(inp) == 3:
    a = float(inp[0])
    b = float(inp[1])
    c = float(inp[2])
elif len(inp) == 2:
    a = float(inp[0])
    b = float(inp[1])
    c = 1.0
elif len(inp) == 1:
    a = 0.0
    b = float(inp[0])
    c = 1.0

# ans = [1,2,3]
# ans = tuple(ans)


def Range(b:float,a,c):
    ans =[]
    ans.append(a)
    while a < b:
        if a + c < b:
            ans.append(round((a + c), 3))
            a += c
        else:
            break
        
    return tuple(ans)


print(Range(b,a,c))