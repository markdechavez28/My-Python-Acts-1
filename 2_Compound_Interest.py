P = float(input("Enter principal amount: ")) #1000
r = float(input("Enter annual interest (in percent): ")) / 100 #5
t = float(input("Enter time duration (in months): ")) / 12 #12
n = float(input("Enter number of times interest in compounded per year: ")) #12

A = P*(1+r/n)**(n*t)

print(f"Total amount after compound interest: {A:.2f}")