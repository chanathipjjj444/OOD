print("*** Fun with Drawing ***")
a = int(input("Enter input : "))


def draw_triangle(a):
    for i in range(a):
        if i != 0:
            print("")
        for j in range(4*a - 3):
            if j ==  a - i-1 or j == a + i -1:
                print("*",end="")
            elif j == 3*a-i -3  or j == 3*a +i -3 :
                print("*",end="")
            elif (j >= a-i and j < a+i) or ( j >= 3*a - i-3 and j < 3*a+i -3):
                print("+", end="")
            else:
                print(".", end="")

def draw_bottom(a):
    for i in range(3*a -2 -a):
        print("")
        for j in range(4*a -3):
            if j == i + 1:
                print("*", end="")
            elif j == 4*a -i -5 :
                print("*", end="")
            elif (j >= i + 1 and j < 4*a - i -5):
                print("+", end="")
            else:
                print(".", end="")

draw_triangle(a)
draw_bottom(a)