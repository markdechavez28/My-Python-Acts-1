size = int(input("Enter the size of the array: "))
array = []

print("Enter the elements of the array: ")

elements = input().split()

array = [int(element) for element in elements]

max_element = max(array)

count_max = array.count(max_element)

print(f"The maximum element is {max_element}.")
