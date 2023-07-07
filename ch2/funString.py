class funString():

    def __init__(self, str1, str2):
        self.string1 = str1
        self.mode = str2

    def __str__(self):
        pass

    def size(self) :
        return  len(self.string1)

    def changeSize(self):
        i = 0
        ch2 = ""
        while str1[i:]:
            ch = ord(str1[i])
            if ch > 64 and ch < 91:
                ch2 += chr(ch+32)
            elif ch > 96 and ch < 123:
                ch2 += chr(ch-32)
            else:
                ch2 += chr(ch)
            i += 1
        return ch2

    def reverse(self):
        return str1[::-1]

    def deleteSame(self):
        ans = []
        emt = [i for i in str1]
        emt.sort()
        for i in emt:
            if i not in ans:
                ans.append(i)
        return "".join(ans)


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1, str2)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())