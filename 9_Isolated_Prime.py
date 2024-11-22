def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_isolated_prime(num):
    if is_prime(num):
        return not (is_prime(num - 2) or is_prime(num + 2))
    return False

def main(): 
    n = int(input("Enter n: "))
    print(f"Enter {n} numbers:")
    numbers = [int(input()) for _ in range(n)]
    
    for num in numbers:
        result = "YES" if is_isolated_prime(num) else "NO"
        print(f"{num}: {result}")

if __name__ == "__main__":
    main()
