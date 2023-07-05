print(" *** String count ***")
message = input("Enter message : ")
u_upper = []
u_lower = []
upper = []
lower = []
no_upper = 0 
no_lower = 0

for i in message:
    if i.isupper():
        no_upper += 1
        u_upper.append(i)
    if i.islower():
        no_lower += 1
        u_lower.append(i)
for x in u_upper:
    if x not in upper:
        upper.append(x)

for x in u_lower:
    if x not in lower:
        lower.append(x)

print(f"No. of Upper case characters : {no_upper}")
print(f"Unique Upper case characters : ", end="")
upper.sort()
lower.sort()
for i in upper:
    print(i, end="  ")
print(f"\nNo. of Lower case Characters : {no_lower}")
print(f"Unique Lower case characters : ", end="")
for i in lower:
    print(i, end="  ")