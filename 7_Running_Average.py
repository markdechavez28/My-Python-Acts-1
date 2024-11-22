N = int(input("Enter the number of integers: "))
total_sum = 0

for i in range(1, N+1):
    num = int(input(f"Enter integer {i}: "))
    total_sum += num
    ave = total_sum/i
    print(f"Running average after {i} integers: {ave:.2f}")