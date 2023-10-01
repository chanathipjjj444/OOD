def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = 0 #left_arr
        j = 0 #right_arr
        k = 0 #merged_arr

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j  += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        
inp = [int(x) for x in input('input : ').split()]
pair = []
sum = 0

for i in range(0, len(inp) - 1, 2):
    pair.append((inp[i],inp[i + 1]))

merge_sort(pair)


for i in range(len(pair)):
    for j in range(i - 1, -1, -1):
        # print(f"pair 0 {pair[i][0], pair[j][0]} and {pair[i][1], pair[j][1]}")
        if pair[i][0] > pair[j][0] and pair[i][1] < pair[j][1]:
            sum += pair[i][0]
            sum += pair[j][0]

print(f"ans = {sum}")