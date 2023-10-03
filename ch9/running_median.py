def partition(array, low, high):
    pivot = array[high]
    i = low - 1 
    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            (array[i],array[j]) = (array[j],array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        
        pivot = partition(array, low, high )
        
        quick_sort(array,low,pivot - 1)
        
        quick_sort(array, pivot + 1, high)
        
        
def find_median(arr):
    if len(arr) % 2 == 0:
        return (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2) - 1]) / 2
    else:
        return float(arr[len(arr) // 2])


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "quick sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
    
else:
    l=list(map(int, l))
    
    for i in range(len(l)):
        arr = [l[j] for j in range(l.index(l[i]) + 1)]
        print("list = ",arr, end=" ")
        n = len(arr)
        quick_sort(arr, 0, n - 1)
        print(f": median = {find_median(arr)}")