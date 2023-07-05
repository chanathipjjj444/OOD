print("*** Converting hh.mm.ss to seconds ***")
a,b,c = input("Enter hh mm ss : ").split()

if int(b) >= 60 or int(b) < 0:
    print(f"mm({b}) is invalid!")
    quit()
if int(c) >= 60 or int(c) < 0:
    print(f"mm({c}) is invalid!")
    quit()
if int(a) < 0:
    print(f"mm({a}) is invalid!")
    quit()

ans = "{:,}".format(int(a)*3600 + int(b)*60 + int(c))
if int(a) < 10:
    a = "0" +str(a)
if int(b) < 10:
    b = "0" +str(b)
if int(c) < 10:
    c = "0" +str(c)


print(f"{a}:{b}:{c} = {ans} seconds")