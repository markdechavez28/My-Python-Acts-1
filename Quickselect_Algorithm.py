import random

def partition(arr, low, high):
   
    pivot = arr[high]  
    i = low - 1  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1

def quickselect(arr, low, high, k):
    
    if low == high:
        return arr[low]
    
    pivot_index = random.randint(low, high) 
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  
    
    partition_index = partition(arr, low, high)
    
    if k == partition_index:
        return arr[k]
    elif k < partition_index:
        return quickselect(arr, low, partition_index - 1, k) 
    else:
        return quickselect(arr, partition_index + 1, high, k)  

arr = [7, 2, 9, 4, 1, 3, 5, 6]
k = 3  

print(f"The {k+1}rd smallest element is: {quickselect(arr, 0, len(arr) - 1, k)}")

