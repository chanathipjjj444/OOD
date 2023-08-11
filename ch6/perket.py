def power(base, top, ans=1):
    if top > 0:
        ans = ans * base
        power(base, top - 1, ans)
    if top == 0:
        print(ans)


def sour(sour_l: list):
    if len(sour_l) == 0:
        return 1
    return sour_l[0] * sour(sour_l[1:])


def bitter(bitter_l: list):
    if len(bitter_l) == 0:
        return 0
    else:
        return bitter_l[0] + bitter(bitter_l[1:])


inp = input("Enter Input : ").split(",")
sour_l = []
bitter_l = []

for i in inp:
    i = i.split(" ")
    sour_l.append(int(i[0]))
    bitter_l.append(int(i[1]))


print(sour(sour_l))
print(bitter(bitter_l))
print(abs(sour(sour_l) - bitter(bitter_l)))
