seconds = int(input("Enter the number of seconds: "))

hour = seconds // 3600
x = seconds % 3600
minute = x // 60
second = x % 60

print(f"{hour:02}:{minute:02}:{second:02}")