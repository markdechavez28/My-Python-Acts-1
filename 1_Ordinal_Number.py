def count_nth(x):
    sequence = ''

    for i in range(1, x+1):
        a = str(i)
        sequence += a

    answer = (sequence[n-1])

    print(f"The {x}th digit is: {answer}")

n = int(input("Enter an ordinal number: "))
count_nth(n)