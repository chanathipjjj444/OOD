
class MyInt:
    def __init__(self,toRoman):
        self.toRoman = toRoman
        self.toRoman2 = toRoman

    def roamnumber(self):
        roman = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5,
                 "IV":5, "I":1}
        ans = ""
        for i in roman:
            d, m = divmod(self.toRoman2,roman[i])
            ans += i * d
            self.toRoman2 = m
        return ans 
    
    def __add__(self, val2):
        return MyInt((self.toRoman + val2.toRoman) + int((self.toRoman + val2.toRoman)/2))


print(" *** class MyInt ***")
a,b = input("Enter 2 number : ").split()

roam1 = MyInt(int(a))
roam2 = MyInt(int(b))
c = roam1 + roam2

print(f"{a} convert to Roman : {roam1.roamnumber()}")
print(f"{b} convert to Roman : {roam2.roamnumber()}")
print(f"{a} + {b} = {c.toRoman}")

