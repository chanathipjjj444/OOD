rom = {"M":1000, "CM":900, "D":500, "CD": 400, "C":100, "XC":90, 
       "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

class translator:
    def __init__(self):
        self.roman = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5,
                 "IV":5, "I":1}
        
    def deciToRoman(self, num):
        self.toRoman = num
        self.toRoman2 = num
        ans = ""
        for i in self.roman:
            d, m = divmod(self.toRoman2,self.roman[i])
            ans += i * d
            self.toRoman2 = m
        return ans 

    def romanToDeci(self, s):
        num = 0
        emt = []
        for i in s:
            emt.append(i)
        s = emt
        for i in range(len(s)):
            for j in self.roman:
                if s[i] == j:
                    num += self.roman[j]
            try:
                if s[i] == "C" and s[i+1] == "M":
                    num -= 200
                elif s[i] == "C" and s[i+1] == "D":
                    num -= 200
                elif s[i] == "X" and s[i+1] == "C":
                    num -= 20
                elif s[i] == "X" and s[i+1] == "L":
                    num -= 20
                elif s[i] == "I" and s[i+1] == "X":
                    num -= 2
                elif s[i] == "I" and s[i+1] == "V":
                    num -= 2
            except:
                pass
        return num
            



num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))