inp = [int(i) for i in input("Data : ").split()]
lis = 1
ans = [inp[0]]
print(f"1 : {ans}")

for i in range(1, len(inp)):
    for j in range(len(ans)):
        if inp[i] > ans[-1]:
            ans.append(inp[i])
            if len(ans) > lis:
                lis = len(ans)
            break
        else:
            if len(ans) == 1:
                ans[-1] = inp[i]
            else:
                ans.pop(-1)
            
    print(f"{i + 1} : {ans}")
print(f"longest increasing subsequence : {lis}")