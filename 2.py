print("*** multiplication or sum ***")
num1,num2 = input("Enter num1 num2 : ").split()
result = int(num1) * int(num2)
re_sum = int(num1) + int(num2)
if result > 1000:
    print(f"The result is {re_sum}")
else:
    print(f"The result is {result}")