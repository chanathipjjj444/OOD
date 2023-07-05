print("*** Fun with permute ***")
a = input("Enter num1 num2 : ").split(",")
ans = []
print(f"Original Cofllection:  {a}")

def perm(a, k=0):
   if k == len(a):
      print(a)

   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]


perm(a=a)
print(f"Collection of distinct numbers: \n{ans}")