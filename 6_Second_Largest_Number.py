x = int(input("Enter the size of the array: "))
print(f"Enter {x} elements: ")
array = []
count = 0

while count != x:
    element = int(input()) 
    array.append(element)
    count += 1

max_value = max(array)
array.remove(max_value)

y = max(array)

print(f"The second largest element is {y}")
