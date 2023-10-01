def insertion_sort(arr):
    for i in range(1, len(arr)):
        iEle = arr[i]
        for l in range(i, -1, -1):
            if iEle <= arr[l -1] and l > 0:
                arr[l] = arr[l-1]
            else:
                arr[l] = iEle
                break
    return arr

def push_in(arr):
    arr2 = arr
    arr = [int(i) for i in arr if int(i) >= 0]
    arr = insertion_sort(arr)
    j = 0
    for i in range(len(arr2)):
        if arr2[i] >= 0:
            arr2[i] = arr[j]
            j += 1
    return arr2

inp = [int(i) for i in input("Enter Input : ").split()]


for i in push_in(inp):
    print(i, end=" ")

