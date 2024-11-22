a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b**2) - (4*a*c)

# Correcting the order of operations
root1 = (-b + discriminant**0.5) / (2*a)
root2 = (-b - discriminant**0.5) / (2*a)

print(f"Root 1 = {root1:.2f}")
print(f"Root 2 = {root2:.2f}")
