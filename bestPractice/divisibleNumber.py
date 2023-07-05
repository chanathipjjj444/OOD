print(" *** Divisible number ***")
a = int(input("Enter a positive number : "))

ans = []
if a <= 0:
    print(f"{a} is OUT of range !!!")
    quit()

def printDivisors(n, count=0) :
    i = 1
    while i <= n :
        if (n % i==0) :
            ans.append(i)
            count += 1
        i = i + 1
    return count

    
num = printDivisors(a)
print("Output ==> ", end="")
for i in ans:
    print(i, end=" ")
print(f"\nTotal ==> {num}")