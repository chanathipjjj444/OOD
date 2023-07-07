b = input("Enter Your List : ").split()

if len(b) < 3:
    print(f"Array Input Length Must More Than {len(b)}")
    quit()

a = [int(i) for i in b]

def find_zero(a):
    ans = []
    countt = 0
    for i in a:
        if i == 0:
            countt += 1
    if countt >= 3 :
        ans.append([0,0,0])
    for i in a:
        for j in a:
            if j == i:
                break
            for k in a:
                if j == k:
                    break
                if i != j:
                    if int(i) + int(j) + int(k) == 0:
                        demo = [i, j, k]
                        demo.sort()
                        if demo not in ans:
                            ans.append(demo)
    return ans

print(find_zero(a))