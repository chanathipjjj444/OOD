a = input("Enter num and sub : ").split()
real = [int(i) for i in a]

def weird(real):
    count = real[1]
    num = real[0]

    for i in range(count):
        if num % 10 != 0:
            num -= 1
        else:
            num = int(num / 10)
    return num

print(weird(real))