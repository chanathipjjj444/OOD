def bi_search(arr, l, r, x):
    
    if r >= l:
        
        mid = (l +r) // 2
        
        if arr[mid] == x:
            return True 
        
        elif arr[mid] >= x:
            return bi_search(arr, l, mid-1, x)

        else:
            return bi_search(arr, mid+1, r, x)
    else:
        return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(sorted(arr), 0, len(arr) - 1, k))