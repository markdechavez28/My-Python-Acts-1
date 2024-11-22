def linear_search(array, target):
    for index in range(len(array)): 
        if array[index] == target:  
            return index 
    return -1  

array = [50, 71, 93, 153, 159, 299, 304, 355, 346, 417, 429, 446, 510, 529, 569]
target = 417

result = linear_search(array, target)

if result != -1:
    print(f"Value {target} found at index {result}.")
else:
    print("Value not found.")



