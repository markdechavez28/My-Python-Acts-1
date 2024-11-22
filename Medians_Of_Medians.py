def partition(arr, low, high):
    
    pivot = arr[high] 
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1

def find_median_of_medians(arr):
    
    n = len(arr)
    if n <= 5:
        return sorted(arr)[n // 2]  

    sublists = [arr[i:i + 5] for i in range(0, n, 5)]
    
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    return find_median_of_medians(medians)

def median_of_medians_select(arr, low, high, k):
    
    if low == high:
        return arr[low]

    pivot = find_median_of_medians(arr[low:high+1])

    pivot_index = arr.index(pivot, low, high + 1)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low] 
    partition_index = partition(arr, low, high)
    
    if k == partition_index:
        return arr[k]
    elif k < partition_index:
        return median_of_medians_select(arr, low, partition_index - 1, k)
    else:
        return median_of_medians_select(arr, partition_index + 1, high, k)

arr = [7, 2, 9, 4, 1, 3, 5, 6]
k = 3

print(f"The {k+1}rd smallest element is: {median_of_medians_select(arr, 0, len(arr) - 1, k)}")
